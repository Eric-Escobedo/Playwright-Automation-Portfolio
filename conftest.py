import pytest
import configparser
from pages.home_page import HomePage
from playwright.sync_api import Page

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment to run tests against dev, staging or prod"
    )

@pytest.fixture(scope="session")
def config(request):
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    env = request.config.getoption("--env")
    
    if env not in config:
        raise ValueError(f"Environment '{env}' is not defiend in config.ini")
    return config[env]

@pytest.fixture
def setup_home_page(page: Page, config) -> HomePage:
    base_url = config.get("base_url")
    home = HomePage(page)
    #page.goto("https://playwright.dev/")
    page.goto(base_url)
    return home