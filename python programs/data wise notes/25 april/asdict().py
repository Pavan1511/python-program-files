# _asdict()
from collections import namedtuple


def method_namedtuple():
    Animal = namedtuple('Animal', 'name no_legs color type')
    a = Animal('Elephant', 4, 'grey', 'veg')
    # print(a)

    #_asdict()

    dct = a._asdict()
    print(f'namedtuple:{a}')  # namedtuple
    print(f'dictionary:{dct}')  # dictionary


if __name__ == "__main__":
    method_namedtuple()
    '''
Output:
namedtuple:Animal(name='Elephant', no_legs=4, color='grey', type='veg')
dictionary:{'name': 'Elephant', 'no_legs': 4, 'color': 'grey', 'type': 'veg'}
'''
