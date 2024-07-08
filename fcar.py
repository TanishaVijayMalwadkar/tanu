def add():
   c_id=int(input("enter the id"))
   car_id.append(c_id)
   c_make=input("enter the make")
   make.append(c_make)
   c_model=input("enter the model")
   model.append(c_model)
   c_des=input("enter the des")
   des.append(c_des)
   c_date=input("enter the date")
   ser_date.append(c_date)
   c_cost=int(input("enter the cost"))
   cost.append(c_cost)
   c_service=int(input("enter the service"))
   service.append(c_service)
def view():
    m_total=0
    n_ser=0
    print("c_id \n c_make \n c_model \n c_des \n c_ser \n c_cost \n c_Service")
    for i in range(len(car_id)):
        print(car_id[i],"\t",make[i],"\t",model[i],"\t",des[i],"\t",ser_date[i],"\t",cost[i],"\t",service[i])
    for i in range(len(cost)):
      m_total+=cost[i]
    print("maintenance is=",m_total)        
    for i in range(len(cost)):
        m_total+=cost[i]
        n_ser+=1
        avg=cost[i]/service[i]
    print("avg is=",avg)    
        
def update():
    fid=int(input("enter the carid"))
    for i in range(len(car_id)):
        if(car_id[i]==fid):
           u_id=int(input("update the id"))
           car_id[i]=u_id
           u_make=input("update make")
           make[i]=u_make
           u_model=input("update model")
           model[i]=u_model
           u_des=input("update des")
           des[i]=u_des
           u_ser=input("update the date")
           ser_date[i]=u_ser
           u_cost=int(input("update cost"))
           cost[i]=u_cost
           u_ser=int(input("enter the service"))
           service[i]=u_ser
def delete():
    did=int(input("delete the record"))
    for i in range(len(car_id)):
        if(car_id[i]==did):
            car_id.remove(car_id[i])
            make.remove(make[i])
            model.remove(model[i])
            des.remove(des[i])
            ser_date.remove(ser_date[i])
            cost.remove(cost[i])
            service.remove(service[i])
def report():
    id=int(input("enter the id"))
    print("c_id \n c_make \n c_model \n c_des \n c_ser \n c_cost \n c_Service")
    for i in range(len(car_id)):
        if(car_id[i==id]):
            print(car_id[i],"\t",make[i],"\t",model[i],"\t",des[i],"\t",ser_date[i],"\t",cost[i],"\t",service[i]) 
def search():
    sid=int(input("search id is"))  
    for i in range(len(car_id)):
        if(car_id[i]==sid):
            print(car_id[i],"\t",make[i],"\t",model[i],"\t",des[i],"\t",ser_date[i],"\t",cost[i],"\t",service[i])

              
                
        
                       
service=[]
car_id=[]
make=[]
model=[]
des=[]
ser_date=[]
cost=[]
cnt=3
while(cnt!=0):
    uname=input("enter the username=")
    upass=int(input("enter the password"))
    if(uname=="admin" and upass==1234):
        print("login success")
        print("car maintenance")
        cnt=1
        while(cnt!=0):
            print("1.add \n 2.view \n 3.update \n 4.delete \n 5.report \n 6.search \n 7.exit ")
            ch=int(input("enter your choice"))
            if(ch==1):
                print("add")
                add()
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
                print("report")
                report()
            if(ch==6):
                print(search)
                search()    
            if(ch==7):
                cnt=0
        cnt=1
    elif(uname!="admin" and upass!="1234"):
        print("both incorrect") 
    elif(uname!="admin"):
        print("username incorrect")
    elif(upass!=1234):
        print("password incorrect")
    cnt-=1
    print("remaining attempt=",cnt)                  
                    