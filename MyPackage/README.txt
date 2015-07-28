to run all the test, move to the top folder and do
> make test

ac83978:MyPackage j35$ make test
test_list_by_number (underLayer1.multiplicator1_class_above_test.TestMultiplicatorClassAbove) ... ok
test_list_by_list (underLayer1.multiplicator_test.TestMultiplicator)
explain here what this test is doing ... ok
test_list_by_number (underLayer1.multiplicator_test.TestMultiplicator)
This message will be displayed if this test fails ... ok
test_missing_one_argument_exception_thrown (underLayer1.multiplicator_test.TestMultiplicator)
tell here what we are doing in this test ... ok
test_list_by_number (underLayer1.multiplicator1_class_below_test.TestMultiplicatorClassBelow) ... ok
test_list_by_list (underLayer1.multiplicator2_test.TestMultiplicator2) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK


====================

to run the test individually, one must un-comment the bottom lines of each unit test and comment the last line
> python underLayer1/multiplicator1_class_above_test.py --verbose

test_list_by_number (__main__.TestMultiplicatorClassAbove) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
