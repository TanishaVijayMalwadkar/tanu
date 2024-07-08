list=[]
def sum():
    l=int(input("enter the list:"))
    sum=0
    for i in range(l):
        no=int(input("enter the number"))
        list.append(no)
    for i in range(len(list)):
        sum=sum+list[i]
    print("sum of result",sum)  
sum()          