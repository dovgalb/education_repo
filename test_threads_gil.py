
def decor(func):
    def wrapper(*args, **kwargs):
        print('begin')
        res = func()
        print('end')
    return wrapper

@decor
def a():
    print('running')

a()