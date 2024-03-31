password = 'Prakash@35'

err = "first index should not be an number "
num = 0
char = 0
caps = 0

if (password[0]>='A' and password[0]<='Z') or (password[0]>='a' and password[0]<='z'):
    err = "first char condition met........true"
    print(err)
    num ,char,caps =0,0,0
    err = ''
    for i in range(len(password)):
        if(password[i]!=' ' and password[i]!='/'):
            if ord(password[i])>=48 and ord(password[i])<=57:
                num = num+1
            elif (password[i]>='a' and password[i]<='z'):
                char = char+1
            elif (password[i]>='A' and password[i]<='Z'):
                caps = caps+1
                char = char+1
        else:
            err = "there is an space or slash in the password"
            break

if (char>=4)and(num>=1)and(caps>=1):
    err = "password met all the condition true and there is no space and slash in the password"
else:
    err = "your password contains insufficient length"

print(err)
