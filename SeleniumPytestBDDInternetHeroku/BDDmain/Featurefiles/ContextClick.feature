Feature: context click feature test
   I want to test context click of the app

  Scenario: check user is able to context click
    When we navigate to this page
    And perform context click
    Then alert should be displayed