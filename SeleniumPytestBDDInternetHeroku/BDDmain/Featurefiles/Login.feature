Feature: Test the Login Feture
  I want to test the Login feature of this APP

  Background: bring app to login page
    Given user naviagtes to login page

  @IP
  Scenario Outline: test username and password entry in the form
    When user enters <username>
    And <password> to login
    And clicks on Login button
    Then user should be <validated> and if authorized then should be logged in
    Examples:
      |username |password            |validated |
      |tomsmith |SuperSecretPassword!|Valid     |
      |admin    |admin               |Invalid   |
      |user1    |pass                |Invalid   |

