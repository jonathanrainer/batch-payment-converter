import unittest
import os

from pathlib import Path

from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.input_formats import XeroFormat


class ConvertFileNoFrontend(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert_file_no_frontend(self):
        self.converter.convert_file(
            Path("data", "input.csv"), XeroFormat,
            Path("output", "output.csv"), None
        )
        self.assertTrue(os.path.isfile("output.csv"))

if __name__ == '__main__':
    unittest.main()
