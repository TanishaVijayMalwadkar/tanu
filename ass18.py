str=input("enter the string")
def stringlist(str):
    for i in range(len(str)):
        cnt=str.count(str[i])
        if cnt==1:
            re=str[i]
            break
    return re
n=stringlist(str)
print("character is non repeating is:",n)       