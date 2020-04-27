#input : "abc @#$34for t&$#298ech IN@DIA123"
#alphatebs -- . atoz A to Z
#output : 15

def counting_alphabets():
	data="abc @#$34for t&$#298ech IN@DIA123"
	alpha_count=0
	others_chars=0
	for ch in data:
		if ch.isalpha()==True:  #return true iff char is alphabet
			alpha_count+=1
		else:
			others_chars+=1

	print(f'no of alphabets ={alpha_count}')
	print(f'no of alphabets={others_chars}')

if __name__ == '__main__':
	counting_alphabets()