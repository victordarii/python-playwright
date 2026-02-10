from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com"
        self.username_selector = "#user-name"
        self.password_selector = "#password"
        self.login_button_selector = "#login-button"
        self.error_message_selector = "[data-test='error']"

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        """Perform login with the given username and password."""
        self.page.fill(self.username_selector, username)
        self.page.fill(self.password_selector, password)
        self.page.click(self.login_button_selector)

    def is_error_message_displayed(self) -> bool:
        """Check if an error message is displayed."""
        return self.page.is_visible(self.error_message_selector)