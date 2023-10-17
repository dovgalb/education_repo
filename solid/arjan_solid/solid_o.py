"""
Принцип открытости - закрытости.
Предполагает, что код открыт для расширений, но закрыт для изменений
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


# class PaymentProcessor:
#     """Такой код не позворляет добавить новые типы заказов без изменения кода этого класса"""
#     def pay_credit(self, security_code, order):
#         print('Processing credit payment type')
#         print(f'Verifying security code: {security_code}')
#         order.status = 'paid'
#
#     def pay_debit(self, security_code, order):
#         print('Processing debit payment type')
#         print(f'Verifying security code: {security_code}')
#         order.status = 'paid'

class PaymentProcessor(ABC):
    """
    Мы создали абстрактный класс с одним абстрактным методом, теперь
    мы можем добавлять новые типы оплаты наследуясь от этого класса
    """
    @abstractmethod
    def pay(self, order, security_code):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing debit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
# Теперь у нас 2 разных класса для двух разных типов оплаты, наследуемых от одного абстрактного класса,
# и мы можем создать множество таких способов оплаты


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing credit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
# Теперь у нас 2 разных класса для двух разных типов оплаты, наследуемых от одного абстрактного класса,
# и мы можем создать множество таких


class PayPallPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing PayPall payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = PayPallPaymentProcessor()
processor.pay(order, '1232')
