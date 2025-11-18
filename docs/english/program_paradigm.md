# Programming Paradigm: Object-Oriented Programming (OOP)

This document explains the Object-Oriented Programming (OOP) paradigm and how it's applied in this QA automation framework.

---

## What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of "objects" that contain data (attributes) and code (methods). OOP organizes software design around data and objects rather than functions and logic.

---

## Why OOP for Test Automation?

### Advantages

1. **Modularity** - Code organized into self-contained objects
2. **Reusability** - Objects can be reused across different tests
3. **Maintainability** - Changes isolated to specific classes
4. **Scalability** - Easy to add new features without breaking existing code
5. **Readability** - Code structure mirrors real-world concepts

## Benefits of OOP in This Framework

| Benefit | How It's Achieved | Example |
|---------|-------------------|---------|
| **Maintainability** | Encapsulation | Change locators in one place |
| **Reusability** | Inheritance | `BaseActions` used by all pages |
| **Scalability** | Open/Closed | Add new pages without changing existing |
| **Readability** | Abstraction | Tests read like user stories |
| **Testability** | Loose coupling | Can mock page objects for unit tests |
| **Organization** | Classes | Clear structure (one class per page) |


---

## Core OOP Concepts

### 1. Classes and Objects

#### Class
A **class** is a blueprint or template for creating objects.

```python
# Class definition
class LoginPage:
    """Blueprint for login page objects."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        # Login logic
        pass
```

#### Object
An **object** is an instance of a class.

```python
# Creating objects (instances)
browser = webdriver.Chrome()
login_page = LoginPage(browser)  # Object created from LoginPage class
account_page = AccountUserPage(browser)  # Another object

# Each object has its own data
login_page.driver  # Browser instance for login page
account_page.driver  # Browser instance for account page
```

**In This Framework**:
- Each page is a class (`LoginPage`, `AccountUserPage`, `SearchProductPage`)
- Tests create objects from these classes
- Each object represents a specific page instance

---

### 2. Encapsulation

**Encapsulation** means bundling data and methods that operate on that data within a single unit (class), and hiding internal implementation details.

#### Example Without Encapsulation

```python
# ❌ Bad - Implementation exposed
def test_login(browser):
    browser.find_element(By.ID, "email").send_keys("user@example.com")
    browser.find_element(By.ID, "password").send_keys("pass123")
    browser.find_element(By.ID, "submit").click()
    # Test knows HOW to login (implementation details)
```

#### Example With Encapsulation

```python
# ✅ Good - Implementation hidden
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._email_input = (By.ID, "email")  # Private attribute
        self._password_input = (By.ID, "password")
        self._submit_button = (By.ID, "submit")
    
    def login(self, username, password):
        """Public method - hides implementation."""
        self.driver.find_element(*self._email_input).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.driver.find_element(*self._submit_button).click()

def test_login(browser):
    page = LoginPage(browser)
    page.login("user@example.com", "pass123")
    # Test knows WHAT to do, not HOW
```

**Benefits**:
- Tests don't know implementation details
- Can change locators without changing tests
- Clear interface (public methods) vs implementation (private attributes)

**In This Framework**:
- Page classes encapsulate page interactions
- Tests use public methods like `login()`, `search()`, `submit()`
- Locators and implementation details are hidden

---

### 3. Inheritance

**Inheritance** allows a class to inherit attributes and methods from another class.

#### Basic Inheritance

```python
# Parent class (Base class)
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

# Child class (Derived class)
class LoginPage(BaseActions):
    """Inherits all methods from BaseActions."""
    
    def login(self, username, password):
        # Can use inherited methods
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

#### Method Overriding

```python
class BaseActions:
    def open(self, url):
        """Default implementation."""
        self.driver.get(url)

class LoginPage(BaseActions):
    def open(self, url):
        """Override with custom behavior."""
        super().open(url)  # Call parent method
        self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        print("Login page loaded")
```

**Benefits**:
- Code reuse (DRY principle)
- Consistent behavior across pages
- Easy to extend functionality

**In This Framework**:
- `BaseActions` is the parent class
- All page classes inherit from `BaseActions`
- Page classes get `click()`, `send_keys()`, `get_text()`, etc. for free

---

### 4. Polymorphism

**Polymorphism** means "many forms" - the ability to use a common interface for different types.

#### Example: Same Method, Different Behavior

```python
class BaseActions:
    def get_page_title(self):
        """Default implementation."""
        return self.driver.title

class LoginPage(BaseActions):
    def get_page_title(self):
        """Custom implementation for login page."""
        return "Customer Login"

class AccountPage(BaseActions):
    def get_page_title(self):
        """Custom implementation for account page."""
        return "My Account"

# Polymorphism in action
def verify_page_title(page):
    """Works with any page object."""
    title = page.get_page_title()  # Different behavior based on object type
    assert title is not None

# All page types work with same function
verify_page_title(LoginPage(driver))
verify_page_title(AccountPage(driver))
```

#### Duck Typing (Python's Polymorphism)

```python
# If it walks like a duck and quacks like a duck, it's a duck
def perform_login(page, username, password):
    """Works with any object that has a login method."""
    page.login(username, password)

# Both work because they have login() method
perform_login(LoginPage(driver), "user@example.com", "pass123")
perform_login(AdminLoginPage(driver), "admin@example.com", "admin123")
```

**Benefits**:
- Flexible code that works with multiple types
- Easy to add new page types
- Common interface for different implementations

**In This Framework**:
- All pages inherit from `BaseActions` (common interface)
- Tests can work with any page object
- Easy to add new pages without changing test structure

---

### 5. Abstraction

**Abstraction** means hiding complex implementation details and showing only essential features.

#### Example: Abstract Concepts

```python
# High-level abstraction
def test_user_can_login(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Abstract - hides complexity
    assert page.is_login_successful()

# What's hidden:
# - Finding elements
# - Waiting for elements
# - Clearing fields
# - Sending keys
# - Clicking buttons
# - Handling exceptions
```

#### Levels of Abstraction

```python
# Level 1: Raw Selenium (Low abstraction)
driver.find_element(By.ID, "email").send_keys("user@example.com")

# Level 2: BaseActions (Medium abstraction)
base_actions.send_keys((By.ID, "email"), "user@example.com")

# Level 3: Page Object (High abstraction)
login_page.login("user@example.com", "pass123")

# Level 4: Test (Highest abstraction)
test_login_success()  # Just describes what to test
```

**Benefits**:
- Simplifies complex operations
- Tests focus on business logic
- Implementation details hidden

**In This Framework**:
- Tests work at highest abstraction level
- Page objects provide business-level methods
- `BaseActions` handles Selenium complexity
- Tests are readable and maintainable

---

## OOP in This Framework: Practical Examples

### Example 1: LoginPage Class

```python
class LoginPage(BaseActions):
    """
    Encapsulation: Bundles login page data and behavior
    Inheritance: Inherits from BaseActions
    Abstraction: Hides Selenium complexity
    """
    
    def __init__(self, driver):
        """Constructor - initializes object."""
        super().__init__(driver)  # Call parent constructor
    
    def login(self, username, password):
        """
        Public method - high-level abstraction.
        Encapsulates login logic.
        """
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
    
    def is_login_successful(self):
        """Public method - checks login success."""
        return self.is_visible(Configuration.ACCOUNT_WELCOME_MESSAGE)
```

### Example 2: Using the LoginPage Object

```python
def test_login_success(browser):
    """
    Test uses OOP concepts:
    - Creates object (LoginPage)
    - Calls methods on object
    - Works at high abstraction level
    """
    # Create object
    page = LoginPage(browser)
    
    # Use object methods (abstraction)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
    
    # Verify (polymorphism - works with any page)
    assert page.is_login_successful()
```

### Example 3: Multiple Page Objects

```python
def test_user_journey(browser):
    """
    Multiple objects working together.
    Each object encapsulates its page's behavior.
    """
    # Login
    login_page = LoginPage(browser)
    login_page.open(Configuration.LOGIN_URL)
    login_page.login(username, password)
    
    # Search
    search_page = SearchProductPage(browser)
    search_page.search("jacket")
    
    # View account
    account_page = AccountUserPage(browser)
    assert account_page.is_welcome_message_visible()
```

---

## OOP Principles Applied

### 1. Single Responsibility Principle (SRP)

Each class has one responsibility:

```python
# ✅ Good - Each class has one job
class LoginPage(BaseActions):
    """Responsible ONLY for login page."""
    def login(self, username, password): pass

class AccountUserPage(BaseActions):
    """Responsible ONLY for account page."""
    def get_welcome_message(self): pass

class BrowserManager:
    """Responsible ONLY for browser management."""
    def start_driver(self): pass
```

### 2. Open/Closed Principle

Open for extension, closed for modification:

```python
# ✅ Can add new pages without modifying BaseActions
class CheckoutPage(BaseActions):  # Extends BaseActions
    def complete_checkout(self):
        # New functionality without changing BaseActions
        pass
```

### 3. Liskov Substitution Principle

Child classes can replace parent classes:

```python
def perform_action(page: BaseActions):
    """Works with BaseActions or any child class."""
    page.click(some_locator)

# All work because they inherit from BaseActions
perform_action(LoginPage(driver))
perform_action(AccountUserPage(driver))
perform_action(SearchProductPage(driver))
```

---

## OOP vs Procedural Programming

### Procedural Approach (Without OOP)

```python
# ❌ Procedural - Functions and data separate
def login(driver, username, password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

def search(driver, query):
    driver.find_element(By.ID, "search").send_keys(query)
    driver.find_element(By.CLASS_NAME, "search-btn").click()

# Data and behavior separated
# Hard to maintain as code grows
```

### OOP Approach

```python
# ✅ OOP - Data and behavior together
class LoginPage:
    def __init__(self, driver):
        self.driver = driver  # Data
    
    def login(self, username, password):  # Behavior
        # Implementation
        pass

class SearchPage:
    def __init__(self, driver):
        self.driver = driver  # Data
    
    def search(self, query):  # Behavior
        # Implementation
        pass

# Data and behavior encapsulated
# Easy to maintain and extend
```

---
---

## Common OOP Patterns in Framework

### 1. Constructor Pattern

```python
class LoginPage(BaseActions):
    def __init__(self, driver):
        """Constructor - initializes object state."""
        super().__init__(driver)
        self.username_input = Configuration.USER_NAME_INPUT
        self.password_input = Configuration.PASSWORD_INPUT_LOGIN
```

### 2. Method Chaining

```python
class LoginPage(BaseActions):
    def enter_username(self, username):
        self.send_keys(self.username_input, username)
        return self  # Return self for chaining
    
    def enter_password(self, password):
        self.send_keys(self.password_input, password)
        return self
    
    def submit(self):
        self.click(self.submit_button)
        return self

# Usage: Method chaining
page.enter_username("user@example.com").enter_password("pass123").submit()
```

### 3. Factory Pattern (in conftest.py)

```python
@pytest.fixture
def browser():
    """Factory for creating browser objects."""
    manager = BrowserManager()
    driver = manager.driver  # Creates browser object
    yield driver
    driver.quit()
```

---

## Best Practices

### 1. Keep Classes Focused

```python
# ✅ Good - Focused class
class LoginPage(BaseActions):
    def login(self, username, password): pass
    def is_login_successful(self): pass

# ❌ Bad - Too many responsibilities
class LoginPage(BaseActions):
    def login(self): pass
    def search(self): pass  # Should be in SearchPage
    def checkout(self): pass  # Should be in CheckoutPage
```

### 2. Use Meaningful Names

```python
# ✅ Good - Clear names
class LoginPage(BaseActions):
    def login(self, username, password): pass

# ❌ Bad - Vague names
class Page1(BaseActions):
    def do_stuff(self, x, y): pass
```

### 3. Favor Composition Over Inheritance

```python
# ✅ Good - Composition when appropriate
class LoginPage:
    def __init__(self, driver):
        self.actions = BaseActions(driver)  # Composition
    
    def login(self, username, password):
        self.actions.send_keys(locator, username)
```

---

## Summary

This framework uses OOP to create:
- **Modular** - Each page is a separate class
- **Reusable** - `BaseActions` shared across pages
- **Maintainable** - Changes isolated to specific classes
- **Scalable** - Easy to add new pages
- **Readable** - Tests focus on business logic

**Key OOP Concepts Applied**:
1. ✅ **Classes and Objects** - Page objects represent pages
2. ✅ **Encapsulation** - Hide implementation details
3. ✅ **Inheritance** - Reuse `BaseActions` functionality
4. ✅ **Polymorphism** - Common interface for all pages
5. ✅ **Abstraction** - High-level test methods

---

## Next Steps

- Review [Automation Strategy](automation_strategy.md) for architectural decisions
- Check [Coding Standards](coding_repository_standards.md) for SOLID principles
- Explore [Page Object Model](page_object_model.md) for POM details
- Read actual page classes in `pages/` directory

---

**OOP makes this framework professional, maintainable, and scalable.**

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  