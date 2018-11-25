from abc import ABC, abstractmethod
from collections import OrderedDict


class ProcessedPayment(ABC):

    @abstractmethod
    def output_payment(self):
        return

    @abstractmethod
    def name(self):
        return


class NatwestBankLinePayment(ProcessedPayment):

    name = "Natwest BankLine"


    def __init__(self, raw_payment):
        self.data = OrderedDict([
            ("H001", ""),
            ("H002", ""),
            ("H003", ""),
            ("T001", "01"),
            ("T002", ""),
            ("T003", ""),
            ("T004", ""),
            ("T005", ""),
            ("T006", ""),
            ("T007", ""),
            ("T008", ""),
            ("T009", ""),
            ("T010", "5600141214791"),
            ("T011", ""),
            ("T012", ""),
            ("T013", ""),
            ("T014", str(raw_payment.amount)),
            ("T015", ""),
            ("T016", ""),
            ("T017", ""),
            ("T018", ""),
            ("T019", ""),
            ("T020", ""),
            ("T021", ""),
            ("T022", raw_payment.sort_code),
            ("T023", ""),
            ("T024", ""),
            ("T025", ""),
            ("T026", ""),
            ("T027", ""),
            ("T028", raw_payment.account_number),
            ("T029", ""),
            ("T030", raw_payment.payee_name),
            ("T031", ""),
            ("T032", ""),
            ("T033", ""),
            ("T034", ""),
            ("T035", ""),
            ("T036", ""),
            ("T037", ""),
            ("T038", ""),
            ("T039", ""),
            ("T040", ""),
            ("T041", ""),
            ("T042", ""),
            ("T043", ""),
            ("T044", ""),
            ("T045", ""),
            ("T046", ""),
            ("T047", ""),
            ("T048", ""),
            ("T049", ""),
            ("T051", ""),
            ("T052", ""),
            ("T053", ""),
            ("T054", ""),
            ("T055", ""),
            ("T056", ""),
            ("T057", ""),
            ("T058", ""),
            ("T059", ""),
            ("T060", ""),
            ("T061", ""),
            ("T062", ""),
            ("T063", ""),
            ("T064", ""),
            ("T065", ""),
            ("T066", ""),
            ("T067", ""),
            ("T068", ""),
            ("T069", ""),
            ("T070", ""),
            ("T071", ""),
            ("T072", ""),
            ("T073", ""),
            ("T074", ""),
            ("T075", ""),
            ("T076", ""),
            ("T077", ""),
            ("T078", ""),
            ("T079", ""),
            ("T080", ""),
            ("T081", ""),
            ("T082", ""),
            ("T083", "")
        ])

    def output_payment(self):
        return self.data.values()

    def __str__(self):
        return "{0} | {1} | {2} | {3}".format(
            self.data["T014"], self.data["T022"], self.data["T028"],
            self.data["T030"])
