l=int(input("Enter the number of list:"))
array=[]
def avg():
    sum=0
    avg1=0
    for i in range (l):
         no=int(input("enter the number:"))
         array.append(no)
    for i in range (len(array)): 
        sum=sum+array[i]   
        avg1=sum/l
    print("avg is",avg1)        
avg()         