import random
print('\n---cutting line1---')

for i in range(1,4):
    password=random.randint(0,9999)
    print('Password is:%04d'%(password))
print('\n---cutting line2---')
nums=('0','1','2','3','4','5','6','7','8','9')
password=[]
for i in range(1,5):
    password.append(random.choice(nums))
    print('debug-Passwordlistchanging:%s'%(password))

#debug
print('debug-listofpassword=%s'%(password))
print('Password is:',end='')
for item in password:
    print('%s'%(item),end='')

print('\n\n---cutting line3---')

char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
charall=char1+char2+char3+char4
print('debug-Allusablechars:%s'%(charall))
pwdLen=8
Password=[]
for i in range(1,pwdLen):
        password.append(random.choice(charall))
        print('debug-Passwordlistchanging:%s'%(password))
print('debug-listofpassword=%s'%(password))
print('Password is:',end='')
for item in password:
    print('%s'%(item),end='')
