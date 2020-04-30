# Program: 8 mapps attribute
from collections import ChainMap
# maps attribute


def mapping():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    # print(stud)
    # print(marks)
    student = ChainMap(stud, marks)
    # maps---> create a list of mappings

    lst = student.maps
    print(lst)


def main():
    mapping()


if __name__ == "__main__":
    main()
