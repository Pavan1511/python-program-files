# Program: 6 __missing__(key):
# internal working of default dict
from collections import defaultdict


def internal_working_defaultdict():
    student = defaultdict(lambda: 'invalid key')  # ---> lamba is a default_factory (instance varuable)

    # adding items to my defaultdict
    student['usn'] = '1rn16scs18'
    student['name'] = 'Arjun'

    print(student['name'])  # Arjun

    # __missing__()--> is implicitly called by __getitem__ of standard dict

    print(student.__missing__('cgpa'))  # invalid key


def main():
    internal_working_defaultdict()


if __name__ == "__main__":
    main()
