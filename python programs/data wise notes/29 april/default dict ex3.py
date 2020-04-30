#Program: 3 returning a default value if key is not present in defaultdict
# creating a defaultdict
# control flow --> 1
from collections import defaultdict

# control flow --> 5


def creating_defaultdict():
    student = defaultdict(func)  # ----> invoke func() ---> 8
    print(type(student))
    student['usn'] = '1rn16scs18'
    student['name'] = 'Arjun'
    student['cgpa'] = 7.5
    print(student)
    print(student['name'])  # Arjun
    print(student['sem'])  # 8 ##control flow --> 7

# control flow --> 6


def func():
    return 8
# control flow --> 4


def main():
    creating_defaultdict()  # control flow --> 8


# control flow --> 2
if __name__ == "__main__":
    main()  # control flow --> 3
    # control flow --> 9
# control flow --> 10 ---os
