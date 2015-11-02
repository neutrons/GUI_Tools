from code.add import Add


class main(object):
    
    def __init__(self, x=0, y=0):
        o_add = Add(x=x, y=y)
        print("Sum of %f and %f is %f" %(x, y, o_add.result()))
        
if __name__ == "__main__":
    main(x=5, y=6)
        