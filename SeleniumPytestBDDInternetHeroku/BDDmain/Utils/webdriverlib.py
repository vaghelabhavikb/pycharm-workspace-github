from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

def wait_for_visibility_of_element(browser, by):
    return WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((by)))

def click(browser, by):
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(wait_for_visibility_of_element(browser, by))).click()

def mouse_move_to_element(browser, by):
    ele = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(wait_for_visibility_of_element(browser, by)))
    ActionChains(browser).move_to_element(ele).perform()

def mouse_click_on_element(browser, by):
    ele = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(wait_for_visibility_of_element(browser, by)))
    ActionChains(browser).click(ele).perform()

def context_click_on_element(browser, by):
    ele = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(wait_for_visibility_of_element(browser, by)))
    ActionChains(browser).context_click(ele).perform()

def accept_alert(browser):
    Alert(browser).accept()

def dismiss_alert(browser):
    Alert(browser).dismiss()

def send_text_alert(browser, s):
    Alert(browser).send_keys(s)

def get_alert_text(browser):
    return Alert(browser).text

def select_value(browser, by ,value):
    Select(wait_for_visibility_of_element(browser,by)).select_by_visible_text(value)

def get_selected_value(browser, by):
    return Select(wait_for_visibility_of_element(browser, by)).first_selected_option.text

def send_text(browser, by, text):
    ele = wait_for_visibility_of_element(browser, by)
    ele.send_keys(text)