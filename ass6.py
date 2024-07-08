str=input("enter the string:")
def stringis(a):
    b=[]
    c=[]
    for i in range(len(a)):
        b.append(a[i])
    c=b.copy()
    c.reverse()        
    if(b==c):
        print("palindrome")
    else:
        print("not palindrome")     
stringis(str)           


    