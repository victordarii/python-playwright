from pages.login_page import LoginPage


def test_valid_login(page):
    # Create an instance of LoginPage
    login_page = LoginPage(page)

    # Navigate to the login page
    login_page.navigate()

    # Perform login with valid credentials
    login_page.login("standard_user", "secret_sauce")

    # Assert that the URL contains 'inventory.html'
    assert "inventory.html" in page.url

