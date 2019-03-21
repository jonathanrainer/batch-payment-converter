import unittest

from datetime import datetime, timedelta

from batch_payment_converter.converter.processed_payments import \
    NatwestBankLinePayment
from batch_payment_converter.converter.payments import Payment
from batch_payment_converter.converter.formats import XeroFormat
from tests.test_utils import TestUtils


class TestNatwestBankLineInitialisation(unittest.TestCase):

    def setUp(self):
        self.raw_payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
             "Services Rendered"], XeroFormat()
        )
        self.test_utils = TestUtils()

    def test_create_processed_payment(self):
        processed_payment = NatwestBankLinePayment(
            self.raw_payment
        )
        self.assertEqual(processed_payment.T001.value, "01")
        self.assertEqual(processed_payment.T010.value, "56001412147931")
        self.assertEqual(processed_payment.T014.value, "399.78")
        self.assertEqual(processed_payment.T016.value, datetime.now() +
                         self.test_utils.calculate_working_days(datetime.now(), 2))
        self.assertEqual(processed_payment.T022.value, "380012")
        self.assertEqual(processed_payment.T028.value, "23452192")
        self.assertEqual(processed_payment.T030.value, "Jane Smitherington")


class TestNatwestBanklineWorkingDayCalculation(unittest.TestCase):
    def setUp(self):
        self.raw_payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
             "Services Rendered"], XeroFormat()
        )

    def test_working_day_calculator(self):
        processed_payment = NatwestBankLinePayment(
            self.raw_payment
        )
        self.assertEqual(processed_payment.calculate_working_days(datetime(2019, 1, 23), 2), timedelta(days=2))
        self.assertEqual(processed_payment.calculate_working_days(datetime(2019, 1, 23), 4), timedelta(days=6))


class TestNatwestBankLinetOutput(unittest.TestCase):

    def setUp(self):
        self.raw_payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
             "Services Rendered"], XeroFormat()
        )
        self.processed_payment = NatwestBankLinePayment(self.raw_payment)
        self.test_utils = TestUtils()

    def test_processed_payment_output(self):
        date_string = (datetime.now() + self.test_utils.calculate_working_days(datetime.now(), 2)).strftime("%d%m%Y")
        self.assertListEqual(
            list(self.processed_payment.output_payment()),
            [
                "", "", "", "01", "", "", "", "", "", "", "", "",
                "56001412147931", "", "", "", "399.78", "", date_string, "", "", "",
                "", "", "380012", "", "", "", "", "", "23452192", "",
                "Jane Smitherington", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", ""

            ])


if __name__ == '__main__':
    unittest.main()
