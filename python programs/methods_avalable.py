#method 
#1]islower-this method returns True if the character is a lowercase letter otherwise it will return False
#2]isupper-this method returns True if the character is a uppercase letter otherwise it will return False
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
#13]endswith()-this method return True if the string ends with a particular substring otherwise it will return False
#14]isalnum()-is alpha numeric
    '''   return true if 
       case 1:both alphabet and number
       case 2:only alphabet
       case 3:ony number

       return false if 
       case 1:contains space
       case 2:contains special char -@#$% 
   '''
#15]join():*)this method is used to join element of an iterable with a certain character separting the each of an iterable
     #     *)iterable -->string,tuple,set,list
     '''
 step1]dividing the problem
     2]analyse input data
     3]analyse output 
     4]remove the spaces in the given string 
        abcfortechtechforabc
     5]convert string data into list 
     	lst=list(new string)
     	lst-->[a,b,c,.....]
     6]find the length of lst
     	size=len(lst)
     7]traverse lst
     	for i in lst(range of size):-->0,1,2,...size-1 -->lst[i]
     	for j in lst(range of i+1,size):-->1,2,3,....size-1-->lst[j]
     8]lst[i]>lst[j]
     9]swap lst[i] with lst[j] and lst[j]with lst[i]
     10]convert from lst[i]
     '''
