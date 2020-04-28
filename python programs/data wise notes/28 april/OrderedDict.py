# OrderedDict
from collections import OrderedDict


def accessing_ord_dct():  # control flow -->5

    student = OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35)])

    # accessing OrderedDict values by using their keys

    print(student['usn'])  # 1ms09cs415
    print(student['name'])  # Arjun
    print(student['cgpa'])  # 8.35


def main():
    accessing_ord_dct()


if __name__ == "__main__":
    main()
'''
Output:
1ms09cs415
Arjun
8.35
'''
