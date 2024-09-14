<h1>Playwright E2E Test Suite with BDD (Cucumber)</h1>
<h2>Project Overview</h2>
<p>This project is an end-to-end test automation suite for the <a rel="noopener" target="_new" href="https://www.saucedemo.com/v1/">SauceDemo website</a>, developed using Playwright in Python. The test suite follows the Page Object Model (POM) design pattern and integrates Behavioral Driven Development (BDD) with Cucumber using pytest-bdd.</p>
<h3>Key Features</h3>
<ul>
    <li><strong>Page Object Model (POM)</strong>: A scalable and maintainable design pattern for UI tests.</li>
    <li><strong>Behavior Driven Development (BDD)</strong>: Human-readable test scenarios using <code>pytest-bdd</code>.</li>
    <li><strong>Continuous Integration (CI)</strong>: GitHub Actions integration for automatic test execution on push.</li>
    <li><strong>Allure Reporting</strong>: Generate test reports for visual insights.</li>
</ul>
<h3>Scenarios Covered</h3>
<ol>
    <li>User login.</li>
    <li>Adding items to the cart.</li>
    <li>Verifying cart contents.</li>
    <li>Completing the checkout process.</li>
</ol>
<hr>
<h2>Project Structure</h2>
<pre><div><div>plaintext</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>playwright-test-suite/
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
</code></div></div></pre>
<hr>
<h2>Prerequisites</h2>
<p>Ensure that the following tools are installed on your system:</p>
<ul>
    <li><strong>Python 3.7+</strong></li>
    <li><strong>Node.js</strong> (for Playwright dependencies)</li>
    <li><strong>pip</strong> (Python package manager)</li>
</ul>
<h3>Install Playwright Browsers</h3>
<p>Before running the tests, install the Playwright browsers:</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>playwright install
</code></div></div></pre>
<hr>
<h2>Installation</h2>
<h3>Step 1: Clone the Repository</h3>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>git clone &lt;repository-url&gt;
cd playwright-test-suite
</code></div></div></pre>
<h3>Step 2: Set Up a Virtual Environment</h3>
<h4>On macOS/Linux:</h4>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>python3 -m venv venv
source venv/bin/activate
</code></div></div></pre>
<h4>On Windows:</h4>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>python -m venv venv
venv\Scripts\activate
</code></div></div></pre>
<h3>Step 3: Install Dependencies</h3>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pip install -r requirements.txt
</code></div></div></pre>
<hr>
<h2>Running the Test Suite</h2>
<h3>Run All Tests with BDD</h3>
<p>To run the full test suite using BDD with pytest-bdd:</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pytest -v
</code></div></div></pre>
<h3>Run a Specific Feature File</h3>
<p>To run a specific feature file (e.g., <code>checkout.feature</code>):</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pytest -v features/checkout.feature
</code></div></div></pre>
<h3>Run with Allure Reporting</h3>
<p>To generate an Allure report, first run the tests and generate report data:</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pytest --alluredir=allure-results
</code></div></div></pre>
<p>Then serve the report locally:</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>allure serve allure-results
</code></div></div></pre>
<hr>
<h2>Writing Your Own Feature Files</h2>
<h3>Example Feature File (<code>checkout.feature</code>):</h3>
<pre><div><div>gherkin</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>Feature: Checkout an item

  Scenario: Checkout a single item
    Given the user is on the login page
    When the user logs in with valid credentials
    And the user adds an item to the cart
    And the user proceeds to the checkout page
    And the user fills in the checkout details
    Then the user should complete the checkout successfully
</code></div></div></pre>
<p>Place all feature files in the <code>features/</code> directory.</p>
<hr>
<h2>Step Definitions</h2>
<p>The step definitions should be placed in the <code>steps/</code> directory. Each step in the feature file maps to a Python function in the step definition file (e.g., <code>checkout_steps.py</code>).</p>
<h3>Example Step Definitions (<code>checkout_steps.py</code>):</h3>
<pre><div><div>python</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>import pytest
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

@given(&quot;the user is on the login page&quot;)
def navigate_to_login_page(browser):
    login_page = LoginPage(browser)
    login_page.goto(&quot;https://www.saucedemo.com/v1/&quot;)

@when(&quot;the user logs in with valid credentials&quot;)
def user_logs_in(browser):
    login_page = LoginPage(browser)
    login_page.login(&quot;standard_user&quot;, &quot;secret_sauce&quot;)

@when(&quot;the user adds an item to the cart&quot;)
def add_item_to_cart(browser):
    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart(&quot;Sauce Labs Backpack&quot;)
    inventory_page.navigate_to_cart()

@when(&quot;the user proceeds to the checkout page&quot;)
def proceed_to_checkout(browser):
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

@when(&quot;the user fills in the checkout details&quot;)
def fill_checkout_details(browser):
    checkout_page = CheckoutPage(browser)
    checkout_page.complete_checkout(&quot;John&quot;, &quot;Doe&quot;, &quot;12345&quot;)

@then(&quot;the user should complete the checkout successfully&quot;)
def verify_checkout_complete(browser):
    assert browser.locator(&quot;text=THANK YOU FOR YOUR ORDER&quot;).is_visible()
</code></div></div></pre>
<hr>
<h2>Continuous Integration (CI/CD)</h2>
<h3>GitHub Actions Configuration</h3>
<p>The project includes a GitHub Actions configuration to run tests automatically on every push or pull request.</p>
<h4>Sample CI Configuration (<code>ci.yml</code>):</h4>
<pre><div><div>yaml</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>name: Playwright Tests

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
        python-version: &apos;3.8&apos;
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
</code></div></div></pre>
<hr>
<h2>Running Tests in Parallel</h2>
<p>You can run tests in parallel using the <code>pytest-xdist</code> plugin.</p>
<h3>Install the Plugin:</h3>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pip install pytest-xdist
</code></div></div></pre>
<h3>Run Tests in Parallel:</h3>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pytest -n &lt;number_of_processes&gt;
</code></div></div></pre>
<p>For example, to run 4 parallel processes:</p>
<pre><div><div>bash</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>pytest -n 4
</code></div></div></pre>
<hr>
<h2>Code Quality (Optional)</h2>
<p>For JavaScript/TypeScript files, you can integrate ESLint. For Python files, consider using <code>flake8</code>.</p>
<h3>Example <code>.eslintrc.js</code> Configuration:</h3>
<pre><div><div>js</div><div><div><div><button><svg width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></div></div></div><div><code>module.exports = {
    &quot;env&quot;: {
        &quot;browser&quot;: true,
        &quot;es2021&quot;: true
    },
    &quot;extends&quot;: &quot;eslint:recommended&quot;,
    &quot;parserOptions&quot;: {
        &quot;ecmaVersion&quot;: 12,
        &quot;sourceType&quot;: &quot;module&quot;
    },
    &quot;rules&quot;: {
        &quot;no-unused-vars&quot;: &quot;warn&quot;,
        &quot;no-console&quot;: &quot;off&quot;
    }
};
</code></div></div></pre>
<hr>
<h2>Contributors</h2>
<ul>
    <li>@khause</li>
    <li>@Tosinfamzy</li>
    <li>@ChrisSargent</li>
</ul>
<hr>
<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
