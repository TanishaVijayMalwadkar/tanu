str=input("enter the string:")
lcnt=0
ucnt=0
dcnt=0
scnt=0
for i in range (len(str)):
    if('a'<=str[i] and 'z'>=str[i]):
        lcnt+=1
    elif('A'<=str[i] and 'Z'>=str[i]):
         ucnt+=1
    elif('0'<=str[i] and '9'>=str[i]):
        dcnt+=1
    else:
        scnt+=1
if(lcnt!=0 or ucnt!=0 or dcnt!=0 or scnt!=0 and len(str)>=8):
    print("valid password")
else:
    print("invalid password")                        