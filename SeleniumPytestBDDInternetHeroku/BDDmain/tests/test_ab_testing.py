from pytest_bdd import scenarios, given, when, then, scenario
from selenium.webdriver.chrome.webdriver import WebDriver
from BDDmain.pom.ab_testing_po import ABTestingPO
from selenium.webdriver.common.by import By
from BDDmain.Utils import webdriverlib

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\SeleniumPytestBDDInternetHeroku\BDDmain\Featurefiles\ABTesting.feature')

@when("we navigate to this page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/abtest")

@then("It should display the correct URL")
def correct_URL(browser):
    assert browser.title == "The Internet"

@then('it should display the correct page contents')
def correct_page_content(browser):
    assert webdriverlib.wait_for_visibility_of_element(browser,by = ABTestingPO.header3).is_displayed()
    assert webdriverlib.wait_for_visibility_of_element(browser,by =  ABTestingPO.paragraph).is_displayed()










