registry = []


def register(func):
    print(f'running register({func})')
    result = registry.append(func)
    return func


@register
def f1():
    print('running f1()')

f1()