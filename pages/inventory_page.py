from pages.base_page import BasePage

class InventoryPage(BasePage):
    def add_item_to_cart(self, item_name: str):
        self.page.click(f"text={item_name}")
        self.page.click("button:has-text('Add to cart')")

    def navigate_to_cart(self):
        self.page.click(".shopping_cart_link")
