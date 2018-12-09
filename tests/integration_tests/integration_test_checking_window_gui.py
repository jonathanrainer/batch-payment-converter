import unittest
import wx
import datetime

from pathlib import Path

from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.formats import XeroFormat
from batch_payment_converter.converter.processed_payments import \
    NatwestBankLinePayment
from batch_payment_converter.gui.checking_window import CheckingWindow


class OpenNewCheckingWindow(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()
        self.processed_payments = self.converter.convert_file(
            Path("data", "input.csv"), XeroFormat, NatwestBankLinePayment
        )

    def test_create_new_checking_window(self):
        app = wx.App(0)
        _ = CheckingWindow(None, "Checking Window", self.processed_payments,
                           Path("output", "output-{0}.csv".format(
                               datetime.datetime.now().strftime(
                                   "%d%m%Y_%H%M%S"))))
        app.MainLoop()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
