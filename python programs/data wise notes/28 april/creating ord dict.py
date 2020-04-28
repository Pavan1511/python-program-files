# creating ord dict
# OrderedDict
from collections import OrderedDict  # control flow -->1
# control flow -->2


def creating_ord_dct():  # control flow -->5
 # approach 1
    student = OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35)])
 # print(type(student))
 # print(student)
 # approach 2
    employee = OrderedDict()  # empty OrderedDict
    employee['id'] = 101234
    employee['name'] = 'Krish'
    employee['salary'] = 35000
    return student, employee
# control flow -->2


def main():  # control flow -->4
    stud, emp = creating_ord_dct()  # control flow -->6
    print(stud)
    print(type(stud))
    print()
    print(emp)
    print(type(emp))


# control flow -->3
if __name__ == "__main__":
    main()  # control flow -->7
# control flow -->8 ---> os

'''
Output:
<class 'collections.OrderedDict'>
OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35)])
OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35)])
<class 'collections.OrderedDict'>

OrderedDict([('id', 101234), ('name', 'Krish'), ('salary', 35000)])
<class 'collections.OrderedDict'>


'''
