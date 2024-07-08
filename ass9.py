str=input("enter the string")
def frequency(str):
    for i in str:
        f=str.count(i)
        print(i,f)
frequency(str)        
    