from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        """
        Добавление товара может являться частью заказа
        """
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        """
        Вычисление цены также может являться частью заказа
        """
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Authorize(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class NotARobot(Authorize):
    authorized = False

    def not_a_robot(self):
        print(f"Are you a robot? naaaaaaaaaa")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class SMSAuth(Authorize):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class CreditPaymentPay(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order: Order):
        print('Processing credit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class DebitPaymentPay(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorize):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class PayPallPay(PaymentProcessor):
    def __init__(self, email, authorizer: Authorize):
        self.email = email
        self.authorizer = authorizer

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print('Processing PayPall payment type')
        print(f'Verifying email address: {self.email}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())

authorizer = NotARobot()


processor = DebitPaymentPay('123321', authorizer)
authorizer.not_a_robot()
processor.pay(order)
