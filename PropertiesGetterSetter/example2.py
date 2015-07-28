class GetterSetterClass():
    
    __age = -1
    
    def __init__(cls, age):
        cls.__age = age             # x is a private variable
        
    def getAge(self):
        return self.__age
    
    def setAge(cls, age):
        if age < 0:
            age = 0
        cls.__age = age
        

if __name__ == "__main__":
    
    my_object = GetterSetterClass(20)
    #print my_object.__age      # -> AttributeError: no attribute '__age'
    my_object.setAge(10)
    print my_object.getAge()    # -> 10
    my_object.setAge(-10)
    print my_object.getAge()    # -> 0

    #my_object.age = 30         # does not work anymore, we broke the interface we used in example1.py