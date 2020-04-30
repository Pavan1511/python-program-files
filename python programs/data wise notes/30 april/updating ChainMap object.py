#Program: 5
# updating ChainMap object
from collections import ChainMap


def update_chainmap():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    student = ChainMap(stud, marks)  # stud -->1st mapping and marks ---> 2nd mapping
    print("Before updating ChainMap:", student)
    student['name'] = 'Ram'
    student['sub1'] = 78
    student['sub3'] = 54
    print()
    print("After updating ChainMap:", student)


def main():
    update_chainmap()


if __name__ == "__main__":
    main()
