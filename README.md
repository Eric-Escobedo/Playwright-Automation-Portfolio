# Playwright Python QA Portfolio
A portfolio project demonstrating UI and REST API test automation using Python, Playwright, Pytest and GitHub Actions.

[![Playwright Tests](https://github.com/Eric-Escobedo/Playwright-Automation-Portfolio/actions/workflows/playwright.yml/badge.svg)](https://github.com/Eric-Escobedo/Playwright-Automation-Portfolio/actions/workflows/playwright.yml)

## Tech Stack
* **Language:** Python
* **Automation Tool:** Playwright for Python
* **Test Runner:** Pytest (with markers & parametrization)

## Project Structure
* `pages/` - Page Object classes encapsulating locators and actions
* `test/` - UI and REST API test suites
* `utils/` - Configuration and helper utilities

## How to Run Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/Eric-Escobedo/Playwright-Automation-Portfolio.git
    cd Playwright-Automation-Portfolio
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```
3. Execute the test suite:
    ```bash
    pytest -v
    ```

## Useful Options
* Smoke tests only: `pytest -v -m smoke`
* Regression tests only: `pytest -v -m regression`
* Different environment: `pytest -v --env staging`

