import re
from playwright.sync_api import Page, expect

def test_search_documentation(page: Page):
    #1. Navigate to Playwright docs
    page.goto("https://playwright.dev/")
    
    #2. Click the search button/bar (Playwright uses a docsearch model)
    page.get_by_role("button", name="Search").click()
    
    #3. Type search term into the input box
    page.get_by_placeholder("Search docs").fill("locators")
    
    #4. Verify that a releveant search result appears
    expect(page.get_by_role("link", name="Locators", exact=True)).to_be_visible()