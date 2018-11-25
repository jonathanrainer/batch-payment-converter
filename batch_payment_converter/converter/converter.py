import csv

from .payments import Payment

class Converter(object):

    def convert_file(self, input_file_name, input_format, output_file_name,
                     output_format):
        # Take in the CSV file with the appropriate format object and convert
        # it into an object
        payments = self.import_csv(input_file_name, input_format)
        # Pass that object through the converter specified by the Output Format
        # Write the output file to the specified location
        return

    def import_csv(self, csv_path, input_format):
        payments = []
        with open(str(csv_path)) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    payments.append(Payment(row, input_format))
        return payments