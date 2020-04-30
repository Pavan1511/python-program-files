# Program: 2 returning a default value if key is not present in defaultdict using lambda fucntion
# creating a defaultdict
from collections import defaultdict


def creating_defaultdict():
    student = defaultdict(func())
    print(type(student))
    student['usn'] = '1rn16scs18'
    student['name'] = 'Arjun'
    student['cgpa'] = 7.5
    print(student)
    print(student['name'])  # Arjun
    print(student['sem'])  # 8


def func():
    return lambda: 8


def main():
    creating_defaultdict()


if __name__ == "__main__":
    main()
