Feature: Checkout an item from SauceDemo

  Scenario: Successful checkout process
    Given I navigate to the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    And I add "Sauce Labs Backpack" to the cart
    Then I verify that "Sauce Labs Backpack" is added to the cart
    And I proceed to checkout
    And I complete the checkout with "Easir", "Maruf", and "1234"
    Then I verify the checkout is successful



Playwright E2E Test Suite with BDD (Cucumber)
Project Overview
This project is an end-to-end test automation suite for the SauceDemo website, developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.

Key Features
Page Object Model (POM): A scalable and maintainable design pattern for UI tests.
Behavior Driven Development (BDD): Human-readable test scenarios using pytest-bdd.
Continuous Integration (CI): GitHub Actions integration for automatic test execution on push.
Allure Reporting: Generate test reports for visual insights.
Scenarios Covered
User login.
Adding items to the cart.
Verifying cart contents.
Completing the checkout process.
Project Structure
plaintext
Copy code
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
Install Playwright Browsers
Before running the tests, install the Playwright browsers:

bash
Copy code
playwright install
Installation
Step 1: Clone the Repository
bash
Copy code
git clone <repository-url>
cd playwright-test-suite
Step 2: Set Up a Virtual Environment
On macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
On Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Running the Test Suite
Run All Tests with BDD
To run the full test suite using BDD with pytest-bdd:

bash
Copy code
pytest -v
Run a Specific Feature File
To run a specific feature file (e.g., checkout.feature):

bash
Copy code
pytest -v features/checkout.feature
Run with Allure Reporting
To generate an Allure report, first run the tests and generate report data:

bash
Copy code
pytest --alluredir=allure-results
Then serve the report locally:

bash
Copy code
allure serve allure-results
Writing Your Own Feature Files
Example Feature File (checkout.feature):
gherkin
Copy code
Feature: Checkout an item

  Scenario: Checkout a single item
    Given the user is on the login page
    When the user logs in with valid credentials
    And the user adds an item to the cart
    And the user proceeds to the checkout page
    And the user fills in the checkout details
    Then the user should complete the checkout successfully
Place all feature files in the features/ directory.

Step Definitions
The step definitions should be placed in the steps/ directory. Each step in the feature file maps to a Python function in the step definition file (e.g., checkout_steps.py).

Example Step Definitions (checkout_steps.py):
python
Copy code
import pytest
from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

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
    checkout_page.complete_checkout("John", "Doe", "12345")

@then("the user should complete the checkout successfully")
def verify_checkout_complete(browser):
    assert browser.locator("text=THANK YOU FOR YOUR ORDER").is_visible()
Continuous Integration (CI/CD)
GitHub Actions Configuration
The project includes a GitHub Actions configuration to run tests automatically on every push or pull request.

Sample CI Configuration (ci.yml):
yaml
Copy code
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
Running Tests in Parallel
You can run tests in parallel using the pytest-xdist plugin.

Install the Plugin:
bash
Copy code
pip install pytest-xdist
Run Tests in Parallel:
bash
Copy code
pytest -n <number_of_processes>
For example, to run 4 parallel processes:

bash
Copy code
pytest -n 4
Code Quality (Optional)
For JavaScript/TypeScript files, you can integrate ESLint. For Python files, consider using flake8.

Example .eslintrc.js Configuration:
js
Copy code
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
