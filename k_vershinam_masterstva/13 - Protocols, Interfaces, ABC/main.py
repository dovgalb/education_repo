# Для реализации полного протокола, возможно, требуется написать довольно
# много методов, но зачастую достаточно реализовать только часть.

class Vowels:
    def __getitem__(self, item):
        return "AEIOU"[item]


v = Vowels()
print(v[0])

for i in v: print(i)

# Реализации метода __getitem__ достаточно для получения элементов по индексу,
# а также поддержки итерирования и оператора in. Специальный метод
# __getitem__ – ключ к протоколу последовательности.
