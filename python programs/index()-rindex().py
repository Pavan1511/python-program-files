#index and rindex()
# a b c   f o r   t  e c h   a b c   t e c h   f o r   a b c   a b c"
        # 0 1 2 3 4 5 6 7 8  9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3
        #			           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2

def check():
	data="abc for tech abc tech for abc abc"
	#index()
	print(data.index('abc'))#0
	#print(data.index('spider'))#error since the spider is not present my given string so it will rise value error
	#ValueError: substring not found
	print(data.index('abc',3,16))#13

	#rindex()
	print(data.rindex('abc'))#30
	#print(data.rindex('spider'))#error since the spider is not present my given string so it will rise value error
	#ValueError: substring not found
	print(data.rindex('abc',0,29))#26
	
if __name__ == '__main__':
	check()