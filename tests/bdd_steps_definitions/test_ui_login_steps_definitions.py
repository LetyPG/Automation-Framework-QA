from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage # <-- Import your existing POM
from pages.products_page import ProductsPage

# This links the .py file to the .feature file
@scenario(
    '../../features/ui/login.feature',  # Path to the feature
    'Successful Login'                  # Scenario name
)
def test_successful_login():
    """BDD test for successful login."""
    pass

# --- Step Definitions ---

# 'browser' and 'login_page' are fixtures from your conftest.py
# pytest-bdd will inject them automatically!

@given('I am on the login page')
def go_to_login_page(browser, login_page):
    login_page.load()  # Assumes your page object has a 'load' method

@when(parsers.parse('I enter "{user}" and "{password}"'))
def enter_credentials(login_page, user, password):
    # This is the key, REUSING existing code.
    login_page.perform_login(user, password) 

@then('I should be logged in successfully')
def check_login_success(browser):
    # You might have another page object for this
    products_page = ProductsPage(browser)
    assert products_page.is_title_visible(), "Login failed"