class parent1:
    def fun1(self):
        self.a=4
        print("parent")
class son1(parent1):
    def fun2(self):
        self.b=4
        print("child")
        print("multiplication is",self.a*self.b)  
class son2(parent1):
    def fun3(self):
        self.c=3
        print("child2")     
        print("multiplication is",self.a*self.c)  
obj1=son1()
obj2=son2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()
    
                    