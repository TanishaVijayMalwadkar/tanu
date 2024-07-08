mystr=input("enter the string is:")
def rev(str):
    s=""
    for i in str:
        s=i+s
    return s    

print("given string:",mystr)
print("reverse sring:",rev(mystr))
