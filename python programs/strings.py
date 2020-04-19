def performing_slicing():
	s1="java"
	s2="python"
	#to concatinate we can use + operator     
	#-1 -2 -3 -4 -5 -6 -7 -8 -9 -10
	# 0  1  2  3  4  5  6  7  8  9
	# j  a  v  a  p  y  t  h  o  n
	s3 = s1+s2
	print(s3)   #javapython
	print(s3[:4]) #java
	print(s3[4:]) #python
	print(s3[:]) #javapython
	print(s3[0:10])#javapython
	print(s3[::-2])#nhyaa
	print(s3[::-1])#nohtypavaj
	print(s3[::2])#jvpto
	print(s3[::3])   #jatn
	print(s3[4::2])#pto
	print(s3[-4::-3])#taj
if __name__ == "__main__":
	performing_slicing()
