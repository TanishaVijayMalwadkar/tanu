cnt=3
while(cnt!=0):
    uname=input("ENTER THE USERNAME=")
    upass=int(input("ENTER THE PASSWORD="))
    if(uname=="admin" and upass==1234):
            print("LOGIN SUCCESSFULLY")
            print("*********LIBRARY MANAGEMENT SYSTEM*********")
            cnt=1
            while(cnt!=0):
                 print("1.addbook \n 2.viewbook \n 3.update \n 4.delete \n 5.search \n 6.exit")
                 ch=int(input("ENTER YOUR CHOICE="))
            if(ch==1):
                    print("ADDTHE BOOK")
            if(ch==2):
                print("VIEW THE BOOK LIST")
            if(ch==3):
                print("UPDATE THE BOOK")
            if(ch==4):
                print("DELTE THE BOOK")
            if(ch==5):
                print("SEARCH THE BOOK")
            if(ch==6):
                 cnt=0
        cnt=1        
    elif():
    print("REMAINING ATTEMPT=",cnt)    
    
