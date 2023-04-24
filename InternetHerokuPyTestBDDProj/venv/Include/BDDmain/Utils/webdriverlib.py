from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def wait_for_visibility_of_element(browser, by):
    return WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((by)))

def click(browser, by):
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(wait_for_visibility_of_element(browser, by))).click()