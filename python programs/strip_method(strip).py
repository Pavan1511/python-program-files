#input : "   This world is full of opportunities     "
#output:This world is full of opportunities

def rem_lead_trail_spcs():
	data="   This world is full of opportunities     "
	stripped_data=data.strip()   #cannot take argument
	print('length of data before removing spaces ',len(data))
	print('data before stripping:',data)
	print()
	print('length of data after removing spaces ',len(stripped_data))
	print('data after stripping:',stripped_data)
if __name__ == '__main__':
	rem_lead_trail_spcs()