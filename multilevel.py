class parent1:
    def fun1(self):
        self.a=10
        print("parent1")
class parent2(parent1):
    def fun2(self):
        self.b=20
        print("parent2")
class parent3(parent2) : 
    def fun3(self):
        self.c=30
        print("parent3") 
        print("Addition is",self.a+self.b+self.c)
obj=parent3()
obj.fun1()
obj.fun2()
obj.fun3()             