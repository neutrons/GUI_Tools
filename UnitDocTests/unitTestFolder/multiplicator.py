class Multiplicator(object):
    '''
    Simple multiplication class to check how unittest works

    arg1 = [1,2,3]
    arg2 = [10,11,12]
    result = [10,22,36]
    
    arg1 = 2
    arg2 = [10,11,12]
    result = [20,22,24]
    
    arg1 = [1,2,3]
    arg2 = 10
    result = [10,20,30]
    
    arg1 = 2
    arg2 = 3
    result = 6
    
    if arg1/arg2 is a string, or None
    result = None
    
    '''
    arg1 = None
    arg2 = None
    
    result = None

    def __init__(self, arg1=None, arg2=None):
        
        if isinstance(arg1, str) or isinstance(arg2, str):
            self.result = None
            return
        
        if (arg1 is None) or (arg2 is None):
            self.resutl = None
            return
        
        if ((isinstance(arg1, int) or isinstance(arg1, float)) and (isinstance(arg2, int) or isinstance(arg2, float))):
            self.result = None
            return
            
        try:
            if isinstance(arg1, list):
                
                if isinstance(arg2, list):
                    self.listByList(arg1, arg2)
                    
                else:
                    self.listByValue(arg1, arg2)
                    
            else:
                
                self.listByValue(arg2, arg1)

        except TypeError:
            raise TypeError("something wrong")
                
    def listByValue(self, argList, value):
        for idx,val in enumerate(argList):
            argList[idx] *= value
        self.result = argList
        
        
    def listByList(self, arg1, arg2):
        _sz_arg1 = len(arg1)
        _sz_arg2 = len(arg2)
        
        left_arg = arg1
        right_arg = arg2
        
        if _sz_arg1 > _sz_arg2:
            left_arg = arg2
            right_arg = arg1
            
        for idx, val in enumerate(left_arg):
            right_arg[idx] = right_arg[idx] * val
            
        self.result = right_arg
        
    def result(self):
        return self.result
    
        
if __name__ == "__main__":
    
    a=10
    b=[1,2,3]
    
    obj = Multiplicator(arg1=a, arg2=b)
    print obj.result