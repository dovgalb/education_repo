
class Generator:
    def __init__(self, sentence):
        self.sentence = sentence

    def generate(self):
        for i in self.sentence:
            yield i


a = Generator('hello world')

for item in a.generate():
    print(item)