class Spam:
    def __getitem__(self, item):
        print('->', item)
        raise IndexError


class GooseSpam:
    def __iter__(self):
        pass

    def __getitem__(self, item):
        print('->', item)
        raise IndexError