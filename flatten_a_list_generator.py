# https://py.checkio.org/en/mission/flatten-a-list-generator-version/
from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    for element in array:
        if isinstance(element, list):
            for ele in flat_list(element):
                yield ele
        else:
            yield element


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
