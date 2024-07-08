str=[]
no=int(input("enter the string array"))
for i in range(no):
    n=int(input("enter the number"))
    str.append(n)
print(str)
for i in range (len(str)):
    for j in range(len(str)):
        if(str[i]==0):
            str.append(str[i])
            str.pop(i)
print(str)                