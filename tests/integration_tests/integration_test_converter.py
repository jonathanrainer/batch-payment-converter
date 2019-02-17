import unittest
import os
import csv
import glob

from datetime import datetime, timedelta
from pathlib import Path

from batch_payment_converter.converter.converter import Converter
from batch_payment_converter.converter.processed_payments import *
from batch_payment_converter.converter.formats import XeroFormat


class ConvertFileNoFrontend(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def tearDown(self):
        files = glob.glob("{0}{1}{2}".format(str(Path("..", "..", "output").absolute()), os.sep, "test_output*"))
        for f in files:
            os.remove(f)

    def create_file(self, format, output_file_name):
        processed_payments = self.converter.convert_file(
            Path("..", "..", "data", "input.csv"), XeroFormat, format
        )
        output_path = Path("..", "..", "output", output_file_name)
        return self.converter.write_output_file(output_path, processed_payments)

    def test_convert_file_no_frontend_natwest(self):
        output_path = self.create_file(NatwestBankLinePayment, "test_output_natwest")
        self.assertTrue(os.path.isfile(str(output_path)))

    def test_convert_file_no_frontend_barclays(self):
        output_path = self.create_file(BarclaysPayment, "test_output_barclays")
        self.assertTrue(os.path.isfile(str(output_path)))

    def test_natwest_dates_format_correct(self):
        output_path = self.create_file(NatwestBankLinePayment, "test_output_natwest_dates")
        # Check the output date format is correct
        with open(output_path) as csv_file:
            test_file_reader = csv.reader(csv_file)
            for row in test_file_reader:
                self.assertRegex(row[18], "[0-9]{8}")

    def test_line_endings(self):
        for subcls in ProcessedPayment.__subclasses__():
            if subcls != ProcessedPayment:
                output_path = self.create_file(subcls, "test_output_line_ending_file")
                with open(output_path) as csv_file:
                    for line in csv_file:
                        self.assertNotRegex(line, "^\n$")

    def test_convert_file_extension(self):
        for subcls in ProcessedPayment.__subclasses__():
            if subcls != ProcessedPayment:
                output_path = self.create_file(subcls, "test_output_line_ending_file")
                self.assertEqual(output_path.suffix, ".txt")

    def test_natwest_standard_date(self):
        output_path = self.create_file(NatwestBankLinePayment, "test_output_natwest_dates")
        with open(output_path) as csv_file:
            test_file_reader = csv.reader(csv_file)
            for row in test_file_reader:
                parsed_date = datetime.date(datetime.strptime(row[18], "%d%m%Y"))
                self.assertEqual(parsed_date, datetime.date(datetime.today()) + timedelta(days=2))


if __name__ == '__main__':
    unittest.main()
