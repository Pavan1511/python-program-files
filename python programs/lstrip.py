#input : "   This world is full of opportunities     "
#output:"This world is full of opportunities    "

def remove_lead_spsc():
	data="   This world is full of opportunities     "
	stripped_data=data.lstrip()
	print('data before removing spaces:',data,sep='')
	size=len(data)
	print('length of data before removing spaces:',size,sep='')
	size2=len(stripped_data)
	print('data after removing spaces:',stripped_data,sep='')
	print('length of stripped data after removing spaces:',size2,sep='')#40



if __name__ == "__main__":
	remove_lead_spsc()