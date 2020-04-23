#checking for immutability of namedtupleini
#from collections import nametuple -->specific pack
import collections
def car_info():
    CAR=collections.namedtuple('car','name brand color type')
    cars1=CAR('hexa','tata','black','petrol')
    print(cars1)
	#cars1[1]='ford'#TypeError: 'car' object does not support item assignment
	#cars1.brand='KIA'#AttributeError: can't set attribute
if __name__ == '__main__':
	car_info()
