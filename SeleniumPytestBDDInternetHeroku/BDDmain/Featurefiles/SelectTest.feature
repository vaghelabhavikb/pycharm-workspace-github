Feature: selection with Select class feature test
   I want to test selection from drop down with help of Select class

  @IP
  Scenario: check user is able to select value from drop down
    When we navigate to this page
    And select the value
    Then value should get selected