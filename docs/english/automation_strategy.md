

## Automation Strategy

This document explains the architectural decisions, design patterns, and strategic choices made in building this QA automation framework.

## Objectives

- Automatize critical flows of an e-commerce web site Magento, validating functionalities as login, user registration, search, shopping cart and checkout, reliably and reutilizable.
- Create a simple Automation Framework for a web site UI (Magento) and as an educational project.
- Understand the basic concepts of Automation Framework  using Python, Selenium WebDriver, Pytest, Faker, Allure Reports, and it is not a production ready code.


## Summary of Architectural Decisions

| Decision | Rationale | Benefit |
|----------|-----------|---------|
| **Page Object Model** | Separate UI from tests | Maintainability, reusability |
| **Pytest** | Simple, powerful fixtures | Clean tests, rich ecosystem |
| **Fixtures over setUp** | Dependency injection | Flexibility, composability |
| **Composition (BaseActions)** | Loose coupling | Testability, flexibility |
| **Shallow inheritance** | Simplicity | Easy to understand |
| **Separate `pages/` directory** | Organization | Scalability |
| **Separate `tests/` directory** | Organization across test strategies | Scalability |
| **Separate `tools/` for unit tests** | Fast feedback | Quick validation |
| **`.env` + `config.py`** | Configuration management | Environment flexibility |
| **Faker for test data** | Dynamic data | Realistic, unique data |

---

## Design Principles Applied

1. **DRY (Don't Repeat Yourself)** - `BaseActions` for reusable operations
2. **SOLID** - See [coding_repository_standards.md](coding_repository_standards.md)
3. **Separation of Concerns** - Pages, tests, utils separated
4. **Single Responsibility** - Each class has one job
5. **Dependency Injection** - Fixtures inject dependencies
6. **Configuration over Code** - `.env` for settings


---

## Core Strategy: Page Object Model (POM)

### What is Page Object Model?

**Page Object Model (POM)** is a design pattern that creates an object repository for web UI elements. Each web page is represented as a class, and the web elements are defined as variables within that class.

### Why POM?

#### 1. **Separation of Concerns**
```python
# ❌ Without POM - Test mixed with implementation
def test_login():
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("pass123")
    driver.find_element(By.ID, "submit").click()
    assert "Welcome" in driver.find_element(By.CLASS_NAME, "message").text

# ✅ With POM - Clean separation
def test_login(browser):
    page = LoginPage(browser)
    page.login("user@example.com", "pass123")
    assert page.is_login_successful()
```

**Benefits**:
- Tests focus on **what** to test, not **how** to interact with UI
- Business logic separated from technical implementation
- Tests read like user stories

#### 2. **Maintainability**

When UI changes, you only update the page object:

```python
# If login button locator changes from ID to CSS
# Update ONLY in LoginPage class:
class LoginPage:
    # Before: LOGIN_BUTTON = (By.ID, "submit")
    # After:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-btn")
    
# All tests using LoginPage automatically work!
```

**Benefits**:
- Single point of change
- Reduces maintenance effort
- Prevents test fragility

#### 3. **Reusability**

Page methods can be reused across multiple tests:

```python
# Multiple tests use the same login method
def test_view_account(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Reused
    # Test account page

def test_view_orders(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Reused
    # Test orders page
```

#### 4. **Readability**

Tests become self-documenting:

```python
def test_user_can_search_products(browser):
    # Arrange
    search_page = SearchProductPage(browser)
    search_page.open(Configuration.SEARCH_URL)
    
    # Act
    search_page.search("jacket")
    
    # Assert
    results = search_page.get_results()
    assert len(results) > 0
    assert any("jacket" in r.lower() for r in results)
```

---

## Why Pytest?

### 1. **Simple and Pythonic**

```python
# Pytest - Simple and readable
def test_addition():
    assert 2 + 2 == 4

# unittest - More boilerplate
import unittest
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
```

### 2. **Powerful Fixtures**

Fixtures provide clean setup/teardown:

```python
@pytest.fixture
def browser():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

def test_login(browser):  # Fixture injected automatically
    # Test uses browser without manual setup
    pass
```

**Benefits**:
- No repetitive setup code
- Automatic cleanup
- Dependency injection
- Scope control (function, class, module, session)

### 3. **Rich Ecosystem**

- `pytest-html` - HTML reports
- `pytest-xdist` - Parallel execution
- `allure-pytest` - Advanced reporting
- `pytest-bdd` - BDD support

### 4. **Detailed Failure Reports**

Pytest provides introspective assertion messages:

```python
def test_example():
    expected = "Hello World"
    actual = "Hello Python"
    assert expected == actual

# Output:
# AssertionError: assert 'Hello World' == 'Hello Python'
#   - Hello Python
#   + Hello World
```

---

## Why Fixtures Over Setup/Teardown?

### Traditional Approach (unittest)

```python
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_login(self):
        # Test code
        pass
```

**Problems**:
- Tied to class structure
- Hard to share across test files
- No dependency injection
- Limited scope control

### Fixture Approach (Pytest)

```python
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):  # Clean, injected
    # Test code
    pass
```

**Advantages**:
- ✅ Shared across files (via `conftest.py`)
- ✅ Dependency injection
- ✅ Flexible scopes
- ✅ Composable (fixtures can use other fixtures)
- ✅ Explicit dependencies

### Fixture Composition

```python
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(browser):  # Uses browser fixture
    page = LoginPage(browser)
    page.login(username, password)
    return page

def test_account_page(logged_in_user):  # Uses composed fixture
    # Test starts with user already logged in
    pass
```

---

## Composition Over Inheritance

### Why Composition?

**Inheritance** creates tight coupling:

```python
#  Inheritance - Tight coupling
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        # Implementation
        pass

class LoginPage(BasePage):
    # Inherits everything from BasePage
    pass
```

**Problems**:
- Changes to `BasePage` affect all child classes
- Hard to test in isolation
- Fragile base class problem

**Composition** provides flexibility:

```python
# Composition - Flexible
class BaseActions:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        # Implementation
        pass

class LoginPage:
    def __init__(self, driver):
        self.actions = BaseActions(driver)  # Composition
    
    def login(self, username, password):
        self.actions.click(locator)  # Use composed object
```

**Benefits**:
- Loose coupling
- Easy to test (can mock `BaseActions`)
- Flexible (can swap implementations)

### This Framework's Approach

We use **inheritance for convenience**, but keep it shallow:

```python
class BaseActions:
    """Reusable Selenium operations."""
    def click(self, locator): pass
    def send_keys(self, locator, text): pass

class LoginPage(BaseActions):
    """Inherits BaseActions for convenience."""
    def login(self, username, password):
        self.send_keys(USER_INPUT, username)
        self.send_keys(PASS_INPUT, password)
        self.click(LOGIN_BUTTON)
```

**Why this works**:
- Single level of inheritance
- `BaseActions` is stable (rarely changes)
- Page objects focus on page-specific logic
- Easy to understand and maintain

---

## Folder Structure Explained

```
Automation-Framework-QA/
├── docs/                    # Documentation
├── driver/                  # Optional browser drivers
├── src/                     # Source code of the framework 'src' is short for 'source'
│   ├── pages/                   # Page Object classes
│   |   ├── base_actions.py      # Reusable Selenium operations
│   |   ├── login.py             # LoginPage
│   |   └── page_account_user.py # AccountUserPage
│   └── api/                     # API Client Module
│       ├── __init__.py          # Module exports
│       ├── base_api_client.py   # Base HTTP client (reusable)
│       ├── user_service_api.py  # User service implementation
│       ├── product_service_api.py  # Product service (future)
│       └── README.md            # This file explain the api module
├── ci_cd/
|     ├── README.md
|     ├── jenkins_api/
|     |     ├── jenkinsfile
|     |     └── 
|     └── jenkins_staging/
|     |     |     ├── jenkinsfile
|     |     |     └── 
|     |     └── jenkins_smoke/
|     |     |     ├── jenkinsfile
|     |     |     └── 
|     |     └── jenkins_ui/
|     |           ├── jenkinsfile
|     |           └── 
├── features/
|           ├── README.md
|           ├── api/
|           |     ├── user_service.feature
|           |     └── product_service.feature
|           |     └── order_payment_service.feature
|           └── ui/
|             ├── login.feature
|             └── account_user.feature
|             └── search_product_page.feature
|
├── tests/                   # Modules (test suites, grouped by test stratgies)
|     |___ bdd_steps_definition/ # BDD Steps Definition
|     |     |__ conftest.py
|     |     ├── test_api_user_steps_definition.py
|     |     └── test_ui_login_steps_definition.py
|     ├── smoke_test/
|     |     ├── test_login.py
|     |     └── test_account_user.py
|     |     ├── test_form_submission.py
|     |     └── test_search_product_page.py
|     ├── sanity_test/
|     |     ├── 
|     |     └── 
|     ├── regression_test/
|     |     ├── 
|     |     └── 
|     ├── e2e_test/
|     |     ├── 
|     |     └── 
|     ├── performance_test/
|     |     ├── 
|     |     └── 
|     |___ db_test/
|     |     ├── 
|     |     └── 
|     ├── api_test/
|     |     ├── test_user/
|     |     |     ├── conftest.py
|     |     |     ├── test_user_service.py
|     |     |     └── test_user_search.py
|     |     |     └── test_user_data_validation.py
|     |     |     └── test_user_service_integration.py
|     |     └── test_product/
|     |     |     ├── 
|     |     |     └── 
|     |     └── test_order/
|     |     |     ├── 
|     |     |     └── 
|     |     └── 
|     ├── security_test/
|     |     ├── 
|     |     └── 
|     ├── load_test/
|     |     ├── 
|     |     └── 
|     ├── install_test/
|     |     ├── 
|     |     └── 
|
├── tools/                   # Unit tests for page objects
│   ├── conftest.py          # Unit test fixtures
│   └── test_login_unit.py
├── utils/                   # Utilities
│   ├── browser_manager.py   # Browser setup
│   ├── config.py            # Configuration
│   ├── data_generator.py    # Test data with Faker
│   └── assertions.py        # Custom assertions
|   ├── logger.py            # Logger

├── .env                     # Environment variables
├── conftest.py              # Global pytest fixtures
├── pytest.ini               # Pytest configuration
└── requiriments.txt         # Dependencies
```

### Why This Structure?

#### 1. **`pages/` - Page Objects**

**Purpose**: One class per page, encapsulating page interactions.

**Why separate directory?**
- Clear organization
- Easy to find page objects
- Scales as pages grow

**Example**:
```python
# pages/login.py
class LoginPage(BaseActions):
    def login(self, username, password):
        # Page-specific logic
        pass
```


## Recommended Testing Distribution

For a balanced QA framework:

| Test Type | % of Tests | Purpose |
|-----------|-----------|---------|
| **BDD (Acceptance)** | 15-20% | Critical user flows, acceptance criteria |
| **Integration/Functional** | 60-70% | Detailed API/UI testing, edge cases |
| **Unit Tests** | 10-15% | Test framework components (POMs, utils) |
| **E2E** | 5-10% | Full system integration |

**BDD Focus Areas:**
- Critical happy paths
- Key negative scenarios
- Business-critical workflows
- Acceptance criteria validation

**Standard Pytest Focus Areas:**
- Edge cases
- Boundary testing
- Performance tests
- Security tests
- Data validation
- Technical scenarios


#### 2. **`tests/` -  Tests Suites**

**Purpose**: 
- Tests that use real browser.
- Where created test suites grouped by test strategy.
- Some important subdirectories inside of `tests/` are planed to be develope in the future, for that reason you can check their existence even if they are empty, only `smoke_test/` and the `api_test/` are develope at the moment of this version.

- In this scope was created an unique directory for each test strategy, at the moment of this version the framework only develope `smoke test` as a test strategy guide, but in the future I will add more test strategies, so for now it has only been created the test suites grouped by test strategy (inside of each directory or for bigger directory, such as `smoke_test/`.
But therefore it was not already develope the rest of test strategies  you could be able to find inside of each test strategy directory an explanatory doc, to undertsand how to use the test strategy and the logical proposal for the architecture of this framework.
- In this scope was develope the test modules grouped by test strategy (as was mentionated before),for develope each test strategy you need to create a test module, but depending on your needs I recomended this two practices:

**1. Organize the test_strategy as was mentionated before, but inside of each test_strategy directory, create subdirectories attending to different functionalities:**


```
      test/
      |__smoke_test/
      |          |__test_login/
      |          |    |__test_login_success.py
      |          |    |__test_login_negative.py
      |          |    |__test_login_desviation.py
      |          |    |__test_login_multiples_inputs_combinations.py
      |          |    |__test_login_multiples_users.py
      |          |___test_account_user/
      |          |    |__test_account_user_success.py
      |          |    |__test_account_user_negative.py
      |          |    |__test_account_user_desviation.py
      |          |    |__test_account_user_multiples_inputs_combinations.py
      |          |    |__test_account_user_multiples_users.py
      

```

**2. Organize the test in subdirectories attending to different funcionalities:** 

```
      test/
      |__test_login/
      |    |__test_login.py
      |    |__test_login_negative.py
      |    |__test_login_api.py
      |    |__test_login_security.py
      |    |__test_login_load.py
      |    |__test_login_performance.py
      |    |__test_login_regressio
      |__test_search/
      |    |__test_search.py
      |    |__test_search_negative.py
      |    |__test_search_api.py
      |    |__test_search_security.py
      |    |__test_search_load.py
      |    |__test_search_performance.py
      |    |__test_search_regression.py

```
 

### About API Tests

This API module provides a robust, scalable framework for REST API testing using **Object-Oriented Programming (OOP)** and **SOLID principles**. It demonstrates professional-grade test automation patterns suitable for educational purposes and real-world projects.

- **Layered Architecture**
```
┌─────────────────────────────────────┐
│        Test Layer                   │  ← Test files with assertions
│  (test_user_service.py, etc.)       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Service Layer                   │  ← Business logic for each API
│  (UserServiceAPI, ProductAPI, etc.) │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Base Client Layer               │  ← HTTP communication (reusable)
│     (BaseAPIClient)                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     External API                    │  ← Actual REST API endpoints
└─────────────────────────────────────┘
```

**Design Patterns Used**
- **Template Method Pattern**: BaseAPIClient defines HTTP methods structure
- **Factory Pattern**: Fixtures create test data and API instances
- **Page Object Model (POM) Equivalent**: Service APIs encapsulate endpoints
- **AAA Pattern**: Arrange-Act-Assert in all tests

**Detailed SOLID Principles Section**
Each principle explained with real code examples from your framework:

- Single Responsibility Principle: BaseAPIClient handles HTTP, UserServiceAPI handles business logic
- Open/Closed Principle: Extend BaseAPIClient without modifying it
- Liskov Substitution Principle: Service APIs can substitute the base class
- Interface Segregation Principle: Each API exposes only relevant methods
- Dependency Inversion Principle: Depends on abstractions (requests interface)


#### API Tests Directory Structure

```
├── tests/
│   ├── api_test/                          # API Tests Directory
│   │   ├── conftest.py                    # Shared fixtures & configuration
│   │   │
│   │   ├── test_user/                     # User API tests (organized by feature)
│   │   │   ├── __init__.py
│   │   │   ├── test_user_service.py       # CRUD operations tests (Create, Read, Update, Delete)
│   │   │   ├── test_user_search.py        # Search/filter tests
│   │   │   ├── test_user_data_validation.py  # Parametrized validation tests
│   │   │   └── test_user_service_integration.py  # Integration/lifecycle tests
│   │   │
│   │   ├── test_product/                  # Product API tests (future)
│   │   │   └── __init__.py
│   │   │
│   │   └── test_order_payment/            # Order/Payment API tests (future)
│   │       └── __init__.py

```
### **1. Test Organization**
- Organize tests by feature/service in separate directories
- Use `conftest.py` for shared fixtures
- Keep test files focused on specific functionality
- Use descriptive test method names


### **2. Fixture Usage**
- Use `scope="module"` for expensive fixtures (API clients)
- Use `scope="function"` for test data that should be fresh
- Place fixtures in `conftest.py` for reusability



### **3. Assertions**
- Use descriptive assertion messages
- Validate multiple aspects (status code, data structure, values)
- Use JSON schema validation for contract testing
- Only check status code (validate response data too)
- Use generic assertion messages

### **4. Test Data**
- Use Faker for realistic test data
- Create fixtures for reusable data structures
- Use parametrized tests for multiple scenarios
- Hardcode test data in test methods
- Reuse same data across tests (unless intentional)

>On the actual version of this framework were develope the api base class and one instance of it (user_api), for the same reason was develope a test subdirectory for the user_api instance to validate the api across user features, but other important subdirectories are planed to be develope in the future, for that reason you cna check their existence even if they are empty.




### About Unit Tests

      
**Why separate from unit tests?**
- Different execution speed (slow vs fast)
- Different dependencies (browser vs mocks)
- Different CI/CD strategies

**Example**:
```python
# tests/test_login.py
def test_login_success(browser):
    page = LoginPage(browser)
    page.login(username, password)
    assert page.is_login_successful()
```

#### 3. **`tools/` - Unit Tests**

**Purpose**: Fast tests for page objects without browser.

**Why separate directory?**
- Fast feedback loop
- No browser overhead
- Test page logic in isolation

**Example**:
```python
# tools/test_login_unit.py
def test_login_calls_correct_methods(mock_driver):
    page = LoginPage(mock_driver)
    page.login("user@example.com", "pass123")
    # Verify methods were called
```

#### 4. **`utils/` - Utilities**

**Purpose**: Shared helper functions and classes.

**Why separate?**
- Reusable across pages and tests
- Single responsibility
- Easy to test

**Contents**:
- `browser_manager.py` - Browser lifecycle
- `config.py` - Configuration management
- `data_generator.py` - Test data generation
- `assertions.py` - Custom assertions

#### 5. **`conftest.py` - Global Fixtures**

**Purpose**: Pytest fixtures shared across all tests.

**Why at root?**
- Automatically discovered by pytest
- Available to all test files
- Centralized setup logic

**Example**:
```python
# conftest.py
@pytest.fixture
def browser():
    manager = BrowserManager()
    driver = manager.driver
    yield driver
    driver.quit()
```

#### 6. **`.env` - Environment Variables**

**Purpose**: Store configuration and secrets.

**Why `.env`?**
- Keep secrets out of code
- Easy to change per environment
- Not committed to version control

**Example**:
```bash
BASE_URL=https://magento.softwaretestingboard.com
USERNAME=user@example.com
PASSWORD=SecurePass123
```

---

## Why BaseActions?

### Problem Without BaseActions

```python
# Every page repeats the same code
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
    
    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):  # Duplicated!
        element = self.driver.find_element(*locator)
        element.click()
```

### Solution: BaseActions

```python
# pages/base_actions.py
class BaseActions:
    """Reusable Selenium operations."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

# pages/login.py
class LoginPage(BaseActions):
    """Inherits all BaseActions methods."""
    def login(self, username, password):
        self.send_keys(USER_INPUT, username)  # From BaseActions
        self.send_keys(PASS_INPUT, password)  # From BaseActions
        self.click(LOGIN_BUTTON)              # From BaseActions
```

**Benefits**:
- DRY (Don't Repeat Yourself)
- Consistent behavior across pages
- Built-in waits and error handling
- Easy to extend with new operations

---

## Configuration Management Strategy

### Why `.env` + `config.py`?

#### Problem: Hardcoded Values

```python
# Bad - Hardcoded
def test_login():
    driver.get("https://magento.softwaretestingboard.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
```

**Problems**:
- Can't change URL without modifying code
- Credentials exposed in code
- Different environments need different values

#### Solution: Configuration Layer

```bash
# .env
BASE_URL=https://magento.softwaretestingboard.com
LOGIN_URL=https://magento.softwaretestingboard.com/customer/account/login
USERNAME=user@example.com
PASSWORD=SecurePass123
USER_NAME_INPUT=css,#email
```

```python
# utils/config.py
class Configuration:
    BASE_URL = os.getenv('BASE_URL')
    LOGIN_URL = os.getenv('LOGIN_URL')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    USER_NAME_INPUT = parse_locator(os.getenv('USER_NAME_INPUT'))
```

```python
# tests/test_login.py - Clean!
def test_login(browser):
    page = LoginPage(browser)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
```

**Benefits**:
- No hardcoded values
- Easy to change per environment
- Secrets not in code
- Single source of truth

---

## Test Data Strategy: Faker

### Why Dynamic Data?

#### Problem: Hardcoded Test Data

```python
# Bad - Hardcoded data
def test_registration():
    page.register(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"  # Fails if already exists!
    )
```

**Problems**:
- Duplicate data errors
- Unrealistic test scenarios
- Limited test coverage

#### Solution: Faker

```python
# Good - Dynamic data with Faker
from utils.data_generator import DataGenerator

def test_registration():
    generator = DataGenerator()
    user = generator.generate_user()
    
    page.register(
        first_name=user["first_name"],   # "Alice" (random)
        last_name=user["last_name"],     # "Johnson" (random)
        email=user["email"]              # "alice.j@example.com" (unique)
    )
```

**Benefits**:
- Unique data every run
- Realistic test scenarios
- Better edge case coverage
- No data pollution

---
---

## Next Steps

- Review [Page Object Model](programming_standards.md) for detailed POM examples
- Check [Coding Standards](coding_repository_standards.md) for SOLID principles
- Check [Coding Standards](programm_paradigm.md) for Object Oriented Programming
- Explore [Best Practices](selenium.md) for QA guidelines
- Explore [Best Practices](pytest.md) for QA guidelines
- Read [Getting Started](getting_started.md) to run the framework

---

**This automation strategy ensures a maintainable, scalable, and professional QA framework.**

----
**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  