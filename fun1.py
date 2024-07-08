def add(x,y):
    return x+y
a=int(input("ENTER THE A VALUE"))
b=int(input("ENTER THE B VALUE"))
c=int(input("ENTER THE C VALUE"))
d=int(input("ENTER THE D VALUE"))
e=add(a,b)
f=add(c,d)
print("ADD a+b",e)
print("ADD c+d",f)
print("ADD a+b+c+d",add(e,f))