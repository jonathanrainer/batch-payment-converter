import unittest

from batch_payment_converter.converter.payments import Payment
from batch_payment_converter.converter.formats import XeroFormat


class TestPaymentInitialisationXero(unittest.TestCase):

    def setUp(self):
        self.payment = Payment(
            [399.78, "38001223452192", "Jane Smitherington", "P/L Payments",
            "Services Rendered"], XeroFormat()
        )

    def test_string_rendering(self):
        self.assertEqual(
            str(self.payment),
            "Jane Smitherington | 38-00-12 | 23452192 | £399.78 | "
            "Services Rendered")




if __name__ == '__main__':
    unittest.main()
