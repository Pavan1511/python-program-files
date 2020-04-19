#isalnum-if we fined any whitespace or special char the output is false or else it gives true
def check_alpha_numeric():
	s1='abc'
	s2='123'
	s3='abc123'
	s4='abc 123'
	s5='abc@123'
	print(s1.isalnum())#True
	print(s2.isalnum())#True
	print(s3.isalnum())#True
	print(s4.isalnum())#False
	print(s5.isalnum())#False

if __name__ == '__main__':
	check_alpha_numeric()