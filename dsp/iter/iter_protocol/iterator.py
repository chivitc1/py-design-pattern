class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


def test_iter():
    iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
    iterator = iter(iterable)
    while True:
        try:
            cap_word = next(iterator)
            print(cap_word)
        except StopIteration:
            break


def test_traditional_iter():
    iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
    for i in iterable:
        print(i)


if __name__ == '__main__':
    test_iter()
    # test_traditional_iter()