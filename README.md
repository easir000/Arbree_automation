<h1>Playwright E2E Test Suite with BDD (Cucumber)</h1>
<h2>Project Overview</h2>
<p>This project is an end-to-end test automation suite for the "SauceDemo" website (<a href="https://www.saucedemo.com/v1/" target="_new" rel="noopener">https://www.saucedemo.com/v1/</a>), developed using Playwright in Python. The test suite follows the <strong>Page Object Model (POM)</strong> design pattern and integrates <strong>Behavioral Driven Development (BDD)</strong> with <strong>Cucumber</strong> using <code>pytest-bdd</code>.</p>
<p>Key features include:</p>
<ul>
<li><strong>Page Object Model (POM)</strong> for scalable and maintainable test automation.</li>
<li><strong>Behavior Driven Development (BDD)</strong> using <code>pytest-bdd</code> for human-readable tests.</li>
<li>Integration with GitHub Actions for <strong>Continuous Integration (CI)</strong>.</li>
<li><strong>Allure Reporting</strong> for test results.</li>
</ul>
<h3>Scenarios Covered:</h3>
<ol>
<li>User login</li>
<li>Adding items to the cart</li>
<li>Verifying cart contents</li>
<li>Completing the checkout process</li>
</ol>
<h2>Project Structure</h2>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">plaintext</div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-plaintext">playwright-test-suite/ ├── features/ #  feature files for BDD │ ├── checkout.feature # Feature file for the checkout process ├── steps/ # Step definition files for feature steps │ ├── checkout_steps.py # Step definitions for the checkout feature ├── pages/ # Page Object Model classes │ ├── base_page.py # BasePage class for shared methods │ ├── login_page.py # Page class for login functionality │ ├── inventory_page.py # Page class for inventory actions │ ├── cart_page.py # Page class for cart actions │ └── checkout_page.py # Page class for the checkout process ├── tests/ # Optional: Additional test scripts │ └── test_checkout.py # Example standalone test without BDD ├── .github/ # GitHub Actions CI configuration │ └── workflows/ │ └── ci.yml # CI configuration to run tests on push ├── allure-results/ # Directory for storing Allure reports ├── README.md # This README file ├── pytest.ini # pytest configuration file ├── requirements.txt # Python dependencies └── conftest.py # Pytest configuration for Playwright </code></div>
</div>
<h2>Prerequisites</h2>
<p>Ensure that the following tools are installed on your system:</p>
<ul>
<li><strong>Python 3.7+</strong></li>
<li><strong>Node.js</strong> (for Playwright dependencies)</li>
<li><strong>pip</strong> (Python package manager)</li>
</ul>
<p>Install Playwright&rsquo;s browser binaries:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">playwright install </code></div>
</div>
<h2>Installation</h2>
<ol>
<li>
<p><strong>Clone the repository</strong>:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">git <span class="hljs-built_in">clone</span> &lt;repository-url&gt; <span class="hljs-built_in">cd</span> playwright-test-suite </code></div>
</div>
</li>
<li>
<p><strong>Set up a virtual environment</strong>:</p>
<p>On macOS/Linux:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">python3 -m venv venv <span class="hljs-built_in">source</span> venv/bin/activate </code></div>
</div>
<p>On Windows:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">python -m venv venv venv\Scripts\activate </code></div>
</div>
</li>
<li>
<p><strong>Install dependencies</strong>:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pip install -r requirements.txt </code></div>
</div>
</li>
<li>
<p><strong>Install Playwright browsers</strong>:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">playwright install </code></div>
</div>
</li>
</ol>
<h2>Running the Test Suite</h2>
<h3>Run all tests with BDD:</h3>
<p>To run the full test suite using BDD and Cucumber (via <code>pytest-bdd</code>):</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pytest -v </code></div>
</div>
<h3>Run specific feature file:</h3>
<p>To run a specific feature file, use:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pytest -v features/checkout.feature </code></div>
</div>
<h3>Run with Allure Reporting:</h3>
<p>To generate an Allure report:</p>
<ol>
<li>
<p>Run the tests and generate the report data:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pytest --alluredir=allure-results </code></div>
</div>
</li>
<li>
<p>Serve the report in a local web server:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">allure serve allure-results </code></div>
</div>
</li>
</ol>
<h2>Writing Your Own Feature Files</h2>
<h3>Example Feature File (<code>checkout.feature</code>):</h3>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">Feature: Checkout an item Scenario: Checkout a single item Given the user is on the login page When the user logs in with valid credentials And the user adds an item to the cart And the user proceeds to the checkout page And the user fills in the checkout details Then the user should complete the checkout successfully </code></div>
</div>
<p>Place all feature files in the <code>features/</code> directory.</p>
<h3>Step Definitions</h3>
<p>The corresponding step definitions should be placed in the <code>steps/</code> directory. Each step in the feature file will map to a Python function in a step definition file (e.g., <code>checkout_steps.py</code>).</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><span class="hljs-keyword">import</span> pytest <span class="hljs-keyword">from</span> pytest_bdd <span class="hljs-keyword">import</span> given, when, then <span class="hljs-keyword">from</span> pages.login_page <span class="hljs-keyword">import</span> LoginPage <span class="hljs-keyword">from</span> pages.inventory_page <span class="hljs-keyword">import</span> InventoryPage <span class="hljs-keyword">from</span> pages.cart_page <span class="hljs-keyword">import</span> CartPage <span class="hljs-keyword">from</span> pages.checkout_page <span class="hljs-keyword">import</span> CheckoutPage <span class="hljs-comment"># Fixture for browser setup</span> <span class="hljs-meta">@pytest.fixture</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">browser</span>(<span class="hljs-params">playwright</span>): browser = playwright.chromium.launch(headless=<span class="hljs-literal">False</span>) context = browser.new_context() page = context.new_page() <span class="hljs-keyword">yield</span> page context.close() browser.close() <span class="hljs-comment"># Step Definitions</span> <span class="hljs-meta">@given(<span class="hljs-params"><span class="hljs-string">"the user is on the login page"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">navigate_to_login_page</span>(<span class="hljs-params">browser</span>): login_page = LoginPage(browser) login_page.goto(<span class="hljs-string">"https://www.saucedemo.com/v1/"</span>) <span class="hljs-meta">@when(<span class="hljs-params"><span class="hljs-string">"the user logs in with valid credentials"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">user_logs_in</span>(<span class="hljs-params">browser</span>): login_page = LoginPage(browser) login_page.login(<span class="hljs-string">"standard_user"</span>, <span class="hljs-string">"secret_sauce"</span>) <span class="hljs-meta">@when(<span class="hljs-params"><span class="hljs-string">"the user adds an item to the cart"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">add_item_to_cart</span>(<span class="hljs-params">browser</span>): inventory_page = InventoryPage(browser) inventory_page.add_item_to_cart(<span class="hljs-string">"Sauce Labs Backpack"</span>) inventory_page.navigate_to_cart() <span class="hljs-meta">@when(<span class="hljs-params"><span class="hljs-string">"the user proceeds to the checkout page"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">proceed_to_checkout</span>(<span class="hljs-params">browser</span>): cart_page = CartPage(browser) cart_page.proceed_to_checkout() <span class="hljs-meta">@when(<span class="hljs-params"><span class="hljs-string">"the user fills in the checkout details"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">fill_checkout_details</span>(<span class="hljs-params">browser</span>): checkout_page = CheckoutPage(browser) checkout_page.complete_checkout(<span class="hljs-string">"John"</span>, <span class="hljs-string">"Doe"</span>, <span class="hljs-string">"12345"</span>) <span class="hljs-meta">@then(<span class="hljs-params"><span class="hljs-string">"the user should complete the checkout successfully"</span></span>)</span> <span class="hljs-keyword">def</span> <span class="hljs-title function_">verify_checkout_complete</span>(<span class="hljs-params">browser</span>): <span class="hljs-keyword">assert</span> browser.locator(<span class="hljs-string">"text=THANK YOU FOR YOUR ORDER"</span>).is_visible() </code></div>
</div>
<h2>GitHub Actions (CI/CD)</h2>
<p>The project includes a GitHub Actions configuration (<code>.github/workflows/ci.yml</code>) to automate the test execution on every push to the repository.</p>
<p>To enable this:</p>
<ol>
<li>Push your project to GitHub.</li>
<li>Edit <code>.github/workflows/ci.yml</code> to adjust your Playwright setup or dependencies if necessary.</li>
<li>The workflow will automatically run tests for every push or pull request.</li>
</ol>
<h3>Sample CI Configuration (<code>ci.yml</code>):</h3>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">yaml</div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">Playwright</span> <span class="hljs-string">Tests</span> <span class="hljs-attr">on:</span> <span class="hljs-attr">push:</span> <span class="hljs-attr">branches:</span> <span class="hljs-bullet">-</span> <span class="hljs-string">main</span> <span class="hljs-attr">pull_request:</span> <span class="hljs-attr">branches:</span> <span class="hljs-bullet">-</span> <span class="hljs-string">main</span> <span class="hljs-attr">jobs:</span> <span class="hljs-attr">test:</span> <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span> <span class="hljs-attr">steps:</span> <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span> <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Set</span> <span class="hljs-string">up</span> <span class="hljs-string">Python</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-python@v2</span> <span class="hljs-attr">with:</span> <span class="hljs-attr">python-version:</span> <span class="hljs-string">'3.8'</span> <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span> <span class="hljs-attr">run:</span> <span class="hljs-string">| python -m venv venv source venv/bin/activate pip install -r requirements.txt playwright install </span> <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Run</span> <span class="hljs-string">Playwright</span> <span class="hljs-string">tests</span> <span class="hljs-attr">run:</span> <span class="hljs-string">| source venv/bin/activate pytest --headed --alluredir=allure-results </span> <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Upload</span> <span class="hljs-string">Allure</span> <span class="hljs-string">results</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/upload-artifact@v2</span> <span class="hljs-attr">with:</span> <span class="hljs-attr">name:</span> <span class="hljs-string">allure-results</span> <span class="hljs-attr">path:</span> <span class="hljs-string">allure-results</span> </code></div>
</div>
<h2>Running Tests in Parallel</h2>
<p>To run tests in parallel, you can use the <code>pytest-xdist</code> plugin:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pip install pytest-xdist pytest -n &lt;number_of_processes&gt; </code></div>
</div>
<p>For example:</p>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">pytest -n 4 <span class="hljs-comment"># Runs the tests in parallel using 4 processes</span> </code></div>
</div>
<h2>Code Quality (Optional)</h2>
<p>For code quality, you can integrate a linter like <code>ESLint</code> for JavaScript/TypeScript files or <code>flake8</code> for Python files.</p>
<h3>Example <code>.eslintrc.js</code> configuration for Playwright projects:</h3>
<div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative">
<div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">javascript</div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"></button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-javascript"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = { <span class="hljs-string">"env"</span>: { <span class="hljs-string">"browser"</span>: <span class="hljs-literal">true</span>, <span class="hljs-string">"es2021"</span>: <span class="hljs-literal">true</span> }, <span class="hljs-string">"extends"</span>: <span class="hljs-string">"eslint:recommended"</span>, <span class="hljs-string">"parserOptions"</span>: { <span class="hljs-string">"ecmaVersion"</span>: <span class="hljs-number">12</span>, <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span> }, <span class="hljs-string">"rules"</span>: { <span class="hljs-string">"no-unused-vars"</span>: <span class="hljs-string">"warn"</span>, <span class="hljs-string">"no-console"</span>: <span class="hljs-string">"off"</span> } }; </code></div>
</div>
<h2>Contributors</h2>
<ul>
<li>@khause</li>
<li>@Tosinfamzy</li>
<li>@ChrisSargent</li>
</ul>
<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
<p>&nbsp;</p>
