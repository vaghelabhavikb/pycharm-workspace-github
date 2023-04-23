from pytest_bdd import scenario, given, when, then, scenarios
from pytest_bdd.scenario import collect_example_parametrizations

scenarios('C:\\Users\\vaghe\\PycharmProjects\\PyTestBDDProj\\venv\\BDDmain\\Featurefiles\\Blog.feature')

@given("I'm an author user")
def author_user():
    print("I'm an author user")

@given("I have an article", target_fixture="article")
def article():
    print("I have an artile")

@when("I go to the article page")
def go_to_article():
    print("I go to new article")

@when("I press the publish button")
def publish_article():
    print("I press the publish button")

@then("I should not see the error message")
def no_error_message():
    print("I should not see the error message")

@then("the article should be published")
def article_is_published():
    print("the article should be published")

# scenario('C:\\Users\\vaghe\\PycharmProjects\\PyTestBDDProj\\venv\\BDDmain\\Featurefiles\\Parameters.feature',
#          'scenario outline test',
#         example_converters=dict(number=int, text=str)
#          )
# def start_test():
#     pass
#
# @when('I enter <number>')
# def enter_number(number):
#     print("number is:" + str(number))
#
# @then('<text> should be printed')
# def text_printed(text):
#     print('printed text is' + text)
