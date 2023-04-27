from pytest_bdd import scenarios, given, when, then, scenario
from selenium.webdriver.chrome.webdriver import WebDriver
from BDDmain.pom.windows_po import WindowsPO
from selenium.webdriver.common.by import By
from BDDmain.Utils import webdriverlib

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\SeleniumPytestBDDInternetHeroku\BDDmain\Featurefiles\Windows.feature')

# driver = WebDriver()

@when("we navigate to this page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/windows")

@when("open and navigate to new opened tab")
def switch_frame(browser):
    current_window_handle = browser.current_window_handle;
    webdriverlib.click(browser,WindowsPO.clickHereLinkText)
    window_handles = browser.window_handles;
    browser.switch_to.window(current_window_handle)
    for handle in window_handles:
        if (handle == current_window_handle):
            continue
        else:
            browser.switch_to.window(handle)
    # assert 1==2



@then('we should be able to navigate to and back from opened tab successfully')
def correct_page_content(browser):
    pass










