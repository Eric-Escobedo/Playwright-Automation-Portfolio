import re
from playwright.sync_api import Page, expect

class DocsPage():
    def __init__(self, page: Page):
        self.page = page 
        self.heading = page.get_by_role("heading", name = "Installation")
        
    def verify_docs_loaded(self):
        #expect(self.page.get_by_role("link", name = "Docs")).to_be_visible()
        expect(self.page).to_have_url("https://playwright.dev/docs/intro")
        return self
        
    def verify_docs_header(self):
        expect(self.heading).to_have_text("Installation")
        return self