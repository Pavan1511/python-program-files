#Program: 2
# Access operations on ChainMap object
# keys()

from collections import ChainMap

#import collections


def access_chainmap():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    student = ChainMap(stud, marks)

    # keys() ---> list out all keys and first it will keys of marks followed by keys from stud
    print('All keys of student ChainMap object ', list(student.keys()))


def main():
    access_chainmap()


if __name__ == "__main__":
    main()
