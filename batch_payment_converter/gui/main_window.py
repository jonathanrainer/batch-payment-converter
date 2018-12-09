import wx
import datetime

from pathlib import Path

from batch_payment_converter.converter.formats import *
from batch_payment_converter.converter.processed_payments import *
from batch_payment_converter.converter.converter import Converter


class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        # Create the initial frame
        wx.Frame.__init__(self, parent, title=title,
                          size=self.calculate_window_size())

        self.margin_to_frame_edge = 25
        # Create sizers for each layout element

        self.title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.title = wx.StaticText(
            self, -1,
            style=wx.ALIGN_CENTER
        )
        self.title.SetLabelMarkup(
            "<span size=\"xx-large\" weight=\"bold\">"
            "Batch Payment File Converter</span>")
        self.title_sizer.Add(self.title, 1, wx.ALL | wx.EXPAND,
                             self.margin_to_frame_edge)
        self.title_sizer.SetMinSize(200, 100)

        # Create a sizer for the input box at the top
        self.input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_label = wx.StaticText(
            self, 0,
            style=wx.ALIGN_CENTER
        )
        self.input_label.SetLabelMarkup("<b>Input File Location</b>")
        self.input_text_box = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.browse_input_button = wx.Button(self, label="Browse")
        self.input_sizer.Add(
            self.input_label, 1,
            wx.EXPAND | wx.TOP | wx.WEST, 35+self.margin_to_frame_edge)
        self.input_sizer.Add(
            self.input_text_box, 5,
            wx.EXPAND | wx.ALL, 15+self.margin_to_frame_edge)
        self.input_sizer.Add(
            self.browse_input_button, 1,
            wx.EXPAND | wx.ALL | wx.EAST, self.margin_to_frame_edge)
        self.browse_input_button.Bind(wx.EVT_BUTTON, self.browse_input_file)


        # Create a sizer for the box to specify outputs
        self.output_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.output_label = wx.StaticText(
            self, 0,
            style=wx.ALIGN_CENTER
        )
        self.output_label.SetLabelMarkup("<b>Output File Location</b>")
        self.output_text_box = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.browse_output_button = wx.Button(self, label="Browse")
        self.output_sizer.Add(
            self.output_label, 1,
            wx.EXPAND | wx.TOP | wx.WEST, 35+self.margin_to_frame_edge)
        self.output_sizer.Add(
            self.output_text_box, 5,
            wx.EXPAND | wx.ALL, 15+self.margin_to_frame_edge)
        self.output_sizer.Add(
            self.browse_output_button, 1,
            wx.EXPAND | wx.ALL, self.margin_to_frame_edge)
        self.browse_output_button.Bind(wx.EVT_BUTTON, self.browse_output_file)

        # Create a sizer for the box that controls the input format and file
        # type
        self.control_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.control_ver_sizer_l = wx.BoxSizer(wx.VERTICAL)
        self.control_ver_sizer_r = wx.BoxSizer(wx.VERTICAL)
        self.input_radio = wx.RadioBox(
            self, choices=[
                x.name for x in InputFormat.__subclasses__()
            ])
        self.input_radio_label = wx.StaticText(
            self, 0, style = wx.ALIGN_CENTRE
        )
        self.output_radio_label = wx.StaticText(
            self, 0, style=wx.ALIGN_CENTRE
        )
        self.input_radio_label.SetLabelMarkup("Input File Format")
        self.output_radio_label.SetLabelMarkup("Output File Format")
        self.output_radio = wx.RadioBox(
            self, choices=[
                x.name for x in ProcessedPayment.__subclasses__()
            ]
        )
        self.control_ver_sizer_l.Add(self.input_radio_label, 1, wx.CENTER)
        self.control_ver_sizer_l.Add(self.input_radio, 4,
                               wx.EXPAND|wx.ALL, self.margin_to_frame_edge)
        self.control_ver_sizer_r.Add(self.output_radio_label, 1, wx.CENTER)
        self.control_ver_sizer_r.Add(self.output_radio, 4,
                               wx.EXPAND | wx.ALL, self.margin_to_frame_edge)
        self.control_sizer.Add(self.control_ver_sizer_l, wx.EXPAND)
        self.control_sizer.Add(self.control_ver_sizer_r, wx.EXPAND)

        # Create the sizer for the convert button at the bottom
        self.convert_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.convert_button = wx.Button(self, label="Convert")
        self.convert_button.Bind(wx.EVT_BUTTON, self.convert)
        self.convert_sizer.Add(self.convert_button, 1, wx.EXPAND|wx.ALL,
                               self.margin_to_frame_edge)

        # Create a sizer to separate
        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.base_sizer.Add(self.title_sizer, 1, wx.EXPAND)
        self.base_sizer.Add(self.input_sizer, 2, wx.EXPAND)
        self.base_sizer.Add(self.output_sizer, 2, wx.EXPAND)
        self.base_sizer.Add(self.control_sizer, 1, wx.EXPAND)
        self.base_sizer.Add(self.convert_sizer, 1, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.base_sizer)
        self.SetAutoLayout(1)
        self.base_sizer.Fit(self)
        self.Show()

    def calculate_window_size(self):
        display_tuple = wx.GetDisplaySize()
        return display_tuple[0]/2 + 20, -1

    def browse_input_file(self, _):
        with wx.FileDialog(self, "Choose Input File",
                           wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Set the contents of the
            self.input_text_box.write(str(Path(fileDialog.GetPath())))

    def browse_output_file(self, _):
        with wx.DirDialog(
                self, "Choose Output Folder Location",
                style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dirDialog:

            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Set the contents of the
            self.output_text_box.write(str(Path(dirDialog.GetPath())))

    def convert(self, _):
        # Check the input file still exists and throw up a dialog if it doesn't
        input_file = Path(self.input_text_box.GetValue())
        if not input_file.is_file():
            wx.MessageBox("Input File Not Found!",
                          "Cannot find input file: {0}".format(input_file),
                          wx.ICON_ERROR, self)
            return
        # Check the output location is legitimate
        output_folder = Path(self.output_text_box.GetValue())
        if not output_folder.is_dir():
            wx.MessageBox("Output Folder Not Found!",
                          "Cannot find input folder: {0}".format(output_folder),
                          wx.ICON_ERROR, self)
            return
        # Start the conversion process
        converter = Converter()
        converter.convert_file(
            input_file,
            [x for x in InputFormat.__subclasses__() if
             x.name == self.input_radio.GetItemLabel(
                 self.input_radio.GetSelection())
             ][0],
            Path(output_folder, "output-{0}.csv".format(
                datetime.datetime.now().strftime("%d%m%Y_%H%M%S"))
                 ),
            [x for x in ProcessedPayment.__subclasses__() if
             x.name == self.output_radio.GetItemLabel(
                 self.output_radio.GetSelection())
             ][0]
        )
        # Once completed open up the new grid to add in the dates and sort out
        # problematic sort codes etc.
