#input : "the clown ran after the car"
#output:5
def counting_spaces():
	data="the clown ran after the car"
	spcs_count=0
	other_chars=0
	for ch in data:
		if ch.isspace()==True:
			spcs_count+=1
		else:
			other_chars+=1
	print(f'total number of spaces={spcs_count}')
	print(f'total number of other chars={other_chars}')
if __name__ == '__main__':
	counting_spaces()