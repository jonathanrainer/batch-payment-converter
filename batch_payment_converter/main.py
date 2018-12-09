import wx

from batch_payment_converter.gui.main_window import MainWindow

if __name__ == "__main__":
    app = wx.App(False)
    system = MainWindow(None, "Batch Payment Converter")
    app.MainLoop()