<div>
<div>Playwright E2E Test Suite with BDD (Cucumber)</div>
<div>Project Overview</div>
<div>This project is an end-to-end test automation suite for the "SauceDemo" website (https://www.saucedemo.com/v1/), developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.</div>
<br />
<div>Key features include:</div>
<br />
<div>Page Object Model (POM) for scalable and maintainable test automation.</div>
<div>Behavior Driven Development (BDD) using pytest-bdd for human-readable tests.</div>
<div>Integration with GitHub Actions for Continuous Integration (CI).</div>
<div>Allure Reporting for test results.</div>
<div>Scenarios Covered:</div>
<div>User login</div>
<div>Adding items to the cart</div>
<div>Verifying cart contents</div>
<div>Completing the checkout process</div>
<div>Project Structure</div>
<div>plaintext</div>
<br />
<div>playwright-test-suite/</div>
<div>├── features/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Gherkin feature files for BDD</div>
<div>│ &nbsp; ├── checkout.feature &nbsp; &nbsp; &nbsp;# Feature file for the checkout process</div>
<div>├── steps/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Step definition files for feature steps</div>
<div>│ &nbsp; ├── checkout_steps.py &nbsp; &nbsp; # Step definitions for the checkout feature</div>
<div>├── pages/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Page Object Model classes</div>
<div>│ &nbsp; ├── base_page.py &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# BasePage class for shared methods</div>
<div>│ &nbsp; ├── login_page.py &nbsp; &nbsp; &nbsp; &nbsp; # Page class for login functionality</div>
<div>│ &nbsp; ├── inventory_page.py &nbsp; &nbsp; # Page class for inventory actions</div>
<div>│ &nbsp; ├── cart_page.py &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Page class for cart actions</div>
<div>│ &nbsp; └── checkout_page.py &nbsp; &nbsp; &nbsp;# Page class for the checkout process</div>
<div>├── tests/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Optional: Additional test scripts</div>
<div>│ &nbsp; └── test_checkout.py &nbsp; &nbsp; &nbsp;# Example standalone test without BDD</div>
<div>├── .github/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # GitHub Actions CI configuration</div>
<div>│ &nbsp; └── workflows/</div>
<div>│ &nbsp; &nbsp; &nbsp; └── ci.yml &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# CI configuration to run tests on push</div>
<div>├── allure-results/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Directory for storing Allure reports</div>
<div>├── README.md &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # This README file</div>
<div>├── pytest.ini &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# pytest configuration file</div>
<div>├── requirements.txt &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Python dependencies</div>
<div>└── conftest.py &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Pytest configuration for Playwright</div>
<div>Prerequisites</div>
<div>Ensure that the following tools are installed on your system:</div>
<br />
<div>Python 3.7+</div>
<div>Node.js (for Playwright dependencies)</div>
<div>pip (Python package manager)</div>
<div>Install Playwright&rsquo;s browser binaries:</div>
<br /><br /><br />
<div>playwright install</div>
<div>Installation</div>
<div>Clone the repository:</div>
<br /><br /><br />
<div>git clone &lt;repository-url&gt;</div>
<div>cd playwright-test-suite</div>
<div>Set up a virtual environment:</div>
<br /><br />
<div>#On macOS/Linux:</div>
<div>python3 -m venv venv</div>
<div>source venv/bin/activate</div>
<br /><br />
<div>#On Windows:</div>
<div>python -m venv venv</div>
<div>venv\Scripts\activate</div>
<br /><br />
<div>#Install dependencies:</div>
<br />
<div>pip install -r requirements.txt</div>
<div>Install Playwright browsers:</div>
<br /><br /><br />
<div>#playwright install</div>
<br />
<div>Running the Test Suite</div>
<div>Run all tests with BDD:</div>
<br /><br />
<div>#To run the full test suite using BDD and Cucumber (via pytest-bdd):</div>
<br />
<div>pytest -v</div>
<br /><br />
<div>Run specific feature file:</div>
<div>To run a specific feature file, use:</div>
<br />
<div>pytest -v features/checkout.feature</div>
<br /><br />
<div>#Run with Allure Reporting:</div>
<div>To generate an Allure report:</div>
<br />
<div>Run the tests and generate the report data:</div>
<br />
<div>pytest --alluredir=allure-results</div>
<br />
<div>#Serve the report in a local web server:</div>
<div>allure serve allure-results</div>
<br /><br />
<div>#Writing Your Own Feature Files</div>
<div>Example Feature File (checkout.feature):</div>
<div>gherkin</div>
<br />
<div>Feature: Checkout an item</div>
<br />
<div>&nbsp; Scenario: Checkout a single item</div>
<div>&nbsp; &nbsp; Given the user is on the login page</div>
<div>&nbsp; &nbsp; When the user logs in with valid credentials</div>
<div>&nbsp; &nbsp; And the user adds an item to the cart</div>
<div>&nbsp; &nbsp; And the user proceeds to the checkout page</div>
<div>&nbsp; &nbsp; And the user fills in the checkout details</div>
<div>&nbsp; &nbsp; Then the user should complete the checkout successfully</div>
<div>Place all feature files in the features/ directory.</div>
<br />
<div>#Step Definitions</div>
<div>The corresponding step definitions should be placed in the steps/ directory. Each step in the feature file will map to a Python function in a step definition file (e.g., checkout_steps.py).</div>
<br /><br /><br />
<div>import pytest</div>
<div>from pytest_bdd import given, when, then</div>
<div>from pages.login_page import LoginPage</div>
<div>from pages.inventory_page import InventoryPage</div>
<div>from pages.cart_page import CartPage</div>
<div>from pages.checkout_page import CheckoutPage</div>
<br />
<div># Fixture for browser setup</div>
<div>@pytest.fixture</div>
<div>def browser(playwright):</div>
<div>&nbsp; &nbsp; browser = playwright.chromium.launch(headless=False)</div>
<div>&nbsp; &nbsp; context = browser.new_context()</div>
<div>&nbsp; &nbsp; page = context.new_page()</div>
<div>&nbsp; &nbsp; yield page</div>
<div>&nbsp; &nbsp; context.close()</div>
<div>&nbsp; &nbsp; browser.close()</div>
<br />
<div># Step Definitions</div>
<div>@given("the user is on the login page")</div>
<div>def navigate_to_login_page(browser):</div>
<div>&nbsp; &nbsp; login_page = LoginPage(browser)</div>
<div>&nbsp; &nbsp; login_page.goto("https://www.saucedemo.com/v1/")</div>
<br />
<div>@when("the user logs in with valid credentials")</div>
<div>def user_logs_in(browser):</div>
<div>&nbsp; &nbsp; login_page = LoginPage(browser)</div>
<div>&nbsp; &nbsp; login_page.login("standard_user", "secret_sauce")</div>
<br />
<div>@when("the user adds an item to the cart")</div>
<div>def add_item_to_cart(browser):</div>
<div>&nbsp; &nbsp; inventory_page = InventoryPage(browser)</div>
<div>&nbsp; &nbsp; inventory_page.add_item_to_cart("Sauce Labs Backpack")</div>
<div>&nbsp; &nbsp; inventory_page.navigate_to_cart()</div>
<br />
<div>@when("the user proceeds to the checkout page")</div>
<div>def proceed_to_checkout(browser):</div>
<div>&nbsp; &nbsp; cart_page = CartPage(browser)</div>
<div>&nbsp; &nbsp; cart_page.proceed_to_checkout()</div>
<br />
<div>@when("the user fills in the checkout details")</div>
<div>def fill_checkout_details(browser):</div>
<div>&nbsp; &nbsp; checkout_page = CheckoutPage(browser)</div>
<div>&nbsp; &nbsp; checkout_page.complete_checkout("Easir", "Maruf", "1234")</div>
<br />
<div>@then("the user should complete the checkout successfully")</div>
<div>def verify_checkout_complete(browser):</div>
<div>&nbsp; &nbsp; assert browser.locator("text=THANK YOU FOR YOUR ORDER").is_visible()</div>
<div>GitHub Actions (CI/CD)</div>
<div>The project includes a GitHub Actions configuration (.github/workflows/ci.yml) to automate the test execution on every push to the repository.</div>
<br />
<div>To enable this:</div>
<br />
<div>Push your project to GitHub.</div>
<div>Edit .github/workflows/ci.yml to adjust your Playwright setup or dependencies if necessary.</div>
<div>The workflow will automatically run tests for every push or pull request.</div>
<div>Sample CI Configuration (ci.yml):</div>
<div>yaml</div>
<br />
<div>name: Playwright Tests</div>
<br />
<div>on:</div>
<div>&nbsp; push:</div>
<div>&nbsp; &nbsp; branches:</div>
<div>&nbsp; &nbsp; &nbsp; - main</div>
<div>&nbsp; pull_request:</div>
<div>&nbsp; &nbsp; branches:</div>
<div>&nbsp; &nbsp; &nbsp; - main</div>
<br />
<div>jobs:</div>
<div>&nbsp; test:</div>
<div>&nbsp; &nbsp; runs-on: ubuntu-latest</div>
<br />
<div>&nbsp; &nbsp; steps:</div>
<div>&nbsp; &nbsp; - uses: actions/checkout@v2</div>
<div>&nbsp; &nbsp; - name: Set up Python</div>
<div>&nbsp; &nbsp; &nbsp; uses: actions/setup-python@v2</div>
<div>&nbsp; &nbsp; &nbsp; with:</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; python-version: '3.8'</div>
<div>&nbsp; &nbsp; - name: Install dependencies</div>
<div>&nbsp; &nbsp; &nbsp; run: |</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; python -m venv venv</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; source venv/bin/activate</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; pip install -r requirements.txt</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; playwright install</div>
<div>&nbsp; &nbsp; - name: Run Playwright tests</div>
<div>&nbsp; &nbsp; &nbsp; run: |</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; source venv/bin/activate</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; pytest --headed --alluredir=allure-results</div>
<div>&nbsp; &nbsp; - name: Upload Allure results</div>
<div>&nbsp; &nbsp; &nbsp; uses: actions/upload-artifact@v2</div>
<div>&nbsp; &nbsp; &nbsp; with:</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; name: allure-results</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; path: allure-results</div>
<br /><br /><br />
<div>#Running Tests in Parallel</div>
<div>To run tests in parallel, you can use the pytest-xdist plugin:</div>
<br /><br /><br />
<div>pip install pytest-xdist</div>
<div>pytest -n &lt;number_of_processes&gt;</div>
<div>For example:</div>
<br /><br /><br />
<div>pytest -n 4 &nbsp;# Runs the tests in parallel using 4 processes</div>
<div>Code Quality (Optional)</div>
<div>For code quality, you can integrate a linter like ESLint for JavaScript/TypeScript files or flake8 for Python files.</div>
<br />
<div>#Example .eslintrc.js configuration for Playwright projects:</div>
<br /><br />
<div>module.exports = {</div>
<div>&nbsp; &nbsp; "env": {</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "browser": true,</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "es2021": true</div>
<div>&nbsp; &nbsp; },</div>
<div>&nbsp; &nbsp; "extends": "eslint:recommended",</div>
<div>&nbsp; &nbsp; "parserOptions": {</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "ecmaVersion": 12,</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "sourceType": "module"</div>
<div>&nbsp; &nbsp; },</div>
<div>&nbsp; &nbsp; "rules": {</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "no-unused-vars": "warn",</div>
<div>&nbsp; &nbsp; &nbsp; &nbsp; "no-console": "off"</div>
<div>&nbsp; &nbsp; }</div>
<div>};</div>
<div>Contributors</div>
<div>@khause</div>
<div>@Tosinfamzy</div>
<div>@ChrisSargent</div>
<div>License</div>
<div>This project is licensed under the MIT License.</div>
</div>
