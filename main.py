class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list = []

    def __iter__(self):
        self.list_of_list = list(reversed(self.list_of_list))
        return self

    def __next__(self):
        if len(self.list) == 0 and len(self.list_of_list) > 0:
            self.list = self.list_of_list.pop()
            self.list = list(reversed(self.list))

        if len(self.list) == 0 and len(self.list_of_list) == 0:
            raise StopIteration

        return self.list.pop()


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
   test_1()


