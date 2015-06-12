Feature: Addition                       # only 1 feature per document
    In order to avoid silly mistakes
    As a math idiot
    I want to be told the sum of two numbers
    
Scenario: Add two numbers               # can contain more than 1 scenario
    Given I have powered calculator on      
    # here for this comment
    When I enter "50" into the calculator 
    And I enter "70" into the calculator
    And I press add
    Then the result should be "120" on the screen
    
# Given: initial state of system (past tense)
# When: describes action (present tense)
# Then: final state of system (future tense)
