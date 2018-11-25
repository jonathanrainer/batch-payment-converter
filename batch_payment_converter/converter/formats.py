from abc import ABC, abstractmethod


class Format(ABC):

    @abstractmethod
    def name(self):
        return

    @abstractmethod
    def mapping(self):
        return


class InputFormat(Format):
    pass


class XeroFormat(InputFormat):

    name = "Xero"
    mapping = {
        "Amount": (0, lambda x:x),
        "Sort Code": (1, lambda x: x[0:6] if len(x) == 14 else "XXXXXX"),
        "Account Number": (1, lambda x: x[6:] if len(x) == 14 else "XXXXXXXX"),
        "Payee":  (2, lambda x:x),
        "Description": (3, lambda x:x),
        "Narrative": (4, lambda x:x)
    }

