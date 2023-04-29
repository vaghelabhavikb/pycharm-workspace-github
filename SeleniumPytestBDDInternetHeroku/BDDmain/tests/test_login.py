from pytest_bdd import scenarios, given, when, then, scenario, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from BDDmain.pom.login_po import LoginPO
from selenium.webdriver.common.by import By
from BDDmain.Utils import webdriverlib

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\SeleniumPytestBDDInternetHeroku\BDDmain\Featurefiles\Login.feature')

@given("user naviagtes to login page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/login")

@when(parsers.parse("user enters {uname}"))
def enter_username(browser, uname):
    webdriverlib.send_text(browser, LoginPO.username, uname)

@when(parsers.parse("{pword} to login"))
def enter_password(browser, pword):
    webdriverlib.send_text(browser, LoginPO.password, pword)

@when("clicks on Login button")
def click_login(browser):
    webdriverlib.click(browser, LoginPO.login_btn)

@then(parsers.parse('user should be {check} and if authorized then should be logged in'))
def correct_page_content(browser, check):
    if check == "Valid":
        assert webdriverlib.wait_for_visibility_of_element(browser, LoginPO.succesfull_login).is_displayed()
    else:
        assert webdriverlib.wait_for_visibility_of_element(browser, LoginPO.failed_login).is_displayed()









