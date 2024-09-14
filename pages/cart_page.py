from pages.base_page import BasePage

class CartPage(BasePage):
    def verify_item_in_cart(self, item_name):
        # Locate the item in the cart based on the item name
        cart_items = self.page.locator(".inventory_item_name")
        items_count = cart_items.count()

        # Iterate over cart items and check if the specified item is in the cart
        for i in range(items_count):
            if cart_items.nth(i).text_content() == item_name:
                return True

        # If the item is not found, raise an AssertionError
        raise AssertionError(f"Item '{item_name}' not found in the cart.")


    def proceed_to_checkout(self):
        try:
            # Locate the checkout button using the class selector
            checkout_button = self.page.locator(".btn_action")
            
            # Click the button and rely on the default timeout
            checkout_button.click()
            
            # Verify navigation to the checkout step one page
            self.page.wait_for_url("**/checkout-step-one.html")
            assert "checkout-step-one.html" in self.page.url, "Failed to navigate to the checkout step one page"
        except Exception as e:
            print(f"Error during proceed to checkout: {e}")
            print("Current URL:", self.page.url)
            print("Page content:", self.page.content())
            raise
