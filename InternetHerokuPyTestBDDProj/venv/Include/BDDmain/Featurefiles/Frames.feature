Feature: frames feature test
   I want to test frame feature of the app

  @IP
#    C:\Users\vaghe\Pycharm-workspace-github\InternetHerokuPyTestBDDProj\venv\Include\BDDmain\tests>pytest -k "not IP"
  #    C:\Users\vaghe\Pycharm-workspace-github\InternetHerokuPyTestBDDProj\venv\Include\BDDmain\tests>pytest -k "IP"
  Scenario: check user is able to switch between nested frames
    When we navigate to this page
    And switch to nested frame
    Then we are able to interact with the element present in the frame