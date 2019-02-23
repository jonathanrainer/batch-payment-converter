import unittest

from pathlib import Path

from batch_payment_converter.gui.checking_window import CheckingWindow
from batch_payment_converter.converter.formats import XeroFormat
from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.processed_payments import NatwestBankLinePayment, BarclaysPayment


class CheckingWindowTests(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_columns_in_output_file_order_natwest(self):
        # Create sets of processed payments
        self.processed_payments = self.converter.convert_file(
            Path("..", "..", "data", "input.csv"), XeroFormat, NatwestBankLinePayment
        )
        self.assertListEqual(
            CheckingWindow.get_object_attrs_not_abstract(self.processed_payments),
            [
                "T001", "T010", "T014", "T016", "T022", "T028", "T030"
            ]

        )

    def test_columns_in_output_file_order_barclays(self):
        # Create sets of processed payments
        self.processed_payments = self.converter.convert_file(
            Path("..", "..", "data", "input.csv"), XeroFormat, BarclaysPayment
        )
        self.assertListEqual(
            CheckingWindow.get_object_attrs_not_abstract(self.processed_payments),
            [
                "sort_code", "payee_name", "account_number", "amount", "account_name", "payment_type_identifier"
            ]

        )


if __name__ == '__main__':
    unittest.main()
