import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Link to the feature file
scenarios('../features/checkout.feature')

@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@given("the user is on the login page")
def navigate_to_login_page(browser):
    login_page = LoginPage(browser)
    login_page.goto("https://www.saucedemo.com/v1/")

@when("the user logs in with valid credentials")
def user_logs_in(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

@when("the user adds an item to the cart")
def add_item_to_cart(browser):
    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.navigate_to_cart()

@when("the user proceeds to the checkout page")
def proceed_to_checkout(browser):
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

@when("the user fills in the checkout details")
def fill_checkout_details(browser):
    checkout_page = CheckoutPage(browser)
    checkout_page.complete_checkout("Easir", "Maruf", "1234")

@then("the user should complete the checkout successfully")
def verify_checkout_complete(browser):
    assert browser.locator("text=THANK YOU FOR YOUR ORDER").is_visible()
