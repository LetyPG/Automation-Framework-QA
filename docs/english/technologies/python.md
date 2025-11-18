
# Python for Test Automation

## What is Python?

**Python** is a high-level, interpreted programming language known for its simplicity and readability. It's one of the most popular languages for test automation.

**Official Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)

## Summary

Python is the language powering this framework:
- **Simple syntax** - Easy to learn and read
- **Rich ecosystem** - Selenium, Pytest, Faker, and more
- **Virtual environments** - Isolated, reproducible setups
- **OOP support** - Clean page object implementation
- **Industry standard** - Widely adopted for QA automation



## Python vs Other Languages for QA

| Language | Pros | Cons |
|----------|------|------|
| **Python** | Easy to learn, rich ecosystem | Slower than compiled languages |
| **Java** | Enterprise standard, strong typing | Verbose, more boilerplate |
| **JavaScript** | Web-native, async support | Callback hell, type issues |
| **C#** | .NET integration, strong typing | Windows-centric |

**This framework uses Python** for its simplicity and rich test automation ecosystem.


---

## Why Python for QA Automation?

### Advantages

1. **Easy to Learn and Read**
   - Simple, clean syntax
   - Reads like English
   - Low barrier to entry for QA engineers

2. **Rich Ecosystem**
   - Selenium, Pytest, Requests, etc.
   - Extensive standard library
   - Active community and packages (PyPI)

3. **Cross-Platform**
   - Works on Windows, Linux, macOS
   - Same code runs everywhere

4. **Rapid Development**
   - Less code to write
   - Quick prototyping
   - Interactive shell for testing

5. **Industry Adoption**
   - Widely used in QA automation
   - Large talent pool
   - Extensive learning resources

---

## Python Basics for This Framework

### Variables and Data Types

```python
# Strings
username = "user@example.com"
password = "SecurePass123"

# Numbers
timeout = 10
retry_count = 3

# Booleans
is_logged_in = True
test_passed = False

# Lists
locators = ["#email", "#password", "#submit"]
test_data = ["user1", "user2", "user3"]

# Dictionaries
user = {
    "email": "user@example.com",
    "password": "pass123",
    "name": "Test User"
}

# Tuples (immutable)
locator = ("css", "#email")
```

### Functions

```python
def login(username, password):
    """Logs in a user."""
    # Function body
    print(f"Logging in {username}")
    return True

# Call function
result = login("user@example.com", "pass123")
```

### Classes and Objects

```python
class LoginPage:
    """Represents the login page."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        # Login logic
        pass

# Create instance
page = LoginPage(driver)
page.login("user@example.com", "pass123")
```

### Imports

```python
# Import entire module
import os

# Import specific items
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import with alias
import pytest as pt
```

### Control Flow

```python
# If statements
if username and password:
    login(username, password)
else:
    print("Missing credentials")

# For loops
for locator in locators:
    element = driver.find_element(By.CSS_SELECTOR, locator)

# While loops
while not is_logged_in:
    attempt_login()
```

### Exception Handling

```python
try:
    element = driver.find_element(By.ID, "email")
    element.click()
except NoSuchElementException:
    print("Element not found")
except TimeoutException:
    print("Timeout waiting for element")
finally:
    print("Cleanup")
```

---

## Python Virtual Environments

### What is a Virtual Environment?

A **virtual environment** is an isolated Python environment that keeps project dependencies separate from system Python.

### Why Use Virtual Environments?

1. **Dependency Isolation**
   - Each project has its own packages
   - No conflicts between projects

2. **Version Control**
   - Pin specific package versions
   - Reproducible environments

3. **Clean System**
   - Don't pollute system Python
   - Easy to delete and recreate

### Creating Virtual Environments

#### Using `venv` (Built-in)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate
```

#### Using `virtualenv` (Third-party)

```bash
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv venv

# Activate (same as venv)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Managing Dependencies

```bash
# Install packages
pip install selenium pytest

# Install from requirements file
pip install -r requiriments.txt

# Freeze current packages
pip freeze > requiriments.txt

# List installed packages
pip list

# Uninstall package
pip uninstall selenium
```

---

## Python Features Used in This Framework

### 1. Object-Oriented Programming (OOP)

**Classes for Page Objects**:
```python
class LoginPage(BaseActions):
    """Login page object."""
    
    def __init__(self, driver):
        super().__init__(driver)  # Inherit from BaseActions
    
    def login(self, username, password):
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

**Benefits**:
- Code reusability (inheritance)
- Encapsulation (hide implementation)
- Clear structure (one class per page)

### 2. Type Hints (Optional)

```python
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver

class BrowserManager:
    def __init__(self, browser: Optional[str] = None):
        self.driver: WebDriver = self._start_driver(browser)
    
    def _start_driver(self, browser: str) -> WebDriver:
        # Returns WebDriver instance
        pass
```

**Benefits**:
- Better IDE support
- Self-documenting code
- Catch type errors early

### 3. F-Strings (String Formatting)

```python
# Modern way (Python 3.6+)
username = "user@example.com"
print(f"Logging in {username}")

# Old ways
print("Logging in {}".format(username))
print("Logging in " + username)
```

### 4. List Comprehensions

```python
# Get text from multiple elements
elements = driver.find_elements(By.CSS_SELECTOR, ".product-name")
product_names = [el.text for el in elements]

# Filter results
jackets = [name for name in product_names if "jacket" in name.lower()]
```

### 5. Context Managers

```python
# File handling
with open("test_data.txt", "r") as file:
    data = file.read()
# File automatically closed

# Custom context manager (not used in this framework, but useful)
class BrowserContext:
    def __enter__(self):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def __exit__(self, *args):
        self.driver.quit()

with BrowserContext() as driver:
    driver.get("https://example.com")
# Driver automatically quit
```

### 6. Decorators

```python
# Pytest fixtures use decorators
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Pytest markers
@pytest.mark.smoke
def test_critical_feature():
    pass
```

### 7. Generators and `yield`

```python
# Pytest fixtures use yield for setup/teardown
@pytest.fixture
def browser():
    # Setup
    driver = webdriver.Chrome()
    
    yield driver  # Test runs here
    
    # Teardown
    driver.quit()
```

---

## Python Standard Library

Useful modules for test automation:

### `os` - Operating System Interface

```python
import os

# Environment variables
base_url = os.getenv("BASE_URL")
username = os.getenv("USERNAME")

# File paths
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "test_data.txt")

# Check if file exists
if os.path.exists(file_path):
    print("File found")
```

### `pathlib` - Object-Oriented File Paths

```python
from pathlib import Path

# Modern way to handle paths
project_root = Path(__file__).parent.parent
config_file = project_root / "config" / "settings.json"

# Check if exists
if config_file.exists():
    data = config_file.read_text()
```

### `json` - JSON Data

```python
import json

# Parse JSON
data = json.loads('{"name": "Test", "value": 42}')

# Create JSON
json_string = json.dumps({"name": "Test", "value": 42})

# Read from file
with open("data.json") as f:
    data = json.load(f)
```

### `datetime` - Date and Time

```python
from datetime import datetime

# Current timestamp
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Use in test data
email = f"test_{timestamp}@example.com"
```

### `random` - Random Numbers

```python
import random

# Random choice
browser = random.choice(["chrome", "firefox"])

# Random number
user_id = random.randint(1000, 9999)
```

---

## Python Best Practices in This Framework

### 1. PEP 8 Style Guide

```python
# Good - Follow PEP 8
class LoginPage:
    def send_login_credentials(self, username, password):
        pass

# Avoid - Poor naming
class loginpage:
    def SendLoginCredentials(self, username, password):
        pass
```

**Key PEP 8 Rules**:
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- 4 spaces for indentation
- Max line length: 79-100 characters

### 2. Docstrings

```python
def login(username: str, password: str) -> bool:
    """
    Logs in a user with provided credentials.
    
    Args:
        username: User's email address
        password: User's password
    
    Returns:
        True if login successful, False otherwise
    """
    # Implementation
    pass
```

### 3. DRY (Don't Repeat Yourself)

```python
# Good - Reusable function
def send_keys(locator, text):
    element = driver.find_element(*locator)
    element.clear()
    element.send_keys(text)

# Use it multiple times
send_keys(email_locator, "user@example.com")
send_keys(password_locator, "pass123")

# Avoid - Repeated code
element = driver.find_element(*email_locator)
element.clear()
element.send_keys("user@example.com")

element = driver.find_element(*password_locator)
element.clear()
element.send_keys("pass123")
```

### 4. Explicit is Better Than Implicit

```python
# Good - Clear and explicit
from selenium.webdriver.common.by import By
locator = (By.CSS_SELECTOR, "#email")

# Avoid - Implicit assumptions
locator = "#email"  # What type? CSS? ID?
```

---

## Python Package Management

### pip - Package Installer

```bash
# Install package
pip install selenium

# Install specific version
pip install selenium==4.15.0

# Install from requirements
pip install -r requiriments.txt

# Upgrade package
pip install --upgrade selenium

# Uninstall
pip uninstall selenium

# Show package info
pip show selenium

# List installed packages
pip list

# Check for outdated packages
pip list --outdated
```

### requirements.txt

```txt
# This framework's dependencies
selenium>=4.15.0
pytest>=7.4.0
pytest-html>=3.2.0
python-dotenv>=1.0.0
faker>=20.0.0
allure-pytest>=2.13.0
```

---
---

## Learning Resources

### Official Documentation
- **Python Docs**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Python Tutorial**: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- **PEP 8 Style Guide**: [https://pep8.org/](https://pep8.org/)

### Interactive Learning
- **Python.org Beginner's Guide**: [https://wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide)
- **Real Python**: [https://realpython.com/](https://realpython.com/)
- **Python Tutor** (Visualize code): [https://pythontutor.com/](https://pythontutor.com/)

### Books
- **"Automate the Boring Stuff with Python"** by Al Sweigart
- **"Python Crash Course"** by Eric Matthes
- **"Fluent Python"** by Luciano Ramalho (Advanced)

### Communities
- **r/learnpython**: [https://www.reddit.com/r/learnpython/](https://www.reddit.com/r/learnpython/)
- **Python Discord**: [https://pythondiscord.com/](https://pythondiscord.com/)
- **Stack Overflow**: Tag `python`

---



**Next Steps**:
- Review Python code in `pages/`, `tests/`, and `utils/`
- Practice with Python interactive shell (`python`)
- Explore [Selenium](selenium.md) and [Pytest](pytest.md) documentation
- Check [Best Practices](../program_paradigm.md) for Python tips

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
