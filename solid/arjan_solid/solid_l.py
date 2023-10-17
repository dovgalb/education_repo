"""
Принцип подстановки Барбары-Лисков. Говорит, что если у нас в программе есть объекты, то
мы должны заменить эти объекты экземплярами подтипов или подклассов без изменения корректности работы программы
"""

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):

        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing credit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class PayPallPaymentProcessor(PaymentProcessor):
    """Проблема заключается в том, что PayPall должен работать не с кодами безопасности,
    а с адресами электронной почты, поэтому мы уберем в абстрактном методе атрибут verify_code и будем добьавлять его в
    инициализаторе каждого класса оплаты, в зависимости от наших потребностей(код, email, и  т.д.)"""

    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print('Processing PayPall payment type')
        print(f'Verifying email address: {self.email_address}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = PayPallPaymentProcessor('email@example.com')
processor.pay(order)
