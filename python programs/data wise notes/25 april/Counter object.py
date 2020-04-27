# Counter object

from collections import Counter


def counter_object_demo():
    lst = ['a', 'b', 'c', 'c', 'b', 'c', 'a', 'b', 'c']
    tupl = (1, 2, 3, 4, 2, 3, 4, 1, 5, 1, 1)
    set_ele = {10, 20, 10, 20, 30, 30, 10}  # ---> {10,20,30}
    dct = {'a': 2, 'b': 5, 'c': 8}
    data = 'abc for tech abc'

    toll_lst = Counter(lst)
    print(toll_lst)  # Counter({'c':4,'b':3,'a':2})
    print()

    toll_tupl = Counter(tupl)
    print(toll_tupl)  # counter({1:4,2:2,3:2,4:2,5:1})
    print()

    toll_set = Counter(set_ele)
    print(toll_set)  # Counter({10:1,20:1,30:1})
    print()

    toll_dct1 = Counter(dct)
    print(toll_dct1)  # Counter({'c':8,'b':5,'a':2})
    toll_dct2 = Counter(a=2, b=5, c=8)
    print(toll_dct2)  # Counter({'c':8,'b':5,'a':2})
    print()

    toll_data = Counter(data)
    print(toll_data)


if __name__ == "__main__":
    counter_object_demo()
'''
Output:
Counter({'c': 4, 'b': 3, 'a': 2})

Counter({1: 4, 2: 2, 3: 2, 4: 2, 5: 1})

Counter({10: 1, 20: 1, 30: 1})

Counter({'c': 8, 'b': 5, 'a': 2})
Counter({'c': 8, 'b': 5, 'a': 2})

Counter({'c': 3, ' ': 3, 'a': 2, 'b': 2, 'f': 1, 'o': 1, 'r': 1, 't': 1, 'e': 1, 'h': 1})
'''
