#input:enter a sequence of number
#1 2 344 66 78

#output: 1,2,344,66,78

def more_join():
	lst=input('enter a sequence of number: \n').split()
	print(lst)
	print(','.join(lst))
if __name__ == '__main__':
	more_join()
