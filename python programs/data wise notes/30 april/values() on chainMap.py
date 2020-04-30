#Program: 3
# values() on ChainMap


from collections import ChainMap

#import collections


def access_chainmap():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    student = ChainMap(stud, marks)

    # values()---> list all values starting values from marks followed by values of stud
    print('values of student ChainMap object:', list(student.values()))


def main():
    access_chainmap()


if __name__ == "__main__":
    main()
