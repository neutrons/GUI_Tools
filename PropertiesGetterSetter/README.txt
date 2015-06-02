What is the decorator property (@property) ?
Why should we use it ?
How to provide elegant setter and getter methods to our class ?



example1.py
___________
This is the way I was defining my variable so far. Looks good but this does not prevent the user
from giving any crazy number (even string) when a normal age is expected.

The solution could be to use the Java convention of getter and setter such as illustrated in example2.py


example2.py
___________

In this example, using the 'Java' way of setting and getting a variable from a class
called GetterSetterClass

the variable __age is private, not accessible from outside the class withou using the 
getter and setter functions
> print my_object.__age   throws an error

Thanks to the setter, we can control the input.

Having to use myObject.getX() and myObject.setX() all the time is horrible. And if we add new variable, we need 
to add the getter and setter for those guys !!!!

Also, we can use the same interface as in example1.py where we set the Age using 
> my_object.age = 20

they must be a better way that does not break the interface.


example3.py
___________

Using the @property and @x.setter
This way, the user doesn't even realize that the setter go through a 'valid input check'.


example4.py
___________

Using the same technique, but with a different syntax without decorators to define the property. 
using getX and setX (less elegant way plus we need to make sure we use the setter function in the __init__ method.










Those examples are based on the following tutorial: http://www.python-course.eu/python3_properties.php