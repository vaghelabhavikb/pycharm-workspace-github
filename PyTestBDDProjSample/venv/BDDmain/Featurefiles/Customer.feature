Feature: Test Customer details
  I want to test customer details as part of this feature

  Background: pre
    Given prerequisite is fulfilled
    Then procced further

  @Smoke
  Scenario: Check Customer naming details
    When I navigate to customer naming details page
    Then I should be able to find the correct customer name and surname