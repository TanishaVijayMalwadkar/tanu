cnt=0
while(cnt!=0):
    uname=input("enter the username=")
    upass=int(input("enter the password="))
    if(uname=="admin" and upass==1234):
        print("login successfully")
        print("employee management system")
        cnt=1
        while(cnt!=0):
            print("1.add \n 2.view \n 3.update 4.delete \n 5.search \n 6.exit")
            ch=int(input("enter your choice"))
            if(ch==1):
                print("add record")
            if(ch==2):
                print("view list")
            if(ch==3):
                print("update record")
            if(ch==4):
                print("delete")
            if(ch==5):
                print("search")
            if(ch==6):
                cnt=0
        cnt=1
    elif(uname!="admin" and upass!=1234):
        print("both incorrect") 
    elif(uname!="admin"):
        print("username incorrect")
    elif(upass!=1234):
        print("password incorrect")
    cnt-=1
    print("remaining attempt",cnt)                                               