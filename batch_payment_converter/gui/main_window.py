import wx

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        # Create the initial frame
        wx.Frame.__init__(self, parent, title=title,
                          size=self.calculate_window_size())

        # Create sizers for each layout element

        self.title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.title = wx.StaticText(
            self, -1,
            style=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL
        )
        self.title.SetLabelMarkup("<big> Batch Payment File Converter "
                                  "</big>")
        self.title_sizer.Add(self.title, 1, wx.EXPAND)

        # Create a sizer for the input box at the top
        self.input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_text_box = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.browse_input_button = wx.Button(self, label="Browse")
        self.input_sizer.Add(self.input_text_box, 5, wx.EXPAND)
        self.input_sizer.Add(self.browse_input_button, 1, wx.EXPAND)

        # Create a sizer for the box to specify outputs
        self.output_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.output_text_box = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.browse_output_button = wx.Button(self, label="Browse")
        self.output_sizer.Add(self.output_text_box, 5, wx.EXPAND)
        self.output_sizer.Add(self.browse_output_button, 1, wx.EXPAND)

        # Create a sizer for the box that controls the input format and file
        # type
        self.control_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_radio = wx.RadioBox(self, choices=["Xero"])
        self.output_radio = wx.RadioBox(self, choices=
            ["Natwest BankLine", "Barclays"])
        self.control_sizer.Add(self.input_radio, 1, wx.EXPAND)
        self.control_sizer.Add(self.output_radio, 1, wx.EXPAND)

        # Create the sizer for the convert button at the bottom
        self.convert_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.convert_button = wx.Button(self, label="Convert")
        self.convert_sizer.Add(self.convert_button, 1, wx.EXPAND)

        # Create a sizer to separate
        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.base_sizer.Add(self.title_sizer, 1, wx.EXPAND)
        self.base_sizer.Add(self.input_sizer, 2, wx.EXPAND)
        self.base_sizer.Add(self.output_sizer, 2, wx.EXPAND)
        self.base_sizer.Add(self.control_sizer, 2, wx.EXPAND)
        self.base_sizer.Add(self.convert_sizer, 1, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.base_sizer)
        self.SetAutoLayout(1)
        self.base_sizer.Fit(self)
        self.Show()

    def calculate_window_size(self):
        display_tuple = wx.GetDisplaySize()
        return display_tuple[0]/2, -1
