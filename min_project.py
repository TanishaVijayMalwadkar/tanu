
def addstudent():
    sroll=int(input("ENTER THE ROLL_NUMBER="))
    roll.append(sroll)
    sname=input("ENTER THE NAME=")
    name.append(sname)
    smarks=int(input("ENTER THE MARKS="))
    marks.append(smarks)
def view_list():
    print("ROLL \t NAME \t MARKS")
    for i in range(len(roll)):
        print(roll[i],"\t",name[i],"\t",marks[i])
def update():
    froll=int(input("ENTER THE ROLL OF UPDATE"))
    for i in range(len(roll)):
        if(roll[i]==froll):
                uroll=int(input("UPDATE THE ROLL_NUMBER="))
                uname=(input("UPDATE THE NAME="))
                umarks=int(input("UPDATE THE MARKS="))
                roll[i]=uroll
                name[i]=uname
                marks[i]=umarks
def delete():
    droll=int(input("ENTER THE ROLL OF DELETE="))
    for i in range(len(roll)):
        if(roll[i]==droll):
            roll.remove(roll[i])
            name.remove(name[i])
            marks.remove(marks[i])
            break
def search():
    stroll=int(input("ENTER THE SEARCH ROLL NO="))
    for i in range(len(roll)):
         if(roll[i]==stroll):
                print(roll[i],"\t",name[i],"\t",marks[i])

            
roll=[]
name=[]
marks=[]
count=3
while(count!=0):
    uname=input("ENTER THE USERNAME=")
    upass=input("ENTER THE PASSWORD=")
    if(uname=="admin" and upass=="1234"):
        print("LOGIN SUCCESSFULLY")
        print("Student Management System")
        cnt=1
        while(cnt!=0):
             print("1.add student\n 2.view_list \n 3.update \n 4.delete \n 5.search \n 6.exit")
             ch=int(input("ENTER YOUR CHOICE"))
             if(ch==1):
                 print("add student")
                 addstudent()
             if(ch==2):
                 print("view list")
                 view_list()
             if(ch==3):
                 print("update")
                 update()
             if(ch==4):
                 print("delete")
                 delete()
             if(ch==5):        
                 print("search=")
                 search()
             if(ch==6):
                 cnt=0
        count=1         
    elif(uname!="admin" and upass!="1234"):
        print("login un-successfully both incorrect")
    elif(uname!="admin"):
        print("user name incorrect")
    elif(upass!="1234"):
        print("password incorrect")
    count-=1
    print("remaining attemet=",count)

