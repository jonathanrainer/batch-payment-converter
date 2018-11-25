import wx

from payment_processor.interface import MainWindow

if __name__ == "__main__":
    app = wx.App(False)
    system = MainWindow(None, "Batch Payment Processor")
    app.MainLoop()