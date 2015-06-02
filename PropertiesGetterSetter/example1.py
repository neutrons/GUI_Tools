class myClass():
    
    def __init__(cls, age):
        cls.age = age
        
if __name__ == "__main__":
    
    my_object1 = myClass(20)
    print 'age of my_object1 is %d' % my_object1.age  # looks good
    
    my_object2 = myClass(-10)
    print 'age of my_object2 is %d' % my_object2.age  # can input something crazy here