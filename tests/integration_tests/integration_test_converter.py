import unittest
import os

from pathlib import Path

from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.formats import XeroFormat
from batch_payment_converter.converter.processed_payments import \
    NatwestBankLinePayment, BarclaysPayment


class ConvertFileNoFrontend(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert_file_no_frontend_natwest(self):
        self.converter.convert_file(
            Path("data", "input.csv"), XeroFormat,
            Path("output", "output_natwest.csv"), NatwestBankLinePayment
        )
        self.assertTrue(os.path.isfile(str(Path("output", "output_natwest.csv"))))

    def test_convert_file_no_frontend_barclays(self):
        self.converter.convert_file(
            Path("data", "input.csv"), XeroFormat,
            Path("output", "output_barclays.csv"), BarclaysPayment
        )
        self.assertTrue(os.path.isfile(str(Path("output", "output_barclays.csv"))))


if __name__ == '__main__':
    unittest.main()
