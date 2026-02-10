import os
import pytest
from playwright.sync_api import sync_playwright

# Create a pytest fixture for the Playwright browser with session scope
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=True)
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# Create a pytest fixture for a new page with function scope
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# Pytest hook to capture a screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Check if the test failed
    if result.when == "call" and result.failed:
        # Get the page fixture if available
        page = item.funcargs.get("page")
        if page:
            # Create the screenshots directory if it doesn't exist
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save the screenshot with the test name
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)