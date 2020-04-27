#join():
#input:abc for tech
#output:a*b*c* *f*o*r* *t*e*c*h

def check_join():
	abc='abc for tech'
	cars=['BMW','Benz','Audi','Nissan GT-R']#list
	fruits=('mangoes','apple','orange')#tuple
	names={"arjun","ram","krish"}#set
	colors={'red':'primary_color','green':'primary_color2','blue':'primary_color3'}
	#join()string
	print(abc)#abc for tech
	print('*'.join(abc)) #a*b*c* *f*o*r* *t*e*c*h
	#join with list
	print(cars)
	print('*'.join(cars))
	#join with tuple
	print(fruits)
	print(''.join(fruits))
	#join with set  - is unorder set so you will not get the output in unorder
	print(names)
	print(''.join(names))
	#join with tuple  -key will be the output that all 
	print(colors)
	print(''.join(colors))

if __name__ == "__main__":
	check_join()