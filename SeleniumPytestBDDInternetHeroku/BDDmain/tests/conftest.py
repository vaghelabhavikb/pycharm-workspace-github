import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    op = Options()
    op.add_experimental_option("excludeSwitches", ['enable-automation'])
    op.add_argument("--start-maximized")
    # op.add_argument('--headless')
    b = webdriver.Chrome(options=op)
    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()

def pytest_bdd_before_scenario(request, feature, scenario):
    print('====Before scenario hook executed')

def pytest_bdd_after_scenario(request, feature, scenario):
    print('====After scenario hook executed')

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    br = step_func_args.get('browser')
    s = scenario.name
    st = step.name
    br.get_screenshot_as_file("C:\\Users\\vaghe\\Pycharm-workspace-github\\SeleniumPytestBDDInternetHeroku\\BDDmain\\Result\\FailureScreenshots\\" + s + "__" + st + ".png")