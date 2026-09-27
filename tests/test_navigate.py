import re
from playwright.sync_api import Page, expect
from pages import HomePage, DocsPage

def test_navigate_to_docs(setup_home_page):
    setup_home_page.click_docs().verify_docs_loaded()
    
def test_naviagte_to_search(setup_home_page):
    (
        setup_home_page.click_search()
        .verify_search_loaded()
        .search_for("locators")
        .verify_search_result("Locators")
    )