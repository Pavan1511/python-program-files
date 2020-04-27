# field defaults
from collections import namedtuple


def method_namedtuple():
    Animal = namedtuple('Animal', 'name no_legs color type tail', defaults=[1])
    #a = Animal('Cheetha', 4, 'dottedyellow', 'nonveg')
    # print(a)
    #a = Animal()#
    #_field_defaults
    #dct = a._field_defaults
    # print(dct)

    a = Animal('Cheetha', 4, 'dottedyellow', "nonveg")
    print(a)
    print(a._field_defaults)


if __name__ == "__main__":
    method_namedtuple()
    '''
Output:
Animal(name='Cheetha', no_legs=4, color='dottedyellow', type='nonveg', tail=1)
{'tail': 1}
'''
