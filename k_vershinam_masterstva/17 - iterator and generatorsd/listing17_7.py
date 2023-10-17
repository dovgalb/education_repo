def gen_AB():
    print('start')
    print('start1')
    yield 'A'
    print('continue')
    yield 'b'
    print('end')


for c in gen_AB():
    print('-->', c)
