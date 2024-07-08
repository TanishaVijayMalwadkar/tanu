str1=[]
str=input("enter the string:")
print(str)
for i in range (len(str)):
    if(str[i]=='a'):
        str1.append('A') 
    elif(str[i]=='b'):
        str1.append('B')
    elif(str[i]=='c'):
        str1.append('C')
    elif(str[i]=='d'):
        str1.append('D')
    print(str1[i])                    