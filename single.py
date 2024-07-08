class parent:
    def fun1(self):
        self.a=10
        print("parent fun1")
class child(parent):
    def fun2(self):
        self.b=20
        print("child fun2")
        print("Addition is=",self.a+self.b)
obj1=child()
obj1.fun1()
obj1.fun2()
                