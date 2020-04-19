def check():
	data="Abc FoR TeCh@#$"
	res=""  #empty string from converstion to res..
	for ch in data:
		if ch.islower()==True:
			res+=ch.upper()
		elif ch.isupper()==True:
			res+=ch.lower()
		else:
			res+=ch
	print(f'original string={data}') #original string=Abc FoR TeCh@#$
	print(f'result={res}')  #result=aBC fOr tEcH@#$

if __name__ == '__main__':
	check()