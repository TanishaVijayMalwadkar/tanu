a=int(input("Enter the value of  n is:"))
c=[]
for i in range (a):
    no=int(input("enter the number"))
    c.append(no)
lar=0    
for i in range (len(c)):
    j=i+1
    for j in range(len(c)-1):
        mul=c[i]*c[j]
        if mul>lar:
            lar=mul
print("Maximum product of array is:",lar)   