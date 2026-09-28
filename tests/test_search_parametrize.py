import re
import pytest
import json
from playwright.sync_api import Page, expect
from pages import HomePage, SearchPage

with open ("data/search_data.json") as f:
    search_data = json.load(f)
    
search_terms = [item["term"] for item in search_data]

@pytest.mark.regression
#@pytest.mark.parametrize("search_term", ["Locators", "Actions", "Routing"])
@pytest.mark.parametrize("search_term", search_terms)
def test_docusaurus_search(setup_home_page: HomePage, search_term: str):
    (
        setup_home_page
        .click_search()
        .search_for(search_term)
        .verify_search_result(search_term)
    )