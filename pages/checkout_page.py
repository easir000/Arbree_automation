from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def complete_checkout(self, first_name: str, last_name: str, postal_code: str):
        try:
            # Fill in the checkout information
            self.page.fill("#first-name", first_name)
            self.page.fill("#last-name", last_name)
            self.page.fill("#postal-code", postal_code)
            
            # Click the Continue button and rely on the default timeout
            self.page.click(".btn_primary.cart_button")
            
            # Verify navigation to the overview page
            self.page.wait_for_url("**/checkout-step-two.html")
            assert "checkout-step-two.html" in self.page.url, "Failed to navigate to the checkout step two page"
        except Exception as e:
            print(f"Error during complete checkout: {e}")
            print("Current URL:", self.page.url)
            print("Page content:", self.page.content())
            raise

    def finish_checkout(self):
        try:
            # Click the Finish button and rely on the default timeout
            self.page.click(".btn_action.cart_button")
            
            # Verify navigation to the checkout complete page
            self.page.wait_for_url("**/checkout-complete.html")
            assert "checkout-complete.html" in self.page.url, "Failed to complete checkout process"
        except Exception as e:
            print(f"Error during finish checkout: {e}")
            print("Current URL:", self.page.url)
            print("Page content:", self.page.content())
            raise
