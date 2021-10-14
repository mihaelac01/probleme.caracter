l='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
l1=''
l2=l
l3=l
for i in l:
    x=chr(ord(i)+1)
    l1+=x
    y=l1.replace('!',' ')
    n=y.replace('[','A')
print('sirul intai:',n)
for i in l2:
    k=l2.replace(('Z'), ('A'))
print('sirul al doilea:', k) 
for i in l3:
    m=l3.replace((' '),('-'))
print('sirul al treilea:', m)