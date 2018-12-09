import wx


class GUIUtils(object):

    @staticmethod
    def calculate_window_size():
        display_tuple = wx.GetDisplaySize()
        return display_tuple[0]/2 + 20, -1