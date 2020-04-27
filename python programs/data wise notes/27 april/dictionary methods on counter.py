# dictionary methods on counter
from collections import Counter


def dtc_methods_counter():
    a = Counter(a=6, b=4, c=8)
    b = Counter(a=0, b=1, c=3)

    # update on counter
    print('Counter a:', a)
    print('Counter b:', b)
    b.update(a)
    print('Counter b:', b)

    # clear()-->remsoves all elements from a counter
    b.clear()
    print('Counter b:', b)

    # key()
    print(a.keys())
    print(a.values())
   # print(a.item())


if __name__ == '__main__':
    dtc_methods_counter()
