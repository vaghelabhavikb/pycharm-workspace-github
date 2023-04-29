from selenium.webdriver.common.by import By

class LoginPO():
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CLASS_NAME, "radius")

    succesfull_login = (By.XPATH, '//div[contains(text(), "You logged into a secure area!")]')
    failed_login = (By.XPATH, '//div[contains(text(), "Your username is invalid!")]')


