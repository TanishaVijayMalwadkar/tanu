a=[]
no=int(input("Enter the value of n="))
for i in range(no):
    no=int(input("enter the number"))
    a.append(no)
print(a)
kstep=int(input("enter a step to rotae"))
for i in range(len(a)):
    if i<kstep:
        a.append(a[0])
        a.pop(0)
        i=0
        if i>kstep:
            break
print(a)            