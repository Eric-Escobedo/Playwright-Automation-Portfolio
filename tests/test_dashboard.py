import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_features_link(setup_home_page: HomePage):
    # setup_home_page already opened https://playwright.dev/ for us
    
    # CLick the "Docs" link using Playwright's role locator
    setup_home_page.click_docs()
    
    # Assert that we sucessfully navigated to the intro search URL
    expect(setup_home_page.page).to_have_url("https://playwright.dev/docs/intro")