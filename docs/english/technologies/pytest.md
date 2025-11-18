
# Pytest - Python Testing Framework

## What is Pytest?

**Pytest** is a mature, feature-rich testing framework for Python. It makes it easy to write small, readable tests and scales to support complex functional testing.

**Official Documentation**: [https://docs.pytest.org/](https://docs.pytest.org/)

## Summary

Pytest is the test framework powering this automation:
- **Simple syntax** - Write tests as functions with `assert`
- **Powerful fixtures** - Reusable setup/teardown logic
- **Rich ecosystem** - Plugins for reporting, parallel execution, etc.
- **Flexible organization** - Markers, parametrization, discovery

## Pytest vs Other Frameworks

| Framework | Pros | Cons |
|-----------|------|------|
| **Pytest** | Simple, powerful fixtures, plugins | Learning curve for fixtures |
| **unittest** | Built-in, familiar to Java devs | More boilerplate, less flexible |
| **nose2** | Similar to pytest | Less active development |
| **Robot Framework** | Keyword-driven, non-programmers | Verbose, less flexible |

**This framework uses Pytest** for its simplicity, power, and ecosystem.



---

## Why Pytest for Test Automation?

### Advantages

1. **Simple Syntax**
   - Write tests as simple functions
   - No boilerplate code required
   - Readable assertions with `assert`

2. **Powerful Fixtures**
   - Reusable setup/teardown logic
   - Dependency injection
   - Scope control (function, class, module, session)

3. **Rich Plugin Ecosystem**
   - HTML reports, parallel execution, coverage
   - Allure integration, BDD support
   - Extensible architecture

4. **Detailed Failure Reports**
   - Clear assertion introspection
   - Helpful error messages
   - Stack traces with context

5. **Flexible Test Discovery**
   - Automatic test discovery
   - Pattern-based selection
   - Markers for test organization

---

## Core Concepts

### Test Functions

Simple functions starting with `test_`:

```python
def test_addition():
    result = 2 + 2
    assert result == 4
```

### Assertions

Use Python's built-in `assert` statement:

```python
def test_string():
    name = "Python"
    assert name == "Python"
    assert len(name) == 6
    assert name.startswith("Py")
```

**Pytest provides detailed failure messages**:
```
AssertionError: assert 'Python' == 'python'
  - python
  + Python
```

### Fixtures

Reusable setup/teardown logic:

```python
import pytest

@pytest.fixture
def sample_data():
    # Setup
    data = {"name": "Test", "value": 42}
    yield data
    # Teardown (optional)
    print("Cleanup")

def test_with_fixture(sample_data):
    assert sample_data["name"] == "Test"
```

---

## How This Framework Uses Pytest

### 1. Test Structure

Tests are organized in `tests/` directory:

```
tests/
├── __init__.py
├── test_login.py
├── test_account_user.py
├── test_form_submission.py
└── test_search_product.py
```

**Example Test**:
```python
# tests/test_login.py
def test_login_success_if_credentials_present(browser):
    page = LoginPage(browser)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
    assert page.is_redirected_to_account()
```

### 2. Fixtures (`conftest.py`)

Global fixtures defined in `conftest.py`:

```python
# conftest.py
import pytest
from utils.browser_manager import BrowserManager

@pytest.fixture(scope="function")
def browser(request):
    """Provides a WebDriver instance for each test."""
    browser_name = request.config.getoption("--browser", default="chrome")
    manager = BrowserManager(browser=browser_name)
    driver = manager.driver
    
    yield driver  # Test runs here
    
    driver.quit()  # Cleanup after test
```

**Benefits**:
- Automatic browser setup/teardown
- No repetitive code in tests
- Shared across all test files

### 3. Configuration (`pytest.ini`)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    integration: Integration tests
```

### 4. Markers

Organize and filter tests:

```python
import pytest

@pytest.mark.smoke
def test_critical_feature(browser):
    # Critical test
    pass

@pytest.mark.regression
def test_detailed_scenario(browser):
    # Detailed test
    pass
```

**Run specific markers**:
```bash
pytest -m smoke        # Run only smoke tests
pytest -m regression   # Run only regression tests
```

---

## Pytest Features Used in Framework

### Command-Line Options

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Show print statements
pytest -s

# Run specific file
pytest tests/test_login.py

# Run specific test
pytest tests/test_login.py::test_login_success

# Run by pattern
pytest -k login

# Run by marker
pytest -m smoke

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf

# Generate HTML report
pytest --html=report.html --self-contained-html
```

### Custom Command-Line Options

This framework adds `--browser` option:

```python
# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )
```

**Usage**:
```bash
pytest --browser=chrome
pytest --browser=firefox
```

### Parametrization

Run same test with different data:

```python
import pytest

@pytest.mark.parametrize("username,password", [
    ("user1@example.com", "pass1"),
    ("user2@example.com", "pass2"),
    ("user3@example.com", "pass3"),
])
def test_login_multiple_users(browser, username, password):
    page = LoginPage(browser)
    page.login(username, password)
    assert page.is_redirected_to_account()
```

### Fixture Scopes

Control fixture lifecycle:

```python
@pytest.fixture(scope="function")  # Default: new instance per test
def browser_function():
    pass

@pytest.fixture(scope="class")  # Shared across test class
def browser_class():
    pass

@pytest.fixture(scope="module")  # Shared across test file
def browser_module():
    pass

@pytest.fixture(scope="session")  # Shared across entire test session
def browser_session():
    pass
```

**This framework uses `scope="function"`** for test isolation.

---

## Pytest Plugins Used

### pytest-html

Generate HTML test reports:

```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

### allure-pytest

Advanced reporting with Allure:

```bash
pip install allure-pytest
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### pytest-xdist (Optional)

Parallel test execution:

```bash
pip install pytest-xdist
pytest -n 4  # Run with 4 workers
```

---

## Best Practices in This Framework

### 1. Test Naming

```python
# Good - Descriptive names
def test_login_success_with_valid_credentials(browser):
    pass

def test_login_fails_with_invalid_password(browser):
    pass

# Avoid - Vague names
def test1(browser):
    pass

def test_login(browser):
    pass
```

### 2. Test Independence

```python
# Good - Each test is independent
def test_create_account(browser):
    # Creates account
    pass

def test_login(browser):
    # Logs in (doesn't depend on test_create_account)
    pass

# Avoid - Tests depend on each other
def test_step1(browser):
    global user_id
    user_id = create_user()

def test_step2(browser):
    login(user_id)  # Depends on test_step1
```

### 3. AAA Pattern (Arrange-Act-Assert)

```python
def test_search_product(browser):
    # Arrange - Setup
    page = SearchProductPage(browser)
    page.open(Configuration.SEARCH_URL)
    
    # Act - Execute
    page.search("jacket")
    
    # Assert - Verify
    results = page.get_results()
    assert len(results) > 0
    assert any("jacket" in r.lower() for r in results)
```

### 4. Use Fixtures for Setup

```python
# Good - Fixture handles setup
@pytest.fixture
def logged_in_user(browser):
    page = LoginPage(browser)
    page.login(username, password)
    return page

def test_account_page(logged_in_user):
    # Test starts with user already logged in
    pass

# Avoid - Setup in every test
def test_account_page(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Repeated setup
    # Test logic
```

---


## Advanced Features

### Fixtures with Parameters

```python
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    manager = BrowserManager(browser=request.param)
    driver = manager.driver
    yield driver
    driver.quit()

# Test runs twice: once with Chrome, once with Firefox
def test_cross_browser(browser):
    pass
```

### Autouse Fixtures

Run automatically without explicit request:

```python
@pytest.fixture(autouse=True)
def log_test_name(request):
    print(f"\nRunning: {request.node.name}")
```

### Fixture Factories

Create multiple instances:

```python
@pytest.fixture
def make_user():
    def _make_user(name, email):
        return {"name": name, "email": email}
    return _make_user

def test_users(make_user):
    user1 = make_user("Alice", "alice@example.com")
    user2 = make_user("Bob", "bob@example.com")
```

### Conditional Skipping

```python
import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux_feature():
    pass

@pytest.mark.xfail(reason="Known bug #123")
def test_known_issue():
    pass
```

---

## Debugging Tests

### Print Debugging
```bash
pytest -s  # Show print statements
```

### PDB Debugger
```python
def test_debug(browser):
    page = LoginPage(browser)
    import pdb; pdb.set_trace()  # Breakpoint
    page.login(username, password)
```

### Verbose Failures
```bash
pytest -vv  # Extra verbose
pytest --tb=long  # Long traceback
```


## Other Useful Options provided by pytest is BDD (Behavior-Driven Development)

For this framework was included an extra QA layer validation using BDD (Behavior-Driven Development), this is a way to validate the real user experience and the real user journey.
There is not need to extra installing, because using `pytest-bdd` (included in the requirements.txt) is enough, this is an amazing plugin that that extends the capabilities of pytest and provides a way to write tests in a more natural language.

## What is BDD (Behavior-Driven Development)?

**Behavior-Driven Development (BDD)** is a software development approach that extends Test-Driven Development (TDD) by writing test cases in natural language that non-programmers can read. BDD focuses on the **behavior** of the application from the user's perspective.

### Key Components:

1. **Gherkin Language**: Human-readable syntax using Given-When-Then
2. **Feature Files**: `.feature` files containing scenarios in plain English
3. **Step Definitions**: Python code that implements each Gherkin step
4. **Living Documentation**: Tests that serve as up-to-date documentation
5. **Extra QA Best Practices**: Using BDD is another layer of quality assurance, it helps to bridge the gap between QA and Development, and also keeps the bussiness close to real user scenarios and real user workflows, in this way it can be validate the real user experience and the real user journey.


**The Core Concept:**
In BDD with pytest-bdd, the 
.feature
 files ARE the tests, not the step definition files.

 ```
features/user_service.feature  ← This is the TEST (executable scenarios)
         │
         │ calls
         ▼
tests/bdd_steps_definitions/   ← This is the IMPLEMENTATION (glue code)

```
**How pytest-bdd Discovers Tests:**
Feature files define test cases: Each Scenario in a 
.feature
 file becomes a pytest test
Step definitions provide implementation: The Python code in tests/bdd_steps_definitions/ is glue code that gets called

**Execution Flow:**
When you run pytest features/user_service.feature:

```
1. pytest-bdd reads the .feature file
   └─> Finds: Scenario: Retrieve a specific user

2. For each Gherkin step, it looks for matching step definitions:
   └─> "Given the user service is available"
       → Searches for @given decorator with this text
       → Finds it in tests/bdd_steps_definitions/test_api_user_steps_definition.py
       → Executes the Python function
```

3. Reports pass/fail based on all steps in the scenario


---

## Learning Resources

### Official Documentation
- **Pytest Docs**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **Fixtures Guide**: [https://docs.pytest.org/en/stable/fixture.html](https://docs.pytest.org/en/stable/fixture.html)

### Tutorials
- **Real Python**: [https://realpython.com/pytest-python-testing/](https://realpython.com/pytest-python-testing/)
- **Test Automation University**: Pytest courses

### Books
- **Python Testing with pytest** by Brian Okken

---


**Next Steps**:
- Review `conftest.py` to see fixtures in action
- Explore `tests/` directory for test examples
- Check [Best Practices](../automation_strategy.md) for testing guidelines
- Check [BDD](../features/README.md) for BDD documentation