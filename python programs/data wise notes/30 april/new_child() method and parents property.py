#Program: 9
# new_child() method and parents property
from collections import ChainMap


def adding_child():
    stud = {'usn': '1ms09cs415', 'name': 'Arjun', 'college_name': 'msrit'}
    marks = {'sub1': 67, 'sub2': 61, 'sub3': 73, 'sub4': 78, 'sub5': 57}
    results = {}

    # print(student)

    total = 0
    for mark in marks.values():
        total += mark

    percentage = total / 500 * 100

    results['total'] = total
    results['percent'] = percentage

    student = ChainMap(stud, marks)

    print("Before adding a child:", student)
    print()

    # new_child() ---> add a child to ChainMap object

    updated_student = student.new_child(results)

    print(updated_student)
    print()

    # listing all mappings except child mapping
    print(updated_student.parents)


def main():
    adding_child()


if __name__ == "__main__":
    main()
