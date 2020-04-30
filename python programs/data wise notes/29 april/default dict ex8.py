#Program: 8 using int as a default_factory function
# use of int function in defaultdict
from collections import defaultdict


def int_defaultdict():
    count_chars = defaultdict(int)

    data = 'abccbacabb'

    for ch in data:
        count_chars[ch] += 1

    print(count_chars)  # {'a':3,'b':4,'c':3}


def main():
    int_defaultdict()


if __name__ == "__main__":
    main()

'''
ch ---> a = 0, 1,2,3
ch---> b = 0 ,1,2,3,4
ch ---> c = 0,1,2,3
'''
