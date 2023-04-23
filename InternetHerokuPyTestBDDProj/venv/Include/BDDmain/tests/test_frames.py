from pytest_bdd import scenarios, given, when, then, scenario
from selenium.webdriver.chrome.webdriver import WebDriver
from Include.BDDmain.pom.frames_po import FramesPO
from selenium.webdriver.common.by import By
from Include.BDDmain.Utils import webdriverlib

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\InternetHerokuPyTestBDDProj\venv\Include\BDDmain\Featurefiles\Frames.feature')

# driver = WebDriver()

@when("we navigate to this page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/frames")

@when("switch to nested frame")
def switch_frame(browser):
    webdriverlib.click(browser, FramesPO.nestedFrames)
    browser.switch_to.frame(FramesPO.topFrame)
    browser.switch_to.frame(FramesPO.leftFrame)

@then('we are able to interact with the element present in the frame')
def correct_page_content(browser):
    assert webdriverlib.wait_for_visibility_of_element(FramesPO.leftFrameText).text == "LEFT"









