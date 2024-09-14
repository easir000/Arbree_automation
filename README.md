Playwright E2E Test Suite with BDD (Cucumber)
Project Overview
This project is an end-to-end test automation suite for the "SauceDemo" website (https://www.saucedemo.com/v1/), developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.

Key features include:

Page Object Model (POM) for scalable and maintainable test automation.
Behavior Driven Development (BDD) using pytest-bdd for human-readable tests.
Integration with GitHub Actions for Continuous Integration (CI).
Allure Reporting for test results.
Scenarios Covered:
User login
Adding items to the cart
Verifying cart contents
Completing the checkout process
Project Structure
plaintext

playwright-test-suite/
├── features/                # Gherkin feature files for BDD
│   ├── checkout.feature      # Feature file for the checkout process
├── steps/                   # Step definition files for feature steps
│   ├── checkout_steps.py     # Step definitions for the checkout feature
├── pages/                   # Page Object Model classes
│   ├── base_page.py          # BasePage class for shared methods
│   ├── login_page.py         # Page class for login functionality
│   ├── inventory_page.py     # Page class for inventory actions
│   ├── cart_page.py          # Page class for cart actions
│   └── checkout_page.py      # Page class for the checkout process
├── tests/                   # Optional: Additional test scripts
│   └── test_checkout.py      # Example standalone test without BDD
├── .github/                 # GitHub Actions CI configuration
│   └── workflows/
│       └── ci.yml            # CI configuration to run tests on push
├── allure-results/           # Directory for storing Allure reports
├── README.md                 # This README file
├── pytest.ini                # pytest configuration file
├── requirements.txt          # Python dependencies
└── conftest.py               # Pytest configuration for Playwright
Prerequisites
Ensure that the following tools are installed on your system:

Python 3.7+
Node.js (for Playwright dependencies)
pip (Python package manager)
Install Playwright’s browser binaries:



playwright install
Installation
Clone the repository:



git clone <repository-url>
cd playwright-test-suite
Set up a virtual environment:


#On macOS/Linux:
python3 -m venv venv
source venv/bin/activate


#On Windows:
python -m venv venv
venv\Scripts\activate


#Install dependencies:

pip install -r requirements.txt
Install Playwright browsers:



#playwright install

Running the Test Suite
Run all tests with BDD:


#To run the full test suite using BDD and Cucumber (via pytest-bdd):

pytest -v


Run specific feature file:
To run a specific feature file, use:

pytest -v features/checkout.feature


#Run with Allure Reporting:
To generate an Allure report:

Run the tests and generate the report data:

pytest --alluredir=allure-results

#Serve the report in a local web server:
allure serve allure-results


#Writing Your Own Feature Files
Example Feature File (checkout.feature):
gherkin

Feature: Checkout an item

  Scenario: Checkout a single item
    Given the user is on the login page
    When the user logs in with valid credentials
    And the user adds an item to the cart
    And the user proceeds to the checkout page
    And the user fills in the checkout details
    Then the user should complete the checkout successfully
Place all feature files in the features/ directory.

#Step Definitions
The corresponding step definitions should be placed in the steps/ directory. Each step in the feature file will map to a Python function in a step definition file (e.g., checkout_steps.py).



import pytest
from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Fixture for browser setup
@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

# Step Definitions
@given("the user is on the login page")
def navigate_to_login_page(browser):
    login_page = LoginPage(browser)
    login_page.goto("https://www.saucedemo.com/v1/")

@when("the user logs in with valid credentials")
def user_logs_in(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

@when("the user adds an item to the cart")
def add_item_to_cart(browser):
    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.navigate_to_cart()

@when("the user proceeds to the checkout page")
def proceed_to_checkout(browser):
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

@when("the user fills in the checkout details")
def fill_checkout_details(browser):
    checkout_page = CheckoutPage(browser)
    checkout_page.complete_checkout("Easir", "Maruf", "1234")

@then("the user should complete the checkout successfully")
def verify_checkout_complete(browser):
    assert browser.locator("text=THANK YOU FOR YOUR ORDER").is_visible()
GitHub Actions (CI/CD)
The project includes a GitHub Actions configuration (.github/workflows/ci.yml) to automate the test execution on every push to the repository.

To enable this:

Push your project to GitHub.
Edit .github/workflows/ci.yml to adjust your Playwright setup or dependencies if necessary.
The workflow will automatically run tests for every push or pull request.
Sample CI Configuration (ci.yml):
yaml

name: Playwright Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        playwright install
    - name: Run Playwright tests
      run: |
        source venv/bin/activate
        pytest --headed --alluredir=allure-results
    - name: Upload Allure results
      uses: actions/upload-artifact@v2
      with:
        name: allure-results
        path: allure-results



#Running Tests in Parallel
To run tests in parallel, you can use the pytest-xdist plugin:



pip install pytest-xdist
pytest -n <number_of_processes>
For example:



pytest -n 4  # Runs the tests in parallel using 4 processes
Code Quality (Optional)
For code quality, you can integrate a linter like ESLint for JavaScript/TypeScript files or flake8 for Python files.

#Example .eslintrc.js configuration for Playwright projects:


module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "rules": {
        "no-unused-vars": "warn",
        "no-console": "off"
    }
};
Contributors
@khause
@Tosinfamzy
@ChrisSargent
License
This project is licensed under the MIT License.
