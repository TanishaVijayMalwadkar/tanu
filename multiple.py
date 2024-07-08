class parent1:
    def fun1(self):
        self.a=10
        print("hello parent 1")
class parent2:
    def fun2(self):
        self.b=20
        print("hello parent2")
class child(parent1,parent2):
    def fun3(self):
        self.c=30
        print("hello child")
        print("Addition is =",self.a+self.b+self.c)
obj=child()
obj.fun1()
obj.fun2()
obj.fun3()        
                
            