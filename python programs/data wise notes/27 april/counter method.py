# counter method
from collections import Counter


def counter_method():
    toll1 = Counter('abccbaabc')
    toll2 = Counter({'a': 3, 'b': 5, 'c': -8, 'd': 0})

    print(toll1)  # Counter({'a': 3, 'b': 3, 'c': 3})Counter({'a': 3, 'b': 3, 'c': 3})
    print(toll2)  # Counter({'b': 5, 'a': 3, 'd': 0, 'c': -8})

    # element()
    print(list(toll1.elements()))  # ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
    print(list(toll2.elements()))  # ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'b']


if __name__ == '__main__':
    counter_method()
