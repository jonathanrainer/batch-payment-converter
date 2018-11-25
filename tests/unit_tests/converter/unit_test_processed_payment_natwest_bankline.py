import unittest

from batch_payment_converter.converter.processed_payments import \
    NatwestBankLinePayment
from batch_payment_converter.converter.payments import Payment
from batch_payment_converter.converter.formats import XeroFormat


class TestNatwestBankLineInitialisation(unittest.TestCase):

    def setUp(self):
        self.raw_payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
             "Services Rendered"], XeroFormat()
        )

    def test_create_processed_payment(self):
        processed_payment = NatwestBankLinePayment(
            self.raw_payment
        )
        self.assertEqual(processed_payment.data["T001"], "01")
        self.assertEqual(processed_payment.data["T010"], "5600141214791")
        self.assertEqual(processed_payment.data["T014"], "399.78")
        self.assertEqual(processed_payment.data["T016"], "")
        self.assertEqual(processed_payment.data["T022"], "380012")
        self.assertEqual(processed_payment.data["T028"], "23452192")
        self.assertEqual(processed_payment.data["T030"], "Jane Smitherington")


class TestNatwestBankLinetOutput(unittest.TestCase):

    def setUp(self):
        self.raw_payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
             "Services Rendered"], XeroFormat()
        )
        self.processed_payment = NatwestBankLinePayment(self.raw_payment)

    def test_processed_payment_output(self):
        self.assertListEqual(
            list(self.processed_payment.output_payment()),
            [
                "", "", "", "01", "", "", "", "", "", "", "", "",
                "5600141214791", "", "", "", "399.78", "", "", "", "", "",
                "", "", "380012", "", "", "", "", "", "23452192", "",
                "Jane Smitherington", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "", "", "", ""

            ])


if __name__ == '__main__':
    unittest.main()
