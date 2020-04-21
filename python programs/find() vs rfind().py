#find() vs rfind()
def check():
	data="abc for tech abc tech for abc abc"
        # a b c   f o r   t  e c h   a b c   t e c h   f o r   a b c   a b c"
        # 0 1 2 3 4 5 6 7 8  9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3
        #			           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
	#find()-->abc
	print(data.find('tech'))#8 
	print(data.find('spider'))#-1 since spider is not there in data by default it return -1 
	print(data.find('abc',10,16))#13
	print(data.find('for',21,25))#22
	print()
	#rfind
	print(data.rfind('tech'))#17
	print(data.rfind('spider'))#-1
	print(data.rfind('abc',0,16))#13
	#a b c   f o r   t  e c h   <a(13) b(14) c> -->sinch it is rfind we will get last

if __name__ == '__main__':
	check()