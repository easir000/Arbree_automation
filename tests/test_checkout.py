import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        # Launch browser with a default timeout setting
        browser = p.chromium.launch(headless=False)  # Run in headed mode for debugging
        context = browser.new_context()
        
        # Set a default timeout for all operations (e.g., 30 seconds)
        context.set_default_timeout(120000)  # 30000 milliseconds = 30 seconds
        
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_checkout_item(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # Step 1: Navigate to the website
    login_page.goto("https://www.saucedemo.com/v1/")

    # Step 2: Login as standard_user
    login_page.login("standard_user", "secret_sauce")

    # Step 3: Add items to cart
    inventory_page.add_item_to_cart("Sauce Labs Backpack")

    # Step 4: Verify the correct items were added to the cart
    inventory_page.navigate_to_cart()
    cart_page.verify_item_in_cart("Sauce Labs Backpack")

    # Step 5: Proceed to Checkout
    cart_page.proceed_to_checkout()

    # Step 6: Complete Checkout Information
    checkout_page.complete_checkout("Easir", "Maruf", "1234")

    # Step 7: Finish Checkout Process
    checkout_page.finish_checkout()
