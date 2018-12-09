import wx

from batch_payment_converter.gui.gui_utils import GUIUtils


class CheckingWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,
                          size=GUIUtils.calculate_window_size())


