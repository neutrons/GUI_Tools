Rules:

- each testing unit should focus on one tiny bit of functionality and prove it to be correct
- each unit test should be fully independent (should be able to run without the use of the other ones).
That means that they should all use a fresh dataset (that may require some cleanup afterwards in some cases).
- try to make them run fast. 
- learn to run one single test at a time to be able to run it during modifications of the code.
- run full test suite before pushing to repo
- when debugging code, it's nice to write a test that pinpoints the particular bug found !
- use very descriptive long names to tests
     ex:   test_multiplication_float_by_list
- unit test are also used to understand how a class/method works.
- when adding new functionality, first implement unit test (to make sure it fails as it should)…then work on new feature.


ERROR -> error in code (code did not even full ran)
FAILURE -> test failed


How to run the tests:
---------------------

1/ run individual tests
> python unitTestFolder/multiplicator_test.py -v




2/ run all tests (test suite)
> python -m unittest discover -v




3/ run doctests
> python docTestFolder/square.py




4/ using nosetests (which needs to be install if not already there)
NB: nosetests does not run the doc tests
from the root directory of the project
> nosetests -v
est_list_by_number (UnitDocTests.unitTestFolder.multiplicator1_class_above_test.TestMultiplicator1) ... ok
test_list_by_number (UnitDocTests.unitTestFolder.multiplicator1_class_below_test.TestMultiplicator1) ... ok
test_list_by_list (UnitDocTests.unitTestFolder.multiplicator2_test.TestMultiplicator2) ... ok
explain here what this test is doing ... ok
This message will be displayed if this test fails ... ok
tell here what we are doing in this test ... ok
test_list_by_number (UnitDocTests.unitTestSuiteFolder.multiplicator1_test.TestMultiplicator1) ... ok
test_list_by_list (UnitDocTests.unitTestSuiteFolder.multiplicator2_test.TestMultiplicator2) ... ok
test_list_by_list (UnitDocTests.unitTestSuiteFolder.multiplicator_test.TestMultiplicator) ... ok
test_list_by_number (UnitDocTests.unitTestSuiteFolder.multiplicator_test.TestMultiplicator) ... ok
UnitDocTests.test_all.load_tests ... ERROR

======================================================================
ERROR: UnitDocTests.test_all.load_tests
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/j35/anaconda/lib/python2.7/site-packages/nose/case.py", line 197, in runTest
    self.test(*self.arg)
TypeError: load_tests() takes exactly 3 arguments (0 given)

----------------------------------------------------------------------
Ran 11 tests in 0.003s

FAILED (errors=1)




Checking the coverage of the unit tests
_______________________________________

There is a nice plugin of nosetests 'nose-cov'
This plugins shows how much code coverage is provided by our unittest


a/ install nose-cov
> pip install nose-cov

b/ run it
> nosetests --with-coverage
........
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
PyQt4                         0      0   100%
mock                       1249   1249     0%   16-2367
myMock                        0      0   100%
myMock.exporttext            27     11    59%   17, 25-35
myMock.transformtoptext      15      0   100%
-------------------------------------------------------
TOTAL                      1291   1260     2%
----------------------------------------------------------------------
Ran 8 tests in 0.077s

OK



If there is a line that is reported that does not need to be tested (like script that launch the program)
we can add the following pragma at the end of the line

  if __name__ == "__main__":   #pragma: no cover
    ....




Get colored output message
__________________________
This is done with another plugin called 'rednose'
> pip install rednose

> nosetests -v --rednose

'''will give a colored output version of the resulting unit tests'''



