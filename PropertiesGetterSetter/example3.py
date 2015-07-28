class GetterSetterClass(object):
    
    def __init__(self, age):
        self.age = age             
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age


if __name__ == "__main__":
    
    my_object = GetterSetterClass(20)
    print my_object.age    # -> 20
    my_object.age = 10
    print my_object.age    # -> 10
    my_object.age = -20
    print my_object.age    # -> 0  
    
    my_object2 = GetterSetterClass(-20)
    print my_object2.age    # -> 0
