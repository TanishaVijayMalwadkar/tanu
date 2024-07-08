n=int(input("enter the 1 to n numbers:"))
a=[]
print("enter the number from 1 to n=",n)
for i in range(n):
    no=int(input("number is="))
    a.append(no)
    a.sort()
print(a)
missing_no=1
for i in range(len(a)-1):
    if(a[i]!=missing_no):
        print(missing_no,"is missing")
        missing_no+=1
    missing_no+=1        