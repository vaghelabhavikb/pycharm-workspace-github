from pytest_bdd import given, when, then, scenario, scenarios
from pathlib import Path

# featureFileDir = 'Featurefiles'
# featureFile = 'Customer.feature'
# BASE_DIR = Path(__file__).resolve().parent
# FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@scenario('C:\\Users\\vaghe\\PycharmProjects\\PyTestBDDProj\\venv\\BDDmain\\Featurefiles\\Customer.feature', 'Check Customer naming details')
def test_customer_details():
    pass

@when('I navigate to customer naming details page')
def navigate():
    print("Navigated")

@then('I should be able to find the correct customer name and surname')
def check_details():
    print("Checked")
    assert 1==2;

@given('prerequisite is fulfilled')
def setup():
    print("Setup Done")

@then('procced further')
def pre_step():
    print('procced further')


