import re
from playwright.sync_api import Page, expect

class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.search_link = page.get_by_role("link", name = "search")
        self.docs_link = page.get_by_role("link", name = "Docs")
    
    def click_search(self):
        self.search_link.click()
    
    def click_docs(self):
        self.docs_link.click()