def parametr_decor(c):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            print('начало выполгнения')
            res = func(*args, **kwargs) * c
            print('Конец выполгнения')
            return res
        return wrapper
    return func_decorator

@parametr_decor(2)
def hello_world(a, b):
    return a * b


if __name__ == '__main__':
    print(hello_world(2,3))