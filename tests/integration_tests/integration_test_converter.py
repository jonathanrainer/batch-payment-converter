import unittest
import os

from pathlib import Path

from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.formats import XeroFormat
from batch_payment_converter.converter.processed_payments import \
    NatwestBankLinePayment


class ConvertFileNoFrontend(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert_file_no_frontend(self):
        self.converter.convert_file(
            Path("data", "input.csv"), XeroFormat,
            Path("output", "output.csv"), NatwestBankLinePayment
        )
        self.assertTrue(os.path.isfile(str(Path("output", "output.csv"))))

    def test_processing_payments(self):
        payments = self.converter.import_csv(Path("data", "input.csv"), XeroFormat)

if __name__ == '__main__':
    unittest.main()
