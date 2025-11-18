# Getting Started Guide

This guide will help you set up and run your first automated test with this framework. The framework is designed to be used for educational purposes, so it is not production-ready code. First than anything I recommend to study and understand the basic concepts needed to use it. 
By the other hand you will need to understand the terminal main usage, taking care that you are going to run the intsallation and the execution of the tests from the terminal.

---

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Google Chrome or Firefox** - Latest version

### Verify Installation
To used this framework, you need to have Python, Git and a web browser installed on your computer, so you need to check if you have them installed, in case you don't have them installed, you can download them from the links provided above, but first than anything I strongly recommend to study and understand the basic concepts needed to use each of them.

### Verify Installation
To verify that you have Python, Git and a web browser installed, you can run the following commands:

- **Check Python version**
  - Should show 3.12 or higher
```
python --version  
```

- **Check pip (Python package manager)**
  - Should show the version of pip installed
```
pip --version
```

- **Check Git**
  - Should show the version of Git installed
```
git --version
```
In case you do not have you need to instaled from the official website: 
- Git: [Download Git](https://git-scm.com/downloads)
- Python: [Download Python](https://www.python.org/downloads/)


**Using the terminal for installing: Linux/macOS**
If you have advanced knowledge of the terminal, and if you already have the `apt` package manager for Linux or `brew` for macOS, you can use the following commands:

- **Git**
```
sudo apt update
sudo apt install git
```

- **Python**
```
sudo apt update
sudo apt install python3
```

- **pip**
```
sudo apt update
sudo apt install python3-pip
```

- **Selenium WebDriver**
```
pip install selenium
```


**Using the terminal for installing: Windows**

Attending to the specific Shell of Windows (CMD or PowerShell) the commands migth be different, but the process is the same, in that case ensure searching for the specific command for each one.

- **Git**
```
pip install git
```

- **Python**
```
pip install python
```

- **pip**
```
pip install pip
```

- **Selenium WebDriver**
```
pip install selenium
```

---
# Starting the Project
## Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/LetyPG/Automation-Framework-QA.git

# Navigate to the project directory
cd Automation-Framework-QA
```

---

## Step 2: Set Up Python Virtual Environment (Recommended)

Using a virtual environment isolates project dependencies from your system Python.

### On Linux/macOS:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### On Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt when activated.

---

## Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requiriments.txt
```

**Note**: The file is named `requiriments.txt` (not `requirements.txt`) in this repository.

### What Gets Installed:
- `selenium` - Browser automation
- `pytest` - Test framework
- `pytest-html` - HTML test reports
- `python-dotenv` - Environment variable management
- `faker` - Test data generation
- `allure-pytest` - Advanced reporting (optional)

---

## Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# Copy the example file
cp docs/english/.env_example.txt .env
```

### Edit `.env` File

Open `.env` and configure the variables values to match your environment, for example, if you want to test a different website, you can change the `BASE_URL` variable to the URL of the website you want to test.
For this proyect as an exmaple is provide a `.env_example.txt` file, you can use it as a template, located in this same directory `docs/english/.env_example.txt`


**Important**: 
- Replace `USERNAME` and `PASSWORD` with real credentials for positive login tests
- Never commit `.env` to version control (it's in `.gitignore`)

---

## Step 5: Verify Browser Driver Setup

This framework uses **Selenium Manager** (built into Selenium 4.6+), which automatically downloads and manages browser drivers. You don't need to manually download drivers!

### Optional: Manual Driver Setup

If you prefer to use a local driver or your environment doesn't allow automatic downloads:

1. Download the appropriate driver:
   - **Chrome**: [ChromeDriver](https://chromedriver.chromium.org/)
   - **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Set environment variable:
   ```bash
   # For Chrome
   export CHROME_DRIVER_PATH=/path/to/chromedriver
   
   # For Firefox
   export FIREFOX_DRIVER_PATH=/path/to/geckodriver
   ```

See [driver/README.md](../../driver/README.md) for more details.

---

## Step 6: Run Your First Test

- General tests:

```
pytest`  (or `pytest -v`)

- General tests in a specific directory <tests/test_directory_name>:

```
pytest tests/ui_tests -v
```

- Specific test file <tests/test_directory_name/test_file_name.py>:

```
pytest tests/smoke_tests/test_account_user.py -v
```

- Specific test by name (this will execute any test function in any suite) with -k:

```
pytest -k test_login_success_if_credentials_present -v
```

- Markers (only if tests are marked accordingly):

```
pytest -m smoke -v
```

```
pytest -m regression -v
```

---

## Step 7: Generate Test Reports

### HTML Report
```bash
pytest -v --html=report.html --self-contained-html
```

Open `report.html` in your browser to view results.

### Allure Report (Optional)
```bash
# Generate Allure results
pytest --alluredir=reports/allure-results

# Serve Allure report
allure serve reports/allure-results
```

---

## Step 8: Run Unit Tests (No Browser Required)

This framework includes unit tests for page objects that run without launching a browser:

```bash
# Run all unit tests
pytest tools/src_unit -v

# Run specific unit test file
pytest tools/src_unit/test_login_unit.py -v

# Run with quiet mode
pytest tools/src_unit -q
```

See [tools/src_unit/README.md](../../tools/src_unit/README.md) for more details.

---

## Common Issues and Solutions

### Issue: `ModuleNotFoundError: No module named 'selenium'`
**Solution**: Activate virtual environment and install dependencies:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requiriments.txt
```

### Issue: `WebDriverException: Message: 'chromedriver' executable needs to be in PATH`
**Solution**: Selenium Manager should handle this automatically. If not:
1. Ensure you have Selenium 4.6+: `pip install --upgrade selenium`
2. Or set `CHROME_DRIVER_PATH` environment variable

### Issue: Tests fail with "Element not found"
**Solution**: 
1. Check if locators in `.env` match the website structure
2. Increase implicit wait time: Add `IMPLICIT_WAIT=5` to `.env`
3. Website may have changed - update locators accordingly

### Issue: Login tests fail
**Solution**: 
1. Verify `USERNAME` and `PASSWORD` in `.env` are correct
2. Ensure the account exists on the test website
3. Check if the website requires CAPTCHA or 2FA

---

## Next Steps

Now that you have the framework running:

1. **Explore the Code**:
   - Review `pages/` directory to understand Page Object Model
   - Check `tests/` to see test structure
   - Examine `utils/` for helper functions

2. **Read Documentation**:
   - [Project Overview](project_overview.md) - Understand the architecture
   - [Automation Strategy](automation_strategy.md) - Learn design decisions


3. **Experiment**:
   - Modify existing tests
   - Add new page objects
   - Create new test scenarios
   - Try different browsers (set `BROWSER=firefox` in `.env`)

4. **Learn Advanced Features**:
   - Dynamic test data with Faker
   - Custom assertions
   - Parallel test execution
   - CI/CD integration

---

## Quick Reference Commands

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/smoke_tests/test_account_user.py -v

# Run by test name pattern
pytest -k test_account_user -v

# Run by marker
pytest -m smoke -v

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run unit tests only
pytest tools -v

# Deactivate virtual environment
deactivate
```

---

## Getting Help

- **Documentation**: Check other files in `docs/english/`
- **Issues**: Review common issues above
- **Examples**: Look at existing tests in `tests/` directory
- **Community**: Share and learn with other QA engineers

---

**Congratulations!** 🎉 You've successfully set up the QA Automation Framework. Happy testing!

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  