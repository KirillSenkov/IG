class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list = []

    def is_there_lists(self, list):
        for item in list:
            if type(item) is type([]):
                return True
        return False

    def unite_list(self, list):
        whole_list = []
        # while self.is_there_lists(list) == True:
        #     for item in list:
        #         whole_list += item
        # return whole_list
        for item in list:
            if type(item) is type([]):
                while len(item) > 0:
                    whole_list += item.pop()
            else:
                whole_list.append(item)
        return whole_list

    def __iter__(self):
        self.list = self.unite_list(self.list_of_list)
        # self.list_of_list = list(reversed(self.list_of_list))
        # while len(self.list_of_list) > 0:
        #     self.list += self.list_of_list.pop()
        #     print(self.list)

        return self

    # def aggregate_lst(self.list_of_list):
    #     while len(self.list_of_list) > 0:
    #         self.list += self.list_of_list.pop()
    #     print(self.list)

    def __next__(self):
        if len(self.list) > 0:
            return self.list.pop()

        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None,
                                                   '!']


if __name__ == '__main__':
    #test_3()

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    #
    var = list(FlatIterator(list_of_lists_2))
    print(dir(var))


