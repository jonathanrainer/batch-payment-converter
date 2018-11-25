from .exceptions import IncorrectSortCodeAccountNumberException


class Payment(object):

    amount = 0
    sort_code = ""
    account_number = ""
    payee_name = ""
    description = ""
    narrative = ""

    def __init__(self, raw_data, input_format):
        self.amount = raw_data[input_format.mapping["Amount"][0]]
        self.payee_name = raw_data[input_format.mapping["Payee"][0]]
        self.description = raw_data[input_format.mapping["Description"][0]]
        self.narrative = raw_data[input_format.mapping["Narrative"][0]]
        sort_code = input_format.mapping["Sort Code"][1](
            raw_data[input_format.mapping["Sort Code"][0]])
        if sort_code == "XXXXXX":
            raise IncorrectSortCodeAccountNumberException()
        else:
            self.sort_code = sort_code
        account_number = input_format.mapping["Account Number"][1](
            raw_data[input_format.mapping["Account Number"][0]])
        self.account_number = account_number

    def __str__(self):
        return "{0} | {1} | {2} | £{3} | {4}".format(
            self.payee_name, self.format_sort_code(self.sort_code),
            self.account_number, self.amount, self.narrative)

    def __repr__(self):
        return self.__str__()

    def format_sort_code(self, sort_code):
        return "{0}-{1}-{2}".format(
            sort_code[0:2], sort_code[2:4], sort_code[4:6])