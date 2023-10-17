"""
Принцип единой ответственности - классы и методы обладают высокой
связностью и отвечают только за одну вещь, это гарантирует что в
дальнейшем их будет удобно использовать повторно
"""

from abc import ABC, abstractmethod


class Order:
    """У класса заказы слишком много обязанностей,
    и мы должны это исправить
    """
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

    # def pay(self, payment_type, security_code):
    #     """
    #     Обработка точно не должна быть частью заказа.
    #     Следует выделить его в отдельный класс, если в будущем мы захотим добавить
    #     другие типы платежей, нам больше не придется менять класс заказа,
    #     мы сможем сделать это в обработке платежей
    #     """
    #     if payment_type == 'debit':
    #         print('Processing debit payment type')
    #         print(f'Verifying security code: {security_code}')
    #         self.status = 'paid'
    #
    #     elif payment_type == 'credit':
    #         print('Processing credit payment type')
    #         print(f'Verifying security code: {security_code}')
    #         self.status = 'paid'
    #
    #     else:
    #         raise Exception('Неизвестный тип оплаты')


class PaymentProcessor:
    """Теперь у нас 2 разных метода"""
    def pay_credit(self, security_code, order):
        print('Processing credit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

    def pay_debit(self, security_code, order):
        print('Processing debit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_credit('1212', order)

# Теперь у заказа и обработчика платежей по одной своей ответственности.
# Ответственность за заказ лежит на одном классе, а ответственность за обработку платежей лежит на другом
