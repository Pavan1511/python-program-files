# most_common(n)
from collections import Counter


def counter_methods():
    toll = Counter('abccbacabcabccbd')
    print(toll)

    # most_common(n)
    print(toll.most_common(1))  # [('c', 6)]
    print(toll.most_common())


if __name__ == '__main__':
    counter_methods()
