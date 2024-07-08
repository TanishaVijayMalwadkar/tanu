list=["flower","fly","flour"]
temp=len(list[0])
for i in range(len(list)):
    if(len(list[i])<temp):
        temp=len(list[i])
    while(temp>0 and list[0][0:temp]!=list[i][0:temp]):
        temp=temp-1
print(list[0][0:temp])        
            