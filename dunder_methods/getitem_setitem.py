class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами нашей коллекции ')

    def __setitem__(self, key, value):
        self.values[key] = value
        return self.values[key]

    def __delitem__(self, key):
        del self.values[key]


v1 = Vector(1, 2, 3, 4)
print(v1[3])
