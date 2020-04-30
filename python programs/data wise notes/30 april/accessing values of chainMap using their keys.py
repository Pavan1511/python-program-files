#Program: 4
# accessing values of ChainMap using their keys
from collections import ChainMap


def access_chainmap():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}

    student = ChainMap(stud, marks)
    print(student['name'])  # Arjun
    print(student['college_name'])  # msrit
    print(student['sub1'])  # 67
    print(student['sub2'])  # 61
    print(student['sub3'])  # 73


def main():
    access_chainmap()


if __name__ == "__main__":
    main()
