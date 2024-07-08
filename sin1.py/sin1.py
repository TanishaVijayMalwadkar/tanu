class A:
    def getdata(self):
        self.a=int(input("enter the a:")) 
class B(A):
    def putdata(self):
        self.b=int(input("enter the b"))
        print("addition is",self.a+self.b)
        print("substraction is",self.a-self.b)
        print("multiplication is",self.a*self.b)
        print("division is",self.a/self.b)
obj1=B()
obj1.getdata()
obj1.putdata()              