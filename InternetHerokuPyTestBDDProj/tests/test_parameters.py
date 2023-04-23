
from pytest_bdd import given, when, then, scenarios, parsers

scenarios('C:\\Users\\vaghe\\PycharmProjects\\PyTestBDDProj\\venv\\BDDmain\\Featurefiles\\Parameters.feature')


@when(parsers.parse('I navigate to {person} address details page'))
def check_person_address(person):
    print('address check for person:' + person)

@then(parsers.parse('It should display apartment number as {apartment}'))
def check_apartment_number(apartment):
    print(apartment)

@then(parsers.parse('Paid up amount {paidup} thousand dollors'))
def check_paid_up(paidup):
    print(paidup)

