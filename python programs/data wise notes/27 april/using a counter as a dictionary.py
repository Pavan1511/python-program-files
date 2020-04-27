# using a counter as a dictionary
from collections import Counter


def using_counter_dct():
    lst = ['abc', 'for', 'tech', 'tech', 'abc', 'for', 'abc', 'tech', 'abc']
    toll = Counter(lst)
    print(toll)  # Counter({'abc': 4, 'tech': 3, 'for': 2})

    # using counter toll as a dictionary
    print(toll['abc'])
    print(toll['tech'])
    print(toll['for'])
    print(toll['python'])

    # create a dictionary
    d = {'a': 1, 'b': 2}
    print(type(d))
    print(d['a'])
    print(d['b'])
    # print(d['z'])#key Error


if __name__ == '__main__':
    using_counter_dct()
