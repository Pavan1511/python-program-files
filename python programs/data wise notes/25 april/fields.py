# _fields
from collections import namedtuple


def demo_methods():
    Employee = namedtuple('Employee', 'id name age role salary')
    e1 = Employee(101234, 'Ramesh', 26, 'Python developer', 60000)
    print(e1)

    Person = namedtuple('Person', 'phone_no location')
    p1 = Person('983762838x', 'Bengaluru')
    print(p1)

    #_fields -->list out all fields of a namedtuple
    print(e1._fields)  # ('id', 'name', 'age', 'role', 'salary')

    Employee2 = namedtuple('Employee2', Employee._fields + Person._fields)

    e2 = Employee2(201134, 'Suresh', 27, 'Java developer', 50000, '957484614x', 'Mysore')
    print(e2)


if __name__ == "__main__":
    demo_methods()
'''Output:
Employee(id=101234, name='Ramesh', age=26, role='Python developer', salary=60000)
Person(phone_no='983762838x', location='Bengaluru')
('id', 'name', 'age', 'role', 'salary')
Employee2(id=201134, name='Suresh', age=27, role='Java developer', salary=50000, phone_no='957484614x', location='Mysore')
'''
