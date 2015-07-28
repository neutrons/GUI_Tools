Will contain code that will demonstrate the use of library argparse

-> https://docs.python.org/2/howto/argparse.html

example1.py - introduction
-----------
show how to define a mandatory argument
--help, -h arguments come from free


example2.py - 2 input mandatory variables
-----------
> python example2.py 10 5
Value of factor1 is: 10
Value of factor2 is: 5


example3.py - Specify type of variable
-----------
> python example3.py 10
Value of factor1 is: 10

> python example3.py 10.5
usage: example3.py [-h] factor1
example3.py: error: argument factor1: invalid int value: '10.5'

> python example3.py --help
usage: example3.py [-h] factor1

positional arguments:
  factor1     factor 1

optional arguments:


example4.py - Optional argument
-----------
> python example4.py --factor1=10
10

> python example4.py

> python example4.py --factor1
usage: example4.py [-h] [--factor1 FACTOR1]
example4.py: error: argument --factor1: expected one argument

> python example4.py --help
usage: example4.py [-h] [--factor1 FACTOR1]

optional arguments:
  -h, --help         show this help message and exit
  --factor1 FACTOR1  factor 1

example5.py - True/False argument
-----------
> python example5.py
> python example5.py --verbosity
verbosity turned on
> python example5.py -v
verbosity turned on

example6.py - positional and optional arguments
-----------
> python example6.py 10
> python example6.py 10 --verbose
(10)^2 = 100

example7.py - restricting values
-----------
> python example7.py 10
Done!
> python example7.py 10 --verbose 1
answer is: 100
> python example7.py 10 --verbose 2
(10)^2 = 100
> python example7.py --help
sage: example7.py [-h] [-v {0,1,2}] square
positional arguments:
  square                Number to square
optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2}, --verbose {0,1,2}
                        verbose mode

example8.py - combine flags
-----------
> python example8.py
> python example8.py -a
Flag1 has been triggered
> python example8.py -ab
Flag1 has been triggered
Flag1 has been triggered

example9.py - conflicting options
-----------
> python example9.py 
Neither quiet or verbose are on
> python example9.py -v
mode verbose is ON
> python example9.py -q
mode quiet is ON
> python example9.py -qv
usage: example9.py [-h] [-v | -q]
example9.py: error: argument -v/--verbose: not allowed with argument -q/--quiet




  