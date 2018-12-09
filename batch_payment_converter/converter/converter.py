import csv

from .payments import Payment


class Converter(object):

    def convert_file(self, input_file_name, input_format, output_file_name,
                     output_class):
        # Take in the CSV file with the appropriate format object and convert
        # it into an object
        payments = self.import_csv(input_file_name, input_format)
        # Pass that object through the converter specified by the Output Format
        processed_payments = self.payments_to_output_format(payments,
                                                            output_class)
        return processed_payments

    @staticmethod
    def import_csv(csv_path, input_format):
        payments = []
        # Open the CSV file
        with open(str(csv_path)) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Ignoring blank rows append to a new payments object
                # the payments create by parsing the data from the raw file.
                if row:
                    payments.append(Payment(row, input_format))
        return payments

    @staticmethod
    def payments_to_output_format(payments, output_class):
        processed_payments = []
        for payment in payments:
            processed_payments.append(output_class(payment))
        return processed_payments

    @staticmethod
    def write_output_file(output_file, processed_payments):
        with open(str(output_file), 'w') as output:
            csv_writer = csv.writer(output)
            for proc_payment in processed_payments:
                csv_writer.writerow(proc_payment.output_payment())