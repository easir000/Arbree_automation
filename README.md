<p>Playwright E2E Test Suite with BDD (Cucumber) Project Overview This project is an end-to-end test automation suite for the &quot;SauceDemo&quot; website (https://www.saucedemo.com/v1/), developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.</p>

<p>Key features include:</p>

<p>Page Object Model (POM) for scalable and maintainable test automation. Behavior Driven Development (BDD) using pytest-bdd for human-readable tests. Integration with GitHub Actions for Continuous Integration (CI). Allure Reporting for test results. Scenarios Covered: User login Adding items to the cart Verifying cart contents Completing the checkout process Project Structure plaintext</p>

<p>playwright-test-suite/ &#9500;&#9472;&#9472; features/ # Gherkin feature files for BDD &#9474; &#9500;&#9472;&#9472; checkout.feature # Feature file for the checkout process &#9500;&#9472;&#9472; steps/ # Step definition files for feature steps &#9474; &#9500;&#9472;&#9472; checkout_steps.py # Step definitions for the checkout feature &#9500;&#9472;&#9472; pages/ # Page Object Model classes &#9474; &#9500;&#9472;&#9472; base_page.py # BasePage class for shared methods &#9474; &#9500;&#9472;&#9472; login_page.py # Page class for login functionality &#9474; &#9500;&#9472;&#9472; inventory_page.py # Page class for inventory actions &#9474; &#9500;&#9472;&#9472; cart_page.py # Page class for cart actions &#9474; &#9492;&#9472;&#9472; checkout_page.py # Page class for the checkout process &#9500;&#9472;&#9472; tests/ # Optional: Additional test scripts &#9474; &#9492;&#9472;&#9472; test_checkout.py # Example standalone test without BDD &#9500;&#9472;&#9472; .github/ # GitHub Actions CI configuration &#9474; &#9492;&#9472;&#9472; workflows/ &#9474; &#9492;&#9472;&#9472; ci.yml # CI configuration to run tests on push &#9500;&#9472;&#9472; allure-results/ # Directory for storing Allure reports &#9500;&#9472;&#9472; README.md # This README file &#9500;&#9472;&#9472; pytest.ini # pytest configuration file &#9500;&#9472;&#9472; requirements.txt # Python dependencies &#9492;&#9472;&#9472; conftest.py # Pytest configuration for Playwright Prerequisites Ensure that the following tools are installed on your system:</p>

<p>Python 3.7+ Node.js (for Playwright dependencies) pip (Python package manager) Install Playwright&rsquo;s browser binaries:</p>

<p>playwright install Installation Clone the repository:</p>

<p></p>

<p>git clone <repository-url> cd playwright-test-suite Set up a virtual environment:</p>

<p> #On macOS/Linux: python3 -m venv venv source venv/bin/activate</p>

<p> #On Windows: python -m venv venv venv\Scripts\activate</p>

<p> #Install dependencies:</p>

<p>pip install -r requirements.txt Install Playwright browsers:</p>

<p></p>

<p>#playwright install</p>

<p>Running the Test Suite Run all tests with BDD:</p>

<p> #To run the full test suite using BDD and Cucumber (via pytest-bdd):</p>

<p>pytest -v</p>

<p> Run specific feature file: To run a specific feature file, use:</p>

<p>pytest -v features/checkout.feature</p>

<p> #Run with Allure Reporting: To generate an Allure report:</p>

<p>Run the tests and generate the report data:</p>

<p>pytest --alluredir=allure-results</p>

<p>#Serve the report in a local web server: allure serve allure-results</p>

<p> #Writing Your Own Feature Files Example Feature File (checkout.feature): gherkin</p>

<p>Feature: Checkout an item</p>

<p> Scenario: Checkout a single item  Given the user is on the login page  When the user logs in with valid credentials  And the user adds an item to the cart  And the user proceeds to the checkout page  And the user fills in the checkout details  Then the user should complete the checkout successfully Place all feature files in the features/ directory.</p>

<p>#Step Definitions The corresponding step definitions should be placed in the steps/ directory. Each step in the feature file will map to a Python function in a step definition file (e.g., checkout_steps.py).</p>

<p></p>

<p>import pytest from pytest_bdd import given, when, then from pages.login_page import LoginPage from pages.inventory_page import InventoryPage from pages.cart_page import CartPage from pages.checkout_page import CheckoutPage</p>

<p># Fixture for browser setup @pytest.fixture def browser(playwright):  browser = playwright.chromium.launch(headless=False)  context = browser.new_context()  page = context.new_page()  yield page  context.close()  browser.close()</p>

<p># Step Definitions @given(&quot;the user is on the login page&quot;) def navigate_to_login_page(browser):  login_page = LoginPage(browser)  login_page.goto(&quot;https://www.saucedemo.com/v1/&quot;)</p>

<p>@when(&quot;the user logs in with valid credentials&quot;) def user_logs_in(browser):  login_page = LoginPage(browser)  login_page.login(&quot;standard_user&quot;, &quot;secret_sauce&quot;)</p>

<p>@when(&quot;the user adds an item to the cart&quot;) def add_item_to_cart(browser):  inventory_page = InventoryPage(browser)  inventory_page.add_item_to_cart(&quot;Sauce Labs Backpack&quot;)  inventory_page.navigate_to_cart()</p>

<p>@when(&quot;the user proceeds to the checkout page&quot;) def proceed_to_checkout(browser):  cart_page = CartPage(browser)  cart_page.proceed_to_checkout()</p>

<p>@when(&quot;the user fills in the checkout details&quot;) def fill_checkout_details(browser):  checkout_page = CheckoutPage(browser)  checkout_page.complete_checkout(&quot;Easir&quot;, &quot;Maruf&quot;, &quot;1234&quot;)</p>

<p>@then(&quot;the user should complete the checkout successfully&quot;) def verify_checkout_complete(browser):  assert browser.locator(&quot;text=THANK YOU FOR YOUR ORDER&quot;).is_visible() GitHub Actions (CI/CD) The project includes a GitHub Actions configuration (.github/workflows/ci.yml) to automate the test execution on every push to the repository.</p>

<p>To enable this:</p>

<p>Push your project to GitHub. Edit .github/workflows/ci.yml to adjust your Playwright setup or dependencies if necessary. The workflow will automatically run tests for every push or pull request. Sample CI Configuration (ci.yml): yaml</p>

<p>name: Playwright Tests</p>

<p>on:  push:  branches:  - main  pull_request:  branches:  - main</p>

<p>jobs:  test:  runs-on: ubuntu-latest</p>

<p> steps:  - uses: actions/checkout@v2  - name: Set up Python  uses: actions/setup-python@v2  with:  python-version: '3.8'  - name: Install dependencies  run: |  python -m venv venv  source venv/bin/activate  pip install -r requirements.txt  playwright install  - name: Run Playwright tests  run: |  source venv/bin/activate  pytest --headed --alluredir=allure-results  - name: Upload Allure results  uses: actions/upload-artifact@v2  with:  name: allure-results  path: allure-results</p>

<p></p>

<p>#Running Tests in Parallel To run tests in parallel, you can use the pytest-xdist plugin:</p>

<p></p>

<p>pip install pytest-xdist pytest -n <number_of_processes> For example:</p>

<p></p>

<p>pytest -n 4 # Runs the tests in parallel using 4 processes Code Quality (Optional) For code quality, you can integrate a linter like ESLint for JavaScript/TypeScript files or flake8 for Python files.</p>

<p>#Example .eslintrc.js configuration for Playwright projects:</p>

<p> module.exports = {  &quot;env&quot;: {  &quot;browser&quot;: true,  &quot;es2021&quot;: true  },  &quot;extends&quot;: &quot;eslint:recommended&quot;,  &quot;parserOptions&quot;: {  &quot;ecmaVersion&quot;: 12,  &quot;sourceType&quot;: &quot;module&quot;  },  &quot;rules&quot;: {  &quot;no-unused-vars&quot;: &quot;warn&quot;,  &quot;no-console&quot;: &quot;off&quot;  } }; Contributors @khause @Tosinfamzy @ChrisSargent License This project is licensed under the MIT License.</p>
