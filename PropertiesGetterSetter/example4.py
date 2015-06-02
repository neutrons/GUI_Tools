class GetterSetterClass(object):
    
    def __init__(cls, age):
        cls.setAge(age)
        
    def getAge(cls):
        return cls.__age
    
    def setAge(cls, age):
        if age < 0:
            cls.__age = 0
        else:
            cls.__age = age

    age = property(getAge, setAge)


if __name__ == "__main__":
    
    my_object = GetterSetterClass(20)
    print my_object.age    # -> 20
    my_object.age = 10
    print my_object.age    # -> 10
    my_object.age = -20
    print my_object.age    # -> 0
