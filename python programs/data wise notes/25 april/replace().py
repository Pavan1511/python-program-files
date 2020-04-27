# _replace()
from collections import namedtuple


def demo_methods():
    CAR = namedtuple('CAR', 'name color price variant')
    c1 = CAR('Seltos', 'Red', 1200000, 'diesel')
    print(c1)
    print(id(c1))

    #_replace()
    new_namedtuple = c1._replace(color='Balck', variant='petrol')
    print(new_namedtuple)
    print(id(new_namedtuple))


if __name__ == "__main__":
    demo_methods()
'''
Output:
CAR(name='Seltos', color='Red', price=1200000, variant='diesel')
60783864
CAR(name='Seltos', color='Balck', price=1200000, variant='petrol')
60783944
'''
