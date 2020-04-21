#casefold():
def check():
	data="Abc For Tech"
	print(data)#True
	casefolded_data=data.casefold()
	print(casefolded_data)
	print(data.find("tech"))#when we use find() we get -1 but when we use index() we get valuse error
	print(casefolded_data.find("tech"))#8
if __name__ == '__main__':
	check()