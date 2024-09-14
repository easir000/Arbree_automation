<p>Playwright E2E Test Suite with BDD (Cucumber) Project Overview This project is an end-to-end test automation suite for the SauceDemo website, developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.</p>

<p>Key Features Page Object Model (POM): A scalable and maintainable design pattern for UI tests. Behavior Driven Development (BDD): Human-readable test scenarios using pytest-bdd. Continuous Integration (CI): GitHub Actions integration for automatic test execution on push. Allure Reporting: Generate test reports for visual insights. Scenarios Covered User login. Adding items to the cart. Verifying cart contents. Completing the checkout process. Project Structure plaintext Copy code playwright-test-suite/ &#9500;&#9472;&#9472; features/ # Gherkin feature files for BDD &#9474; &#9500;&#9472;&#9472; checkout.feature # Feature file for the checkout process &#9500;&#9472;&#9472; steps/ # Step definition files for feature steps &#9474; &#9500;&#9472;&#9472; checkout_steps.py # Step definitions for the checkout feature &#9500;&#9472;&#9472; pages/ # Page Object Model classes &#9474; &#9500;&#9472;&#9472; base_page.py # BasePage class for shared methods &#9474; &#9500;&#9472;&#9472; login_page.py # Page class for login functionality &#9474; &#9500;&#9472;&#9472; inventory_page.py # Page class for inventory actions &#9474; &#9500;&#9472;&#9472; cart_page.py # Page class for cart actions &#9474; &#9492;&#9472;&#9472; checkout_page.py # Page class for the checkout process &#9500;&#9472;&#9472; tests/ # Optional: Additional test scripts &#9474; &#9492;&#9472;&#9472; test_checkout.py # Example standalone test without BDD &#9500;&#9472;&#9472; .github/ # GitHub Actions CI configuration &#9474; &#9492;&#9472;&#9472; workflows/ &#9474; &#9492;&#9472;&#9472; ci.yml # CI configuration to run tests on push &#9500;&#9472;&#9472; allure-results/ # Directory for storing Allure reports &#9500;&#9472;&#9472; README.md # This README file &#9500;&#9472;&#9472; pytest.ini # pytest configuration file &#9500;&#9472;&#9472; requirements.txt # Python dependencies &#9492;&#9472;&#9472; conftest.py # Pytest configuration for Playwright Prerequisites Ensure that the following tools are installed on your system:</p>

<p>Python 3.7+ Node.js (for Playwright dependencies) pip (Python package manager) Install Playwright Browsers Before running the tests, install the Playwright browsers:</p>

<p>bash Copy code playwright install Installation Step 1: Clone the Repository bash Copy code git clone <repository-url> cd playwright-test-suite Step 2: Set Up a Virtual Environment On macOS/Linux: bash Copy code python3 -m venv venv source venv/bin/activate On Windows: bash Copy code python -m venv venv venv\Scripts\activate Step 3: Install Dependencies bash Copy code pip install -r requirements.txt Running the Test Suite Run All Tests with BDD To run the full test suite using BDD with pytest-bdd:</p>

<p>bash Copy code pytest -v Run a Specific Feature File To run a specific feature file (e.g., checkout.feature):</p>

<p>bash Copy code pytest -v features/checkout.feature Run with Allure Reporting To generate an Allure report, first run the tests and generate report data:</p>

<p>bash Copy code pytest --alluredir=allure-results Then serve the report locally:</p>

<p>bash Copy code allure serve allure-results Writing Your Own Feature Files Example Feature File (checkout.feature): gherkin Copy code Feature: Checkout an item</p>

<p> Scenario: Checkout a single item  Given the user is on the login page  When the user logs in with valid credentials  And the user adds an item to the cart  And the user proceeds to the checkout page  And the user fills in the checkout details  Then the user should complete the checkout successfully Place all feature files in the features/ directory.</p>

<p>Step Definitions The step definitions should be placed in the steps/ directory. Each step in the feature file maps to a Python function in the step definition file (e.g., checkout_steps.py).</p>

<p>Example Step Definitions (checkout_steps.py): python Copy code import pytest from pytest_bdd import given, when, then from pages.login_page import LoginPage from pages.inventory_page import InventoryPage from pages.cart_page import CartPage from pages.checkout_page import CheckoutPage</p>

<p>@pytest.fixture def browser(playwright):  browser = playwright.chromium.launch(headless=False)  context = browser.new_context()  page = context.new_page()  yield page  context.close()  browser.close()</p>

<p>@given(&quot;the user is on the login page&quot;) def navigate_to_login_page(browser):  login_page = LoginPage(browser)  login_page.goto(&quot;https://www.saucedemo.com/v1/&quot;)</p>

<p>@when(&quot;the user logs in with valid credentials&quot;) def user_logs_in(browser):  login_page = LoginPage(browser)  login_page.login(&quot;standard_user&quot;, &quot;secret_sauce&quot;)</p>

<p>@when(&quot;the user adds an item to the cart&quot;) def add_item_to_cart(browser):  inventory_page = InventoryPage(browser)  inventory_page.add_item_to_cart(&quot;Sauce Labs Backpack&quot;)  inventory_page.navigate_to_cart()</p>

<p>@when(&quot;the user proceeds to the checkout page&quot;) def proceed_to_checkout(browser):  cart_page = CartPage(browser)  cart_page.proceed_to_checkout()</p>

<p>@when(&quot;the user fills in the checkout details&quot;) def fill_checkout_details(browser):  checkout_page = CheckoutPage(browser)  checkout_page.complete_checkout(&quot;John&quot;, &quot;Doe&quot;, &quot;12345&quot;)</p>

<p>@then(&quot;the user should complete the checkout successfully&quot;) def verify_checkout_complete(browser):  assert browser.locator(&quot;text=THANK YOU FOR YOUR ORDER&quot;).is_visible() Continuous Integration (CI/CD) GitHub Actions Configuration The project includes a GitHub Actions configuration to run tests automatically on every push or pull request.</p>

<p>Sample CI Configuration (ci.yml): yaml Copy code name: Playwright Tests</p>

<p>on:  push:  branches:  - main  pull_request:  branches:  - main</p>

<p>jobs:  test:  runs-on: ubuntu-latest</p>

<p> steps:  - uses: actions/checkout@v2  - name: Set up Python  uses: actions/setup-python@v2  with:  python-version: '3.8'  - name: Install dependencies  run: |  python -m venv venv  source venv/bin/activate  pip install -r requirements.txt  playwright install  - name: Run Playwright tests  run: |  source venv/bin/activate  pytest --headed --alluredir=allure-results  - name: Upload Allure results  uses: actions/upload-artifact@v2  with:  name: allure-results  path: allure-results Running Tests in Parallel You can run tests in parallel using the pytest-xdist plugin.</p>

<p>Install the Plugin: bash Copy code pip install pytest-xdist Run Tests in Parallel: bash Copy code pytest -n <number_of_processes> For example, to run 4 parallel processes:</p>

<p>bash Copy code pytest -n 4 Code Quality (Optional) For JavaScript/TypeScript files, you can integrate ESLint. For Python files, consider using flake8.</p>

<p>Example .eslintrc.js Configuration: js Copy code module.exports = {  &quot;env&quot;: {  &quot;browser&quot;: true,  &quot;es2021&quot;: true  },  &quot;extends&quot;: &quot;eslint:recommended&quot;,  &quot;parserOptions&quot;: {  &quot;ecmaVersion&quot;: 12,  &quot;sourceType&quot;: &quot;module&quot;  },  &quot;rules&quot;: {  &quot;no-unused-vars&quot;: &quot;warn&quot;,  &quot;no-console&quot;: &quot;off&quot;  } }; Contributors @khause @Tosinfamzy @ChrisSargent</p>
