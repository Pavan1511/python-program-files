
#ch--T,h,i,s, W,o,r,L,d I,s f,U,L,L o,f o,P,P,o,R,t,U,n,i,T,i,e,S
#control 1 from os 1
def counting_upp_low_oth():  #fucntion defination will be called #control 4
	data="This WorLd Is fULL of oPPoRtUniTieS"
	
	count_low=count_upp=oth_chars=0  #intilization of variables

	for ch in data:    #control 5 ch will be iterated --#ch--T,h,i,s, W,o,r,L,d I,s f,U,L,L o,f o,P,P,o,R,t,U,n,i,T,i,e,S--
		#lowercase a to z
		if ch.islower() == True: #if ch is lower true -- true==true
			count_low+=1        # count_low = count_low + 1
		#uppercase a to z	
		elif ch.isupper() == True: #if ch is upper true -- true == true   #this will be excuted when if statement is false
			count_upp+=1
		else:
			oth_chars+=1
	print(f'no of lowercase letters is:{count_low}')
	print(f'no of uppercase letters is:{count_upp}')
	print(f'no of othercase char is:{oth_chars}')
#control 2	
if __name__ == '__main__':    #__main__=="__main__"   #this line is not requiired to write but this is industries stand for writing
	#control 3
	counting_upp_low_oth()

#method 
#1]islower
#2]isupper
#3]upper()- lower to upper case
#4]lower()- upper to lower case
#5]isalpha()- if ch is either lower upper==> true otherwise==>false return true when char is alphabet
#6]isspace()- return true when char is space
#7]isdigit()- return true when char is digit from 0 to 9
#8]strip()-remove white spaces at leading(beggining) and traling(end)
#9]lstrip()-remove white spaces at leading(beggining) white spaces of string
#10]rstrip()-remove white spaces at traling(end) white spaces of string
#11]replace()-this method is used to replace a particular substring in given string
 		     #*]takes 2 argumentas  

#12]startswith()-this method return True if the string starts with a particular substring otherwise it will return False