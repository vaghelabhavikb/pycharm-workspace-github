Feature: Test Customer address
  I want to test customer address as part of this feature

  Scenario: Check Customer address details
    When I navigate to Mark's address details page
    Then It should display apartment number as 121
    And Paid up amount 1.2 thousand dollors

  Scenario Outline: scenario outline test
    When I enter <number>
    Then <text> should be printed

    Examples:
    |number|text    |
    |1     |"Hi"      |
    |2     |"Hello"   |