
arr=[1,2,3,4,5,6,7,8,5,8]
print("The initialized list is:",arr)
res_list=[]
for i in arr:
    if i not in res_list:
        res_list.append(i)
print("the result list after removing duplicates is",res_list)        
