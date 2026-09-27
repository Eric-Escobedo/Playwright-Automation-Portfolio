import re
from playwright.sync_api import Page, expect

class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name = "Search")
        self.search_input = page.get_by_placeholder(re.compile("search docs", re.IGNORECASE))
        
    def verify_search_loaded(self):
        expect(self.search_input).to_be_visible()
        return self
    
    def search_for(self, query: str):
        self.search_input.fill(query)
        return self
    
    def verify_search_result(self, expected_text: str):
         result_item = self.page.get_by_role("link", name = re.compile(expected_text, re.IGNORECASE)).first
         expect(result_item).to_be_visible()
         return self