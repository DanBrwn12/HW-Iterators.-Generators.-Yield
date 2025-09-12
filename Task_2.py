import types


def flat_generator(list_of_lists):
    cursor_outer = 0
    cursor_inner = 0
    while cursor_outer < len(list_of_lists):
        current_list = list_of_lists[cursor_outer]
        if cursor_inner < len(current_list):
            yield current_list[cursor_inner]
            cursor_inner += 1
        else:
            cursor_inner = 0
            cursor_outer += 1
            continue



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
