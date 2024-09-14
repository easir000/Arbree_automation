from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
