from functools import partial

nums = [1,4,5,10,40]
def count(num):
    count = 0
    while num > count:
        count += 1
        print(count)



partials = [partial(count, num)() for num in nums]


