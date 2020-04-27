#zfill()
def check():
	data1="abc"
	data2="abc for"
	data3="abc for tech"
	data4=""
	print(data1.zfill(15))#000000000000abc
	print(data2.zfill(20))#0000000000000abc for
	print(data3.zfill(18))#000000abc for tech
	print(data4.zfill(18))#000000000000000000
if __name__ == '__main__':
	check()