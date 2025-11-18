

# Selenium WebDriver

## What is Selenium WebDriver?

**Selenium WebDriver** is a browser automation framework that allows you to programmatically control web browsers. It's the industry standard for UI test automation.

**Official Documentation**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)

## Summary

Selenium WebDriver is the foundation of this framework:
- **Browser automation** - Control real browsers programmatically
- **Cross-browser testing** - Same tests on Chrome, Firefox, etc.
- **Industry standard** - Widely adopted, well-documented
- **Abstracted in framework** - Hidden behind `BaseActions` and page objects

---

## Why Selenium for UI Testing?

### Advantages

1. **Cross-Browser Support**
   - Chrome, Firefox, Safari, Edge
   - Same test code works across browsers

2. **Multiple Language Bindings**
   - Python, Java, C#, JavaScript, Ruby
   - This framework uses Python

3. **Real Browser Testing**
   - Tests run in actual browsers
   - Validates real user experience

4. **Open Source & Active Community**
   - Free to use
   - Extensive documentation and support

5. **Industry Standard**
   - Widely adopted in QA automation
   - Large ecosystem of tools and plugins

## Selenium vs Other Tools

| Tool | Use Case | Pros | Cons |
|------|----------|------|------|
| **Selenium** | UI automation | Real browsers, cross-browser | Slower than headless |
| **Playwright** | Modern web apps | Fast, modern API | Newer, smaller community |
| **Cypress** | JavaScript apps | Developer-friendly | JavaScript only |
| **Puppeteer** | Chrome automation | Fast, headless | Chrome only |

**This framework uses Selenium** for its maturity, community, and cross-browser support.

---

## Core Concepts

### WebDriver

The main interface for controlling the browser.

```python
from selenium import webdriver

# Create a WebDriver instance
driver = webdriver.Chrome()

# Navigate to a URL
driver.get("https://example.com")

# Close the browser
driver.quit()
```

### Locators

Strategies to find elements on a page:

| Strategy | Example | Use Case |
|----------|---------|----------|
| `ID` | `By.ID, "email"` | Unique element identifier |
| `CSS_SELECTOR` | `By.CSS_SELECTOR, "#email"` | CSS-based selection |
| `XPATH` | `By.XPATH, "//input[@id='email']"` | Complex element paths |
| `CLASS_NAME` | `By.CLASS_NAME, "btn-primary"` | Elements by class |
| `NAME` | `By.NAME, "username"` | Form elements |
| `TAG_NAME` | `By.TAG_NAME, "button"` | Elements by tag |
| `LINK_TEXT` | `By.LINK_TEXT, "Sign In"` | Exact link text |
| `PARTIAL_LINK_TEXT` | `By.PARTIAL_LINK_TEXT, "Sign"` | Partial link text |

**Best Practice**: Prefer `ID` and `CSS_SELECTOR` for speed and reliability.

### WebElement

Represents an HTML element on the page.

```python
from selenium.webdriver.common.by import By

# Find an element
element = driver.find_element(By.ID, "email")

# Interact with element
element.send_keys("user@example.com")  # Type text
element.click()                         # Click
element.clear()                         # Clear input
text = element.text                     # Get text
```

### Waits

Handle dynamic content and timing issues:

#### Implicit Wait
```python
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
```

#### Explicit Wait (Recommended)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "email")))
```

**This framework uses explicit waits** in `BaseActions` for reliability.

---

## How This Framework Uses Selenium

### 1. Browser Management (`utils/browser_manager.py`)

Abstracts WebDriver creation:

```python
class BrowserManager:
    def __init__(self, browser="chrome"):
        self.driver = self._start_driver(browser)
    
    def _start_driver(self, browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)
        # ... Firefox, etc.
```

**Benefits**:
- Easy browser switching
- Centralized configuration
- Selenium Manager handles drivers automatically

### 2. Base Actions (`pages/base_actions.py`)

Wraps common Selenium operations:

```python
class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
```

**Benefits**:
- Automatic waits
- Error handling
- Reusable across all pages

### 3. Page Objects

Use `BaseActions` to interact with pages:

```python
class LoginPage(BaseActions):
    def login(self, username, password):
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

---

## Selenium Manager (New in 4.6+)

**Selenium Manager** automatically downloads and manages browser drivers.

### Before Selenium Manager
```bash
# Manual steps:
1. Download chromedriver
2. Add to PATH or specify location
3. Update when browser updates
```

### With Selenium Manager
```python
# Just this:
driver = webdriver.Chrome()
# Selenium Manager handles the rest!
```

**This framework leverages Selenium Manager** - no manual driver management needed.

**Optional Override**:
```bash
# If you need a specific driver
export CHROME_DRIVER_PATH=/path/to/chromedriver
```

---

## Common Selenium Operations

### Navigation
```python
driver.get("https://example.com")      # Navigate to URL
driver.back()                          # Go back
driver.forward()                       # Go forward
driver.refresh()                       # Refresh page
current_url = driver.current_url       # Get current URL
```

### Element Interaction
```python
element.click()                        # Click
element.send_keys("text")              # Type
element.clear()                        # Clear input
element.submit()                       # Submit form
```

### Element Information
```python
text = element.text                    # Visible text
value = element.get_attribute("value") # Attribute value
is_displayed = element.is_displayed()  # Visibility
is_enabled = element.is_enabled()      # Enabled state
```

### JavaScript Execution
```python
driver.execute_script("window.scrollTo(0, 500);")
driver.execute_script("arguments[0].click();", element)
```

### Alerts
```python
alert = driver.switch_to.alert
alert.accept()      # Click OK
alert.dismiss()     # Click Cancel
alert.send_keys()   # Type in alert
```

### Windows/Tabs
```python
driver.switch_to.window(window_handle)
driver.window_handles  # List of all windows
```

---

## Expected Conditions

Used with explicit waits:

```python
from selenium.webdriver.support import expected_conditions as EC

# Element presence
EC.presence_of_element_located((By.ID, "email"))

# Element visibility
EC.visibility_of_element_located((By.ID, "email"))

# Element clickable
EC.element_to_be_clickable((By.ID, "submit"))

# Text in element
EC.text_to_be_present_in_element((By.ID, "message"), "Success")

# URL contains
EC.url_contains("dashboard")

# Title is
EC.title_is("Home Page")
```

---

## Best Practices in This Framework

### 1. Use Explicit Waits
```python
# Good - BaseActions uses explicit waits
self.wait.until(EC.element_to_be_clickable(locator))

# Avoid - Implicit waits or sleep
time.sleep(5)
```

### 2. Prefer CSS Selectors
```python
# Good - Fast and readable
locator = (By.CSS_SELECTOR, "#email")

# Use sparingly - Slower, brittle
locator = (By.XPATH, "//div[@class='form']//input[@id='email']")
```

### 3. Abstract Selenium Details
```python
# Good - Page object hides Selenium
page.login(username, password)

# Avoid - Selenium in tests
driver.find_element(By.ID, "email").send_keys(username)
```

### 4. Handle Stale Elements
```python
def click(self, locator):
    try:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    except StaleElementReferenceException:
        # Re-find element
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
```

---

## Troubleshooting

### Element Not Found
```python
# Check locator is correct
# Increase wait time
# Verify element is in DOM (not in iframe)
```

### Element Not Clickable
```python
# Wait for element to be clickable
# Check if element is covered by another element
# Scroll element into view
```

### Stale Element Reference
```python
# Re-find element after page changes
# Use fresh locators, not stored elements
```

### Timeout Exceptions
```python
# Increase wait time
# Check if element actually appears
# Verify locator strategy
```

---
---

## Learning Resources

### Official Documentation
- **Selenium Docs**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- **WebDriver Spec**: [https://w3c.github.io/webdriver/](https://w3c.github.io/webdriver/)

### Tutorials
- **Selenium with Python**: [https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/)
- **Test Automation University**: [https://testautomationu.applitools.com/](https://testautomationu.applitools.com/)

### Community
- **Selenium Forum**: [https://groups.google.com/g/selenium-users](https://groups.google.com/g/selenium-users)
- **Stack Overflow**: Tag `selenium` and `selenium-webdriver`

---


**Next Steps**:
- Review [BaseActions](../base_actions.md) to see Selenium in action
- Explore [Page Object Model](../program_paradigm.md) for abstraction patterns

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
