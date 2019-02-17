from datetime import datetime,timedelta

from abc import ABC, abstractmethod


class ProcessedPayment(ABC):

    @abstractmethod
    def name(self):
        return

    @abstractmethod
    def output_payment(self):
        return


class ProcessedPaymentField(object):

    def __init__(self, name, value, user_editable):
        self.name = name
        self.value = value
        self.user_editable = user_editable


class NatwestBankLinePayment(ProcessedPayment):

    name = "Natwest BankLine"

    def __init__(self, raw_payment):
        self.H001 = ProcessedPaymentField(
            "Originating Customer Identifier", "", False)
        self.H002 = ProcessedPaymentField("Import File Name", "", False)
        self.H003 = ProcessedPaymentField("Bank Identifier", "", False)
        self.T001 = ProcessedPaymentField("Record Type", "01", False)
        self.T002 = ProcessedPaymentField("Template Indicator", "", False)
        self.T003 = ProcessedPaymentField("Template Reference", "", False)
        self.T004 = ProcessedPaymentField("Confidential Indicator", "", False)
        self.T005 = ProcessedPaymentField("Beneficiary Identifier", "", False)
        self.T006 = ProcessedPaymentField("Customer Payment Reference", "",
                                          False)
        self.T007 = ProcessedPaymentField("Destination Country", "", False)
        self.T008 = ProcessedPaymentField("Priority", "", False)
        self.T009 = ProcessedPaymentField("Routing Method", "", False)
        self.T010 = ProcessedPaymentField("Debit Account Identifier",
                                          "56001412147931", False)
        self.T011 = ProcessedPaymentField("Debit Charger Account Identifier",
                                          "", False)
        self.T012 = ProcessedPaymentField("Charges Code Type", "", False)
        self.T013 = ProcessedPaymentField("Payment Currency", "", False)
        self.T014 = ProcessedPaymentField("Payment Amount",
                                          str(raw_payment.amount), False)
        self.T015 = ProcessedPaymentField("Execution Date", "", False)
        self.T016 = ProcessedPaymentField(
            "Date Payment to Arrive (Credit Date)", datetime.now() + timedelta(days=2), True)
        self.T017 = ProcessedPaymentField("Ordering Institution Identifier", "",
                                          False)
        self.T018 = ProcessedPaymentField(
            "Ordering Institution Name and Address Line Number 1", "", False)
        self.T019 = ProcessedPaymentField(
            "Ordering Institution Name and Address Line Number 2", "", False)
        self.T020 = ProcessedPaymentField(
            "Ordering Institution Name and Address Line Number 3", "", False)
        self.T021 = ProcessedPaymentField(
            "Ordering Institution Name and Address Line Number 4", "", False)
        self.T022 = ProcessedPaymentField(
            "Account with Bank Identifier", raw_payment.sort_code, False)
        self.T023 = ProcessedPaymentField(
            "Account with Bank Account Number", "", False)
        self.T024 = ProcessedPaymentField(
            "Account with Bank Name and Address Line Number 1", "", False)
        self.T025 = ProcessedPaymentField(
            "Account with Bank Name and Address Line Number 2", "", False)
        self.T026 = ProcessedPaymentField(
            "Account with Bank Name and Address Line Number 3", "", False)
        self.T027 = ProcessedPaymentField(
            "Account with Bank Name and Address Line Number 4", "", False)
        self.T028 = ProcessedPaymentField(
            "Beneficiary Account Number", raw_payment.account_number, False)
        self.T029 = ProcessedPaymentField(
            "Beneficiary Institution Identifier", "", False)
        self.T030 = ProcessedPaymentField(
            "Beneficiary Name and Address Line Number 1",
            raw_payment.payee_name, False)
        self.T031 = ProcessedPaymentField(
            "Beneficiary Name and Address Line Number 2", "", False)
        self.T032 = ProcessedPaymentField(
            "Beneficiary Name and Address Line Number 3", "", False)
        self.T033 = ProcessedPaymentField(
            "Beneficiary Name and Address Line Number 4", "", False)
        self.T034 = ProcessedPaymentField("Beneficiary Reference", "", False)
        self.T035 = ProcessedPaymentField("FX Deal Reference", "", False)
        self.T036 = ProcessedPaymentField("FX Deal Exchange Rate", "", False)
        self.T037 = ProcessedPaymentField(
            "Information for the Beneficiary Line Number 1", "", False)
        self.T038 = ProcessedPaymentField(
            "Information for the Beneficiary Line Number 2", "", False)
        self.T039 = ProcessedPaymentField(
            "Information for the Beneficiary Line Number 3", "", False)
        self.T040 = ProcessedPaymentField\
            ("Information for the Beneficiary Line Number 4", "", False)
        self.T041 = ProcessedPaymentField("RTGS Required", "", False)
        self.T042 = ProcessedPaymentField("Credit Currency", "", False)
        self.T043 = ProcessedPaymentField("Intermediary Bank Identifier", "",
                                          False)
        self.T044 = ProcessedPaymentField(
            "Intermediary Bank Name and Address Line Number 1", "", False)
        self.T045 = ProcessedPaymentField(
            "Intermediary Bank Name and Address Line Number 2", "", False)
        self.T046 = ProcessedPaymentField(
            "Intermediary Bank Name and Address Line Number 3", "", False)
        self.T047 = ProcessedPaymentField(
            "Intermediary Bank Name and Address Line Number 4", "", False)
        self.T048 = ProcessedPaymentField(
            "Additional Codewords Number 1", "", False)
        self.T049 = ProcessedPaymentField(
            "Additional Codewords Text Number 1", "", False)
        self.T050 = ProcessedPaymentField(
            "Additional Codewords Number 2", "", False)
        self.T051 = ProcessedPaymentField(
            "Additional Codewords Text Number 2", "", False)
        self.T052 = ProcessedPaymentField(
            "Additional Codewords Number 3", "", False)
        self.T053 = ProcessedPaymentField(
            "Additional Codewords Text Number 3", "", False)
        self.T054 = ProcessedPaymentField(
            "Additional Codewords Number 4", "", False)
        self.T055 = ProcessedPaymentField(
            "Additional Codewords Text Number 4", "", False)
        self.T056 = ProcessedPaymentField(
            "Additional Codewords Number 5", "", False)
        self.T057 = ProcessedPaymentField(
            "Additional Codewords Text Number 5", "", False)
        self.T058 = ProcessedPaymentField(
            "Additional Codewords Number 6", "", False)
        self.T059 = ProcessedPaymentField(
            "Additional Codewords Text Number 6", "", False)
        self.T060 = ProcessedPaymentField(
            "Additional Codewords Number 7", "", False)
        self.T061 = ProcessedPaymentField(
            "Additional Codewords Text Number 7", "", False)
        self.T062 = ProcessedPaymentField(
            "Additional Codewords Number 8", "", False)
        self.T063 = ProcessedPaymentField(
            "Additional Codewords Text Number 8", "", False)
        self.T064 = ProcessedPaymentField(
            "Additional Codewords Number 9", "", False)
        self.T065 = ProcessedPaymentField(
            "Additional Codewords Text Number 9", "", False)
        self.T066 = ProcessedPaymentField(
            "Additional Codewords Number 10", "", False)
        self.T067 = ProcessedPaymentField(
            "Additional Codewords Text Number 10", "", False)
        self.T068 = ProcessedPaymentField(
            "Regulatory Reporting Line Number 1", "", False)
        self.T069 = ProcessedPaymentField(
            "Regulatory Reporting Line Number 2", "", False)
        self.T070 = ProcessedPaymentField(
            "Regulatory Reporting Line Number 3", "", False)
        self.T071 = ProcessedPaymentField(
            "Remittance Advice Indicator", "", False)
        self.T072 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Address Line 1", "", False)
        self.T073 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Address Line 2", "", False)
        self.T074 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Address Line 3", "", False)
        self.T075 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Address Line 4", "", False)
        self.T076 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Fax Number", "", False)
        self.T077 = ProcessedPaymentField(
            "Remittance Advice Beneficiary Email Address", "", False)
        self.T078 = ProcessedPaymentField(
            "By Order of Account", "", False)
        self.T079 = ProcessedPaymentField(
            "By Order of Name", "", False)
        self.T080 = ProcessedPaymentField(
            "By Order of Address Line 1", "", False)
        self.T081 = ProcessedPaymentField(
            "By Order of Address Line 2", "", False)
        self.T082 = ProcessedPaymentField(
            "By Order of Address Line 3", "", False)

    def __str__(self):
        return "{0} | {1} | {2} | {3}".format(self.T014, self.T022, self.T028,
                                              self.T030)

    def output_payment(self):
        return [
            "", self.H001.value, self.H002.value, self.H003.value, self.T001.value,
            self.T002.value, self.T003.value, self.T004.value, self.T005.value,
            self.T006.value, self.T007.value, self.T008.value, self.T009.value,
            self.T010.value, self.T011.value, self.T012.value, self.T013.value,
            self.T014.value, self.T015.value, self.T016.value.strftime("%d%m%Y"),
            self.T017.value,
            self.T018.value, self.T019.value, self.T020.value, self.T021.value,
            self.T022.value, self.T023.value, self.T024.value, self.T025.value,
            self.T026.value, self.T027.value, self.T028.value,
            self.T029.value, self.T030.value, self.T031.value, self.T032.value,
            self.T033.value, self.T034.value, self.T035.value, self.T036.value,
            self.T037.value, self.T038.value, self.T039.value, self.T040.value,
            self.T041.value, self.T042.value, self.T043.value, self.T044.value,
            self.T045.value, self.T046.value, self.T047.value, self.T048.value,
            self.T049.value, self.T050.value, self.T051.value, self.T052.value,
            self.T053.value, self.T054.value, self.T055.value, self.T056.value,
            self.T057.value, self.T058.value, self.T059.value, self.T060.value,
            self.T061.value, self.T062.value, self.T063.value, self.T064.value,
            self.T065.value, self.T066.value, self.T067.value, self.T068.value,
            self.T069.value, self.T070.value, self.T071.value, self.T072.value,
            self.T073.value, self.T074.value, self.T075.value, self.T076.value,
            self.T077.value
            ]


class BarclaysPayment(ProcessedPayment):

    name = "Barclays"

    def __init__(self, raw_payment):
        self.sort_code = ProcessedPaymentField(
            "Sort Code", raw_payment.sort_code, False)
        self.payee_name = ProcessedPaymentField(
            "Payee Name", raw_payment.payee_name, False)
        self.account_number = ProcessedPaymentField(
            "Account Number", raw_payment.account_number, False)
        self.amount = ProcessedPaymentField("Amount", raw_payment.amount, False)
        self.account_name = ProcessedPaymentField("Account Name",
                                                  "<<TO BE INSERTED>>", True)
        self.payment_type_identifier = ProcessedPaymentField(
            "Payment Type Identifier", "99", False)

    def __str__(self):
        return "{0} | {1} | {2} | {3}".format(
            self.payee_name, self.sort_code, self.account_number, self.amount)

    def output_payment(self):
        return [
            self.sort_code.value, self.payee_name.value,
            self.account_number.value, self.amount.value,
            self.account_name.value, self.payment_type_identifier.value, "/"
        ]
