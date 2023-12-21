class X:
    def __init__(self,a):
        self.a = a

    def update_v(self, new):
        self.a = new
        print('Параметр был обновлен')

    def print_data(self) -> None:
        print(self.a, '- хуйня X')


class Y:
    def __init__(self,a):
        self.a = a

    def update_v(self, new):
        self.a = new
        print('Параметр был обновлен')

    def print_data(self) -> None:
        print(self.a, '- хуйня Y')


def my_func(param: X, update_value: int) -> str:
    param.update_v(update_value)
    param.print_data()


if __name__ == '__main__':
    x = X(1)
    y = Y(1)

    my_func(y, 5)


    def div(x: int, y: int):
        return x / y


    print(div(2, 3))
    print(div("str1", "str2"))
