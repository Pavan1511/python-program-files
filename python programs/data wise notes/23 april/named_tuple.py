#1]round brackets
#2]ordered 
#3]immutable
#problems with named tuple
def employee_info():
	emp1=(101234,'ramesh',26,'java developer',45000)
	emp2=(102235,'suresh',27,'python developer',46000)
	print(emp1)#(101234, 'ramesh', 26, 'java developer', 45000)
	print(type(emp1))#<class 'tuple'>
	
	#accessing tuple elements
	print(emp1[0])#101234
	print(emp1[4])#45000
	print(emp2[0])#102235
	print(emp2[4])#print(emp1[4])
if __name__ == '__main__':
	employee_info()