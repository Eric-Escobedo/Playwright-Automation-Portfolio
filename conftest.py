import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page

@pytest.fixture
def setup_home_page(page: Page) -> HomePage:
    home = HomePage(page)
    page.goto("https://playwright.dev/")
    return home