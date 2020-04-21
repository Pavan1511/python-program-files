#count()
def check():
	data="abc for tech abc tech for abc abc"
	print(data.count('abc'))#4
	print(data.count('tech'))#2
	print(data.count('for',0,21))#1 this is number of occurance of word for--that is 1
	print(data.count('for',0,29))#2 this is number of occurance of word for--that is 1
	print(data.count('spider'))#0 is not present in substring


if __name__ == '__main__':
	check()