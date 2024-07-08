class A:
    def getdata(self):
        self.a=int(input("enter the a"))
class B(A):
    def putdata(self):
        self.b=int(input("enter the b"))
        print("Addition is=",self.a+self.b)
class C(A):
    def putdata(self):
        self.c=int(input("enter the c"))
        print("Addition is=",self.a+self.c)
obj1=B()
obj1.getdata()
obj1.putdata()
obj2=C()     
obj2.getdata()
obj2.putdata()                 