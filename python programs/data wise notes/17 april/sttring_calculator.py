def counting_upp_low_oth():
	data="This WorLd Is fULL of oPPoRtUniTieS"
	count_low=count_upp=oth_chars=0
	for ch in data:
		#lowercase a to z
		if ch >= 'a'and ch <= 'z':
			count_low+=1        # count_low = count_low + 1
		#uppercase a to z	
		elif ch>='A' and ch<='Z':
			count_upp+=1
		else:
			oth_chars+=1
	print(f'no of lowercase letters is:{count_low}')
	print(f'no of uppercase letters is:{count_upp}')
	print(f'no of othercase char is:{oth_chars}')
	a=10
	b=12
	print("a= ",a,"b= ",b)
	print(f'a={a}')
if __name__ == '__main__':
	counting_upp_low_oth()