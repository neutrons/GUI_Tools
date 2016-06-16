class Add(object):

    term1 = 0
    term2 = 0
    
    def __init__(self, x=0, y=0):
        self.term1 = x
        self.term2 = y
        
    def result(self):
        return self.term1 + self.term2
    
    