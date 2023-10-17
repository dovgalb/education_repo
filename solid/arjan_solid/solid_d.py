"""
Принцип инверсии зависимостей, означает, что мы хотим, чтобы наши классы зависели от абстрактных типов, а не от конкретных типов
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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f'Verifying code {code}')
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class IAmNotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print(f'Are you a robot?')
        self.authorized = True

    def is_authorized(self):
        return self.authorized

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
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
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print('Processing PayPall payment type')
        print(f'Verifying email address: {self.email_address}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
authorizer = IAmNotARobot()
processor = DebitPaymentProcessor('21312', authorizer)
authorizer.not_a_robot()
processor.pay(order)