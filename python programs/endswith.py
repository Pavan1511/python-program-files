#input:"This is python session"
#       "T h i s   i s   p y   t h   o  n    s   e s  s   i  o  n "
#		 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
def searching_startswith():
	s="This is python session"
	res1=s.endswith('This')
	print(res1)
	res2=s.endswith('session')
	print(res2)
	res3=s.endswith('session',15,21)
	print(res3)

if __name__ == '__main__':
	searching_startswith()