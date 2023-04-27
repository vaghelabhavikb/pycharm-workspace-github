from pytest_bdd import scenarios, when, then

from BDDmain.Utils import webdriverlib
from BDDmain.pom.context_click_po import ContextClickPO

scenarios(r'C:\Users\vaghe\Pycharm-workspace-github\SeleniumPytestBDDInternetHeroku\BDDmain\Featurefiles\ContextClick.feature')

# driver = WebDriver()

@when("we navigate to this page")
def nav_to_this_page(browser):
    browser.get("http://the-internet.herokuapp.com/context_menu")

@when("perform context click")
def perform_context_click(browser):
    webdriverlib.context_click_on_element(browser,ContextClickPO.contextClick)

@then('alert should be displayed')
def verify_alert(browser):
    print("||||||||||||" + webdriverlib.get_alert_text(browser))
    webdriverlib.accept_alert(browser)










