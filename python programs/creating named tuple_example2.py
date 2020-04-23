#method 2 :create namedtuple -->string of fields from collections 

from collections import namedtuple
#namedtuple indirectly uses[(split() to divide)]
def creating_namedtuple():
	Employee=namedtuple('employee',"id name age designation salary")

	#how to set valuse for this above fields
	e1=Employee(101234,'ramesh',26,'java developer',45000)
	e2=Employee(102235,'suresh',27,'python developer',46000)
	#employee 1
	print(e1)
	print(e1.id)
	print(e1.name)
	print(e1.age)
	print(e1.designation)
	print(e1.salary)
	

if __name__ == '__main__':
	creating_namedtuple()