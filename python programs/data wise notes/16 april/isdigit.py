#input : "T1hi2s i4s p8yt9h99o5n se4ss3io0n"
#output:

def counting_digits():
	data="T1hi2s i4s p8yt9h99o5n se4ss3io0n"
	digit_count=0
	other_chars=0
	for ch in data:
		if  ch.isdigit()==True:
			digit_count+=1
		else:
			other_chars+=1
	print(f'total number of digit={digit_count}')
	print(f'total number of other chars={other_chars}')
if __name__ == '__main__':
	counting_digits()