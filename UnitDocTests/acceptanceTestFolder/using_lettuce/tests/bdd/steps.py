# -*- coding: utf-8 -*-
from lettuce import *
from nose.tools import assert_equals
from calculator.calculator import Calculator

@step(u'I am using the calculator')
def select_calc(step):
    print('Attempting to use calculator ....')
    world.calc = Calculator()

@step(u'Given I input "([^"]*)" add "([^"]*)"')
def given_i_input_group1_add_group1(step, x, y):
    world.actual_result = world.calc.add(int(x), int(y))

@step(u'Then I should see "([^"]*)"')
def then_i_should_see_group1(step, expected_result):
    assert_equals(int(expected_result), world.actual_result)