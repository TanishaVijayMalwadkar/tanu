def addrecord():
    c_id=int(input("enter the car id"))
    car_id.append(c_id)
    c_date=input("enter the date")
    ser_date.append(c_date)
    c_model=input("enter the model")
    model.append(c_model)
    c_make=input("enter the car make")
    make.append(c_make)
    c_des=input("enter the description")
    descrition.append(c_des)
    c_year=int(input("enter the year"))
    year.append(c_year)
    c_cost=int(input("enter the cost"))
    cost.append(c_cost)
    c_ser=int(input("enter the service"))
    service.append(c_ser)
def view():
    m_total=0
    num_ser=0
    print("c_id \t c_date \t c_model \t c_make \t c_descrption \t c_year \t c_cost \t c_ser")
    for i in range(len(car_id)):
        print(car_id[i],"\t",ser_date[i],"\t",model[i],"\t",make[i],"\t",descrition[i],"\t",year[i],"\t",cost[i],"\t",service[i])    
    for i in range(len(cost)):
        m_total+=cost[i]
    print("maintenance is=",m_total)
    for i in range(len(cost)):
        m_total+=cost[i]
        num_ser+=1
        avg=cost[i]/service[i]  
    print("services is=",avg)  
        
def update():
    fid=int(input("enter the updated the record"))
    for i in range(len(car_id)):
        if(car_id[i]==fid):
            u_id=int(input("updated the car id="))
            car_id[i]=u_id
            u_date=input("update the date")
            ser_date[i]=u_date
            u_model=input("update the model")
            model[i]=u_model
            u_make=input("update the make") 
            make[i]=u_make
            u_des=input("update the des")
            descrition[i]=u_des
            u_cost=int(input("updated the cost"))
            cost[i]=u_cost   
def delete():
    did=int(input("delete the record"))
    for i in range(len(car_id)):
        if(car_id[i]==did):
            car_id.remove(car_id[i])
            ser_date.remove(ser_date[i])
            make.remove(make[i])
            model.remove(model[i])
            descrition.remove(descrition[i])
            cost.remove(cost[i])
            year.remove(year[i])   
def search():
    sid=int(input("enter the seearch the record"))
    for i in range (len(car_id)):
        if(car_id[i]==sid):
            print(car_id[i],"\t",ser_date[i],"\t",model[i],"\t",make[i],"\t",descrition[i],"\t",year[i],"\t",cost[i],"\t",service[i])  
def report():
    id=int(input("enter the car id="))
    print("c_id \t c_date \t c_model \t c_make \t c_descrption \t c_year \t c_cost \t c_ser")
    for i in range(len(car_id)):
        if(id==car_id[i]):
            print(car_id[i],"\t",ser_date[i],"\t",model[i],"\t",make[i],"\t",descrition[i],"\t",year[i],"\t",cost[i],"\t",service[i])  

                     
                        
service=[]               
car_id=[]
ser_date=[]
model=[]
make=[]
descrition=[]
year=[]
cost=[]
cnt=3
while(cnt!=0):
    uname=input("enter the username=")
    upass=int(input("enter the pass="))
    if(uname=="admin" and upass==1234):
        print("login success")
        print("car maintenance trracker")
        cnt=1
        while(cnt!=0):
            print("1.add record \n 2.view 3.update \n 4.delete \n 5.search \n 6.report \n 7.exit")
            ch=int(input("enter your choice"))
            if(ch==1):
                print("add")
                addrecord()
            if(ch==2):
                print("view")
                view()
            if(ch==3):
                print("update")
                update()
            if(ch==4):
                print("delete")
                delete()
            if(ch==5):
                print("search")    
                search()
            if(ch==6):
                print("report")
                report()    
            if(ch==7):
                cnt=0
        cnt=1
    elif(uname!="admin" and upass!=1234):
        print("both incorrect")
    elif(uname!="admin"):
        print("uname incorrect")
    elif(upass!=1234):
        print("upass incorrect")
    cnt-=1
    print("remaining attempt=",cnt)                                         