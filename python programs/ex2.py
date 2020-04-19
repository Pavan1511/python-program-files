#input:"abc for tech tech for abc"
#output:'aabbcccceeffhhoorrtt'
def sorting_string():
	data="abc for tech tech for abc"
	new_data=''
	for ch in data:
		if ch!='':
			new_data+=ch
	print(data)
	print(new_data)
	lst=list(new_data)
	size=len(lst)
	for i in range(size):
		for j in range(i+1,size):
			if lst[i]>lst[j]:
				lst[i],lst[j]=lst[j],lst[i]
		print(lst)
	print(''.join(lst))  #aabbcccceeffhhoorrtt

if __name__ == '__main__':
	sorting_string()