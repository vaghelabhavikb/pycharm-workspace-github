from pytest_bdd import scenarios, when, then
from BDDmain.Utils import webdriverlib
from BDDmain.pom.select_from_dropdown_po import SelectFromDropdownPO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\SeleniumPytestBDDInternetHeroku\BDDmain\Featurefiles\SelectTest.feature')

# driver = WebDriver()

@when("we navigate to this page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/dropdown")

@when("select the value")
def select_a_value(browser):
    # ele = browser.find_element(By.ID, "dropdown")
    # Select(ele).select_by_value("Option 1")
    webdriverlib.select_value(browser,SelectFromDropdownPO.dropdown, "Option 1")

@then('value should get selected')
def verify_selected_value(browser):
    assert webdriverlib.get_selected_value(browser, SelectFromDropdownPO.dropdown) == "Option 1"









