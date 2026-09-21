import re
from playwright.sync_api import Page, expect

def test_homepage_has_correct_title(page: Page):
    # Havigate to the offical Playwright site
    page.goto("https://playwright.dev/") 
    expect(page).to_have_title(re.compile("Playwright"))
    
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    
    #Click the "Get started" link
    page.get_by_role("link", name="Get started").click()
    
    #Expect the URL to contain intro/sintallation docs
    expect(page).to_have_url(re.compile(".*intro"))