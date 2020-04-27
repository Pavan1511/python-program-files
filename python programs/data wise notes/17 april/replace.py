#input:"This is Java session"
#output:"This is Python session"

def replace_substr():
	data="This is Java session"
	res=data.replace('Java','Python')
	print("string before replacing:",data)
	print("string after replacing:",res)

if __name__=="__main__":
	replace_substr()


#input:"This is Java session"
#output:"This is Python session"

def replace_substr1():
	data="This is Java session Java"
	res=data.replace('Java','Python')
	print("string before replacing:",data)
	print("string after replacing:",res)

if __name__=="__main__":
	replace_substr1()
	