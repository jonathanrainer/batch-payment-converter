import wx
import re

from datetime import datetime

from wx.grid import Grid
from wx import MessageDialog

from batch_payment_converter.gui.gui_utils import GUIUtils
from batch_payment_converter.converter.converter import Converter


class CheckingWindow(wx.Frame):

    def __init__(self, parent, title, processed_payments, output_file_loc):
        wx.Frame.__init__(self, parent, title=title,
                          size=GUIUtils.calculate_window_size())

        self.margin_to_frame_edge = 25
        self.column_width = len(
            self.get_object_attrs_not_abstract(processed_payments))
        self.processed_payments = processed_payments
        self.attr_column_mapping = {}
        self.output_file_loc = output_file_loc

        self.title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.title = wx.StaticText(
            self, -1,
            style=wx.ALIGN_CENTER
        )
        self.title.SetLabelMarkup(
            "<span size=\"xx-large\" weight=\"bold\">"
            "Checking Window</span>")
        self.title_sizer.Add(self.title, 1, wx.ALL | wx.EXPAND,
                             self.margin_to_frame_edge)
        self.title_sizer.SetMinSize(200, 100)

        # Build up the grid to display the data
        self.grid_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid = Grid(self, -1)

        self.grid.CreateGrid(len(processed_payments), self.column_width)
        self.grid_sizer.Add(self.grid, wx.EXPAND)

        for col_id, attribute in enumerate(self.get_object_attrs_not_abstract(
                processed_payments)):
            self.grid.SetColLabelValue(col_id, processed_payments[0].__dict__[attribute].name)
            self.attr_column_mapping[attribute] = \
                (col_id, processed_payments[0].__dict__[attribute].name)

        for row_id, payment in enumerate(processed_payments):
            for col_id, attribute in enumerate(self.get_object_attrs_not_abstract(
                    processed_payments)):
                if isinstance(payment.__dict__[attribute].value, datetime):
                    self.grid.SetCellValue(
                        row_id, col_id,
                        payment.__dict__[attribute].value.strftime("%d/%m/%Y"))
                else:
                    self.grid.SetCellValue(
                        row_id, col_id, payment.__dict__[attribute].value)
                if isinstance(payment.__dict__[attribute].value, str) and \
                        re.match(r"X{6,14}", payment.__dict__[attribute].value):
                    for col_col_id, _ in enumerate(self.get_object_attrs_not_abstract(
                    processed_payments)):
                        self.grid.SetCellBackgroundColour(
                            row_id, col_col_id,
                            wx.Colour(238, 210, 2, wx.ALPHA_OPAQUE))
                elif not payment.__dict__[attribute].user_editable:
                    self.grid.SetReadOnly(row_id, col_id)

        self.grid.AutoSize()

        # Create a Confirm Button
        self.confirm_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.confirm_button = wx.Button(self, label="Confirm")
        self.confirm_button.Bind(wx.EVT_BUTTON, self.confirm)
        self.confirm_sizer.Add(self.confirm_button, 1, wx.EXPAND | wx.ALL,
                               self.margin_to_frame_edge)

        # Set up the base sizers

        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.base_sizer.Add(self.title_sizer, 1, wx.EXPAND | wx.ALL,
                            self.margin_to_frame_edge)
        self.base_sizer.Add(self.grid_sizer, 2,
                            wx.EXPAND|wx.ALL,
                            self.margin_to_frame_edge)
        self.base_sizer.Add(self.confirm_sizer, 1, wx.EXPAND| wx.ALL,
        self.margin_to_frame_edge)
        # Layout sizers
        self.SetSizer(self.base_sizer)
        self.SetAutoLayout(1)
        self.base_sizer.Fit(self)
        self.Show()

    @staticmethod
    def get_object_attrs_not_abstract(processed_payments):
        return sorted([x for x in dir(processed_payments[0]) if
         not x.startswith("_") and
         x in processed_payments[0].__dict__ and
         hasattr(processed_payments[0].__dict__[x], "value") and
         processed_payments[0].__dict__[x].value != ""],
                      key=lambda x: processed_payments[0].__dict__[x].ordinal)

    def confirm(self, _):
        # Go over all the rows and run the validator methods. If one of them fails throw up an error message flagging
        # where the error is
        for row_id, processed_payment in enumerate(self.processed_payments):
            for user_editable_attr in [y for y in
                      self.get_object_attrs_not_abstract(self.processed_payments) if
                      self.processed_payments[0].__dict__[y].user_editable]:
                column_id, _ = \
                    self.attr_column_mapping[user_editable_attr]
                if(not processed_payment.__dict__[user_editable_attr].validator(
                        self.grid.GetCellValue(row_id, column_id))):
                    error_dialog = \
                        MessageDialog(self,
                                      "Data Entered in Column '{}' on Row '{}' - '{}' "
                                      "does not match what was expected. \n"
                                      "Please alter the data and click confirm again.\n\n"
                                      "No data has been altered and no files have been created.".format(
                                          self.attr_column_mapping[user_editable_attr][1],
                                          row_id, self.grid.GetCellValue(row_id, column_id)
                                      ),
                                      "Data Error - Please Recheck the Table",
                                      wx.OK|wx.ICON_ERROR|wx.CENTRE)
                    error_dialog.ShowModal()
                    return
        # After the validity of the data is assured, set the values to the new values and begin the conversion process
        for row_id, processed_payment in enumerate(self.processed_payments):
            for user_editable_attr in [y for y in
                      self.get_object_attrs_not_abstract(self.processed_payments) if
                      self.processed_payments[0].__dict__[y].user_editable]:
                column_id, _ = \
                    self.attr_column_mapping[user_editable_attr]
                if isinstance(processed_payment.__dict__[user_editable_attr].value, datetime):
                    processed_payment.__dict__[user_editable_attr].value = datetime.strptime(
                        self.grid.GetCellValue(row_id, column_id), "%d/%m/%Y")
                else:
                    processed_payment.__dict__[user_editable_attr].value = \
                        self.grid.GetCellValue(row_id, column_id)
        converter = Converter()
        converter.write_output_file(self.output_file_loc,
                                    self.processed_payments)
        self.Close()
