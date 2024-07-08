vow=input("enter the string:")
cnt=0
for i in range(len(vow)):
    if(vow[i]=='a' or vow[i]=='e' or vow[i]=='i' or vow[i]=='o' or vow[i]=='u' or vow[i]=='A' or vow[i]=='E' or vow[i]=='I' or vow[i]=='O' or vow[i]=='U'):
       cnt+=1
print("Number of vowls A:",vow.count('a')+vow.count('A'))    
print("Number of vowls E:",vow.count('e')+vow.count('E'))    
print("Number of vowls I:",vow.count('i')+vow.count('I'))    
print("Number of vowls O:",vow.count('o')+vow.count('O'))    
print("Number of vowls U:",vow.count('u')+vow.count('U'))    

print("cnt is=",cnt)