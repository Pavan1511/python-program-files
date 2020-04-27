# operator--->(+),(-),(*),(/)
from collections import Counter


def operation_Counter():
    a = Counter(x=6, y=5, z=1)
    b = Counter(x=2, y=3, z=0)

    # addition of two counter
    print(a + b)
    print()
    # subtraction of two counter
    print(a - b)
    print()
    # union by using |
    print(a | b)

    # intersection by &
    print(a & b)


if __name__ == '__main__':
    operation_Counter()
