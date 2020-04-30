# default dict
from collections import defaultdict


def creating_defaultdict():
    student = defaultdict(main)
    print(type(student))

    student['usn'] = '1rn16cs18'
    student['name'] = 'arjun'
    student['cgpa'] = 7.5

    print(student)

    print(student['name'])
    print(student['sem'])


def main():
    creating_defaultdict()


if __name__ == '__main__':
    main()
