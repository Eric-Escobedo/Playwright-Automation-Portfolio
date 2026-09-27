import re
from playwright.sync_api import Page, expect
#from pages import DocsPage, SearchPage

class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.search_link = page.get_by_role("button", name = re.compile("Search", re.IGNORECASE))
        self.docs_link = page.get_by_role("link", name = "Docs")
    
    def click_search(self):
        from pages import SearchPage
        self.search_link.click()
        return SearchPage(self.page)
    
    def click_docs(self):
        from pages import DocsPage
        self.docs_link.click()
        return DocsPage(self.page)