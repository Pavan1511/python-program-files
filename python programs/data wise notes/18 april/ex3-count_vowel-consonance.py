#input:"ab@c for t#ech tech for a$bc abc"
#output:'vowel,consta'

def counting():
    data="ab@c for t#ech tech for a$bc abc"

    #setup intial value for v,c,s,w,s
    vow=conso=spcs=words=sp_chars=0
    #traverse string
    for ch in data:
        #vowels==>a,e,i,o,u
        if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
            vow+=1
        elif ch=='':
            spcs+=1
            words+=1
        elif ch=='@'or ch=='$' or ch=='#':
            sp_chars+=1
        else:
            conso+=1
    print(f'tota no of vowels:{vow}')
    print(f'tota no of consonance:{conso}')
    print(f'tota no of spcs:{spcs}')
    print(f'tota no of words:{words+1}')
    print(f'tota no of sp_chars:{sp_chars}')
    
if __name__ =="__main__":
    counting()
