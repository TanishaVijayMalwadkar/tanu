import csv
def ADD_MAINTENANCE():
    c_id=input("ENTER THE CAR ID IS")
    Car_ID.append(c_id)
    c_Make=input("ENTER THE CAR MAKE IS")
    Make.append(c_Make)
    c_model=input("ENTER THE CAR MODEL IS")
    MODEL.append(c_model)
    c_year=input("ENTER THE CAR YEAR IS")
    YEAR.append(c_year)
    c_ServiceDate=input("ENTER THE CAR SERVICE DATE IS")
    SERVICE_DATE.append(c_ServiceDate)
    c_description=input("ENTER THE CAR DESCRIPTION IS")
    Description.append(c_description)
    c_cost=input("ENTER THE CAR COST IS")
    Cost.append(c_cost)
    c_service=input("ENTER THE SERVICES")
    service.append(c_service)
    
    
    with open('car1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(Car_ID)): 
           writer.writerows((Car_ID[i],"\t",Make[i],"\t",MODEL[i],"\t",YEAR[i],"\t",SERVICE_DATE[i],"\t",Description[i],"\t",Cost[i],"\t",service[i]))
        
def VIEW_LIST():
    m_total=0
    num_ser=0
    print("c_id \t  c_make \t c_model \t c_year \t c_servicedate \t c_description \t c_cost \t c_service")
    for i in range(len(Car_ID)):
        print(Car_ID[i],"\t",Make[i],"\t",MODEL[i],"\t",YEAR[i],"\t",SERVICE_DATE[i],"\t\t\t",Description[i],"\t\t\t",Cost[i],"\t",service[i])
    
    for i in range(len(Cost)):
        m_total+=Cost[i]
    print("TOTAL MAINTENANCE IS=",m_total)
    
    for i in range(len(Cost)):
        m_total+=Cost[i]
        num_ser+=1
        avg=Cost[i]/service[i]
    print("AVERAGE IS=",avg)    

def Update():
   fcar_id=input("ENter The Car is Updated")
   for i in range(len(Car_ID)):
       if(Car_ID[i]==fcar_id):
           ucar=input("CAR ID IS UPDATED")
           umake=input("CAR MAKE IS UPDATED")
           UMODEL=input("CAR MODEL IS UPDATED") 
           UYEAR=input("CAR YEAR IS UPDATED")
           USERVICE_DATE=input("CAR SERVICE DATE IS UPDATED")
           UDescription=input("CAR DESCRIPTION IS UPDATED")
           UCost=input("CAR COST IS UPDATED")
           Car_ID[i]=ucar
           Make[i]=umake
           MODEL[i]=UMODEL
           YEAR[i]=UYEAR
           SERVICE_DATE[i]=USERVICE_DATE
           Description[i]=UDescription
           Cost[i]=UCost
           with open('car1.csv', mode='w', newline='') as file:
               writer=csv.writer(file)
               for i in range(len(Car_ID)):
                   writer.writerow(("\t",Car_ID[i],"\t",Make[i],"\t",MODEL[i],"\t",YEAR[i],"\t",SERVICE_DATE[i],"\t\t\t",Description[i],"\t\t\t",Cost[i],"\t",service[i]))
       
def delete():
    dcarid=input("ENTER THE DELETE THE CAR ID IS=")   
    for i in range(len(Car_ID)):    
        if(Car_ID[i]==dcarid):
            Car_ID.remove(Car_ID[i])
            MODEL.remove(MODEL[i])
            YEAR.remove(YEAR[i])
            SERVICE_DATE.remove(SERVICE_DATE[i])
            Description.remove(Description[i])
            Cost.remove(Cost[i])
            with open('car1.csv', mode='w', newline='') as file:
               writer=csv.writer(file)
               for i in range(len(Car_ID)):
                   writer.writerow(("\t",Car_ID[i],"\t",Make[i],"\t",MODEL[i],"\t",YEAR[i],"\t",SERVICE_DATE[i],"\t\t\t",Description[i],"\t\t\t",Cost[i],"\t",service[i]))
       
      
def report():
    id=input("Enter the Car id=")
    print("c_id \t  c_make \t c_model \t c_year \t c_servicedate \t c_description \tc_cost \t c_service")
    for i in range(len(Car_ID)):
        if(id==Car_ID[i]):
            print(Car_ID[i],"\t",Make[i],"\t",MODEL[i],"\t",YEAR[i],"\t",SERVICE_DATE[i],"\t\t\t",Description[i],"\t\t\t",Cost[i],"\t",service[i])
Car_ID=[]
Make=[]
MODEL=[]
YEAR=[]
SERVICE_DATE=[]
Description=[]
Cost=[]
service=[]
average=[]
cnt=3

while(cnt!=0):
    Uname=input("ENTER THE USERNAME=")
    Upass=int(input("ENTER THE PASSWORD="))
    if(Uname=="admin" and Upass==1234):
        print("LOGIN SUCCESSFULLY")
        print("***************CAR MAINTENANCE TRACKER*************")
        cnt=1
        while(cnt!=0):
             print("1.ADD_MAINTENANCE\n 2.VIEW_LIST \n 3.UPDATE \n 4.DELETE \n 5.REPORT \n 6.EXIT")
             ch=int(input("ENTER YOUR CHOICE"))
             if(ch==1):
                 print("ADD MAINTENACE RECORD")
                 ADD_MAINTENANCE()
             if(ch==2):
                 print("VIEW LIST OF CAR RECORD")
                 VIEW_LIST()
             if(ch==3):
                 print("UPDATE CAR MAINTENANCE RECORD")  
                 Update()   
             if(ch==4):
                 print("DELETE CAR MAINTENANCE RECORD")   
                 delete()
             if(ch==5):
                 print("GENERATE A REPORT BY ID") 
                 report()   
             if(ch==6):    
                 cnt=0
        cnt=1         
    elif(Uname!="admin" and Upass!=1234):
        print("LOGIN UN-SUCCESSFULLY BOTH INCORRECT")
    elif(Uname!="admin"):
        print("USER NAME INCORRECT")
    elif(Upass!=1234):
        print("PASSWORD INCORRECT")
    cnt-=1
    print("REMAINING ATTEMPT IS=",cnt)

try:
    with open('car1.csv','r',newline='')as file:
        reader=csv.reader(file)
        for row in reader:
            print("\t c_id \t  c_make \t c_model \t c_year \t c_servicedate \t c_description \tc_cost \t c_service")
            Car_ID.append(row[0])    
            Make.append(row[1])       
            MODEL.append(row[2])      
            YEAR.append(row[3])   
            SERVICE_DATE.append(row[4])  
            Description.append(row[5])  
            Cost.append(row[6])      
            SERVICE_DATE.append(row[7])     
except FileNotFoundError:
    print("File Does Not Exists")                