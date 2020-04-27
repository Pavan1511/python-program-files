# _make
from collections import namedtuple


def student_info():
    Student = namedtuple('Student', ['usn', 'name', 'college'])
    #s = Student('1ms09cs416', 'Arun', 'msrit')
    # print(s)
    #_make()

    lst = ['1ms09cs417', 'Gautham', 'msrit']
    s1 = Student._make(lst)
    print(s1)


if __name__ == "__main__":
    student_info()
    '''
Output:
Student(usn='1ms09cs417', name='Gautham', college='msrit') '''
