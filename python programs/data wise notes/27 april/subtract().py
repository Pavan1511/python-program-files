# subtract()
from collections import Counter


def counter_method():
    a = Counter(a=5, b=8, c=10)
    b = Counter({'a': 2, 'b': 4, 'c': 8})
    c = Counter([1, 2, 3])
    d = Counter([3, 2, 1, 1, 2, 3])

    # subtract()
    print(a)  # Counter({'c': 10, 'b': 8, 'a': 5})
    print()
    print(b)  # Counter({'c': 8, 'b': 4, 'a': 2})

    # subtract()  a-b
    a.subtract(b)
    print(a)  # Counter({'b': 4, 'a': 3, 'c': 2})
    # subtract()  d-c
    print(c)  # Counter({1: 1, 2: 1, 3: 1})
    print(d)  # Counter({3: 2, 2: 2, 1: 2})
    d.subtract(c)
    print(d)


if __name__ == '__main__':
    counter_method()
