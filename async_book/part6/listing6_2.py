import multiprocessing
import time
from multiprocessing import Pool


def say_hello(name: str, num: int) -> str:
    time.sleep(num)
    return f'Привет, {name}!'


if __name__ == '__main__':
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff', 3))
        hi_john = process_pool.apply_async(say_hello, args=('John', 1))
        print(f'процессы выполняются')
        print(hi_jeff.get())
        print(hi_john.get())
        print(f'процессы завершились')

