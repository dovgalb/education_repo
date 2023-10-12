from dataclasses import dataclass


@dataclass
class BankAccount:
    name: str
    _balance: (int, float)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError
        self._balance = value



a = BankAccount("таня", 300)
a.balance


