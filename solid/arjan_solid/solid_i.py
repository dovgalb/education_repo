"""
Принцип разделения интерфейсов. Гласит, что в целом будет лучше, если у нас будет несколько специфических интерфейсов,
а не один интерфейс общего назначнеия
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


class SMSAuth:
    authorized = False

    def verify_code(self, code):
        print(f'Verifying code {code}')
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):
    # Мы расширили этот пример - таким образом существует отправленное смс-сообщение,
    # в котором существует код для авторизации платежа.
    # по сути мы усложнили это класс, и нам не везде нужно реализовывать оба метода

    # @abstractmethod
    # def auth_sms(self, code):
    # """так как у накс есть тепрь дочерний класс, с реализацией этого метода, здесь он больше не нужен"""
    #     ...

    @abstractmethod
    def pay(self, order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuth):
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

    # система обработки кредитных платежей  не имеет двухфакторной аутентификации, но обязана реализовывать этот класс
    # def auth_sms(self, code):
    #     raise Exception('Credit card payments dont support SMS code authorization.')

    def pay(self, order):
        print('Processing credit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class PayPallPaymentProcessor(PaymentProcessor):
    """Проблема заключается в том, что PayPall должен работать не с кодами безопасности,
    а с адресами электронной почты, поэтому мы уберем в абстрактном методе атрибут verify_code и будем добьавлять его в
    инициализаторе каждого класса оплаты, в зависимости от наших потребностей(код, email, и  т.д.)"""

    def __init__(self, email_address, authorizer: SMSAuth):
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
authorizer = SMSAuth()
processor = DebitPaymentProcessor('21312', authorizer)
authorizer.verify_code("21312")
processor.pay(order)