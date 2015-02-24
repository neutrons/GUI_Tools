def square(x):
    """ Squares of x
    
    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(-3)
    6
    
    """
    
    return x*x

if __name__ == "__main__":
    import doctest
    doctest.testmod()