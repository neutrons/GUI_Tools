class GetterSetterClass(object):
    
    _a = '1 underscore'
    __b = '2 underscore'
    
    def __init__(self, age):
        self.setAge(age)
        
    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age

    age = property(getAge, setAge)


if __name__ == "__main__":
    
    my_object = GetterSetterClass(20)
    print my_object.age    # -> 20
    my_object.age = 10
    print my_object.age    # -> 10
    my_object.age = -20
    print my_object.age    # -> 0
    print my_object._a
    print my_object.__b
