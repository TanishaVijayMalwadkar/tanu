class bird:
    def intro(self):
        print("There are many types of bird:")
    def flight(self):
        print("most of the bird can fly but some cannot fly:")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostrich cannot fly")
obj_bird=bird()
obj_bird.intro()
obj_bird.flight()
obj_sparrow=sparrow()  
obj_sparrow.flight()
obj_ostrich=ostrich()
obj_ostrich.flight()
              
                    