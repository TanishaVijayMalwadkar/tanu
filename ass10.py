array1=[1,3,5,7]
array2=[2,4,6,8]
i=0
j=0
sorted=[]
while(i<len(array1) and j<len(array2)):
    if(array1[i]<=array2[j]):
        sorted.append(array1[i])
        i+=1
    else:
        sorted.append(array2[j])
        j+=1
print("first sort=",array1) 
print("second sort=",array2)
print("merger=",sorted)           