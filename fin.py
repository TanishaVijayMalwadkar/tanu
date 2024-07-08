def add():
    c_id=int(input("enter the car id is"))
    car_id.append(c_id)
    c_cost=int(input("enter the cost"))
    cost.append(c_cost)
    c_model=input("enter the model")
    model.append(c_model)
    c_make=input("enter the make")
    make.append(c_make)
    c_des=input("enter the des")
    des.append(c_des)
    c_date=input("enter the date")
    ser_date.append(c_date)
    c_ser=int(input("enter the services"))
    services.append(c_ser)
def view():
    m_total=0
    n_ser=0
    print("c_id \t c_cost \t c_model \t c_make \t c_des \t c_date \t c_Ser")
    for i in range(len(car_id)):
        print(car_id[i],"\t",cost[i],"\t",model[i],"\t",make[i],"\t",des[i],"\t",ser_date[i],"\t",services[i])
    for i in range(len(cost)):
        m_total+=cost[i]
    print("total maintenance=",m_total)  
    for i in range(len(cost)):
        m_total+=cost[i]
        n_ser+=1
        n_ser=cost[i]/services[i]
    print("avg per services=",n_ser)     
        
        
def update():
    fid=int(input("enter the id"))
    for i in range(len(car_id)):
        if(car_id[i]==fid):
            u_id=int(input("update the id"))
            car_id[i]=u_id
            u_cost=int(input("update the cost"))
            cost[i]=u_cost
            u_model=input("update the model")
            model[i]=u_model
            u_make=input("update the make")
            make[i]=u_make
       # u_des=input("update the des")
        #des[i]=u_des
        #u_date=input("enter the date")
        #ser_date[i]=u_date
        #u_services=int(input("update the services"))
        #services[i]=u_services
def delete():
    did=int(input("enter the delete the record"))
    for i in range(len(car_id)):
        if(car_id[i]==did):
            car_id.remove(car_id[i])
            cost.remove(cost[i])
            model.remove(model[i])
            make.remove(make[i])
            services.remove(services[i])
def report():
    cid=int(input("enter the id"))
    print("c_id \t c_cost \t c_model \t c_make \t c_des \t c_date \t c_Ser")
    for i in range(len(car_id)):
        if(car_id[i]==cid):
            print(car_id[i],"\t",cost[i],"\t",model[i],"\t",make[i],"\t",des[i],"\t",ser_date[i],"\t",services[i])

                
def search():
    sid=int(input("enter the search id"))
    for i in range(len(car_id)):
        if(car_id[i]==sid):
             print(car_id[i],"\t",cost[i],"\t",model[i],"\t",make[i],"\t",des[i],"\t",ser_date[i],"\t",services[i])            
car_id=[]
cost=[]
model=[]
make=[]
des=[]
ser_date=[]
services=[]
cnt=3
while(cnt!=0):
    uname=input("enter the username=")
    upass=int(input("enter the password="))
    if(uname=="admin" and upass==1234):
        print("login success")
        cnt=1
        while(cnt!=0):
            print("1.add \n 2.view 3.update 4.delete 5.report 6.search 7.exit")
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
                print("search")
                search()
            if(ch==7):
                cnt=0
        cnt=1
    elif(uname!="admin" and upass!=1234):
        print("both incorrect")
    elif(uname!="admin"):
        print("username incorrect")
    elif(upass!=1234):
        print("password incorrect")            
    cnt-=1
    print("remaining attempt=",cnt)                                