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




