#Program: 1
# create a ChainMap
from collections import ChainMap

#import collections


def connecting_multi_dict():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    # print(stud)
    # print(marks)
    student = ChainMap(stud, marks)

    print(student)
    print(type(student))


def main():
    connecting_multi_dict()


if __name__ == "__main__":
    main()
