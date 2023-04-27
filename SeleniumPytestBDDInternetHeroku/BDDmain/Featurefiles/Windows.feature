Feature: windows feature test
   I want to test windows feature of the app


  Scenario: check user is able to switch to opened new tab
    When we navigate to this page
    And open and navigate to new opened tab
    Then we should be able to navigate to and back from opened tab successfully