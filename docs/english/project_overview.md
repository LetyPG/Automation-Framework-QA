
## Project Directory Structure

```
Automation-Framework-QA/
├── docs/                    # Documentation of the framework in markdown format and includes English and Spanish documentation
├── ci_cd/                   # CI/CD Module base calss for CI/CD tests, contains jenkinsfiles for different jobs (api, staging, smoke, ui), that are used to run the tests in different environments.
├── drivers/                 # Drivers for different browsers
|__ features/                # Features for different environments using BDD (Behavior Driven Development)
├── src/                     # Source code of the framework 'src' is short for 'source'
│   ├── pages/               # Clase by page (modelo POM)
│   |__ api/                 # API Module base calss for API tests
├── tests/                   # Module test cases
├── utils/                   # Configuration, logs, data and helpers
├── tools/                   # Unit tests for page objects
├── .env                     # Environment variables and external locators
├── conftest.py              # Pytest global fixtures
├── requirements.txt         # Environment dependencies
└── README.md                # Framework documentation

```
----

## Amplified Structure Details

Al directories that were structure for this framework are based on the SOLID principles. so it was the intent to make the framework easy to maintain and scale. 
From here the directories were structured as follows (You can see initials `L, S, O, I, D` as the begining of the directory explanation)

### 1. `L` Principle:
```
│
├── drivers/

```

<details>
<summary>`drivers/` Directory <br>- Liskov Substitution Principle (support for different browsers)</summary>


```

├── drivers/                      
│   └── chromedriver.exe           #The code can be used in different implementations of the driver (Webdriver) on different browsers 
│                                  (Chrome, Firefox, Zafari) without breaking the tests.
│                                  #If a child class (LoginPage) extends and uses the parent class (Basepage),then it does not modify the test flow.


```

</details>


----

### 2. `S` Principle
### 3. `I` Principle:

```
│
├── pages/

```


<details><summary>`pages/` Directory <br>-  Single Responsibility Principle (each class models a single web page) <br>- Interface Segregation Principle (each class consume only the necessary methods from each class)</summary>


- Each class models a single page of the site for all pages
- The first Object "Page"  inicializing the model POM (Page Object Model)   
- Support the DRY (Don’t Repeat Yourself) principle   

- Each class Page models a single web page.
- The pages isolation is going to be relative as the way that the software handles its services, usually one page handle a single service to centralized the logic of the page and the users requests, for this scope were consired separeted this services, also each service corresponds with a unique url (as login, registration, search, shopping cart, checkout, etc.)


```

├── src/pages/                        
│   ├── __init__.py
│   ├── base_page.py         # Definition of the base class (BasePage), with reusable methods to encapsulate interaction logic, with the browser and elements (click, write, wait)
│   ├──                      # Them are created instanciated to the driver, where the generic methods of the base class are inherited (herencia) 
│   ├──                      # Are cretaed new class for each interface, with especific methods of each interface are added, so a new Object Page is created for each interface
│   ├── login_page.py               # Login (LoginPage)
│   ├── page_form_submission.py     # Authentification  Form or Registration (SubmissionForm)
│   ├── page_account_user.py        # User Account (UserAccount)
|
|   # This are other pages of the site that are not used in this project but are created for the POM (Page Object Model)
│   ├── search_product_page.py      # Search Products (SearchProducts)
│   ├── product_page.py             # Add to cart, favorites, etc. (ProductActions)
│   ├── cart_page.py                # Shopping Cart (ShopingPage)
│   ├── payment_page.py             # Payment Page (PurchasePage)
│   ├── page_favorites.py           # Favorites (Favorites)

```

</details>

----

### 4. `O` Principle

```
│
├── tests/

```

<details>
<summary>`tests/` Directory <br>- Open to extension, closed to modification</summary>

- Open to extension, closed to modification it means that we can add new tests or pages without modifying the existing code.
- It can be add new tests or pages without modifying the existing code.
- It can be add new validations or assertions without modifying the existing code.
- Each test is independent of the others and include it's own assertions and validations.

>Also was created a islote class wich contains the assertions and validations, instead of adding them to each test, this class is used to centralize the assertions and validations, and it is located in the utils directory.

```
├── tests/    
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_page_form_submission.py
│   ├── test_account_user.py
│   ├── test_search_product.py
# This are other tests of the site that are not used in this project but are created for the POM (Page Object Model)
│   ├── test_add_to_cart.py
│   ├── test_favorites.py
│   ├── test_checkout.py
│   └── test_order_history.py

```

</details>


### Rationale 
- For this project was created one only test module, but it can be created more modules to test different features of the site, as an example suggestions coould be crested this differents directories as indepndent modules: smoke, regression, e2e, etc.
- Also is a good practice to create a test module with negative tests, to validate the error messages and the error pages, but for this project was not created. The real is that with this isolation is better to separate funcionallity validation to the error handling.
- Therefore the arguments explain before it is importante to mentionated that on the `test_loging. py` file was included a negative test to validate the funcionallity error in case of wrong credentials.

### 5. `D`: Principle

```
│
├── utils/

```

<details>
<summary>`utils/` Directory <br> Dependency Inversion Principle (tests do not depend directly on the webdriver, the dettails such as selectors, the data, the browser configurations) </summary>



- The utils directory contains the assertions, data generator, browser manager, config and logger.
- By applying this principle,is keeping the logic  which states that high-level modules should not depend on low-level modules, but both should depend on abstractions. 
- The utils provides abstractions to the tests, so the tests are not dependent on the webdriver, the details such as selectors and browser configuration are abstracted in layers (`utils`, `.env`, fixtures).
- This keeps the tests independent of the details of the implementation, by using abstractions to hide the implementation details.

```
├── utils/  
│   ├── __init__.py
│   ├── assertions.py       # Soft/hard assertions, custom comparisons (assert equal) for validations of confirmations as if a 
│   ├──                     received text(actual) is equal(==) to expected (expected)
│   ├──                     
│   ├── data_generator.py   # Data generator with Faker (users, emails, addresses, etc.), so test do not depend on details fixed as data
│   ├── browser_manger.py   # This abstracts webdriver for different browsers and ensures in the pytest configuration (conftest.py) that tests can be executed 
│   ├──                      without depending on details fixed as data (driver= Chromedriver vs driver=BrowseManger) and can be changed to others without touching the tests
│   ├──                     
│   ├── config.py           # It centralizes values as urls, locators,timeout and avoid harcodearlos (fixed data inside the code) in the test, this means that,
│   ├──                      if a locator with a unique attribute CSS (By.Id, "email") changes, it must be searched inside the test to change it, 
│   ├──                      So Config is used as an abstraction to make the tests independent of fixed data
│   ├──                     
│   └── logger.py          # It centralizes logging with format, timestamp and levels (info, error, debug)
│


```

</details>


### 6. `D`: Repeatability Principle

```
│
├── .env

```

<details>
<summary>`.env` File (variables of environment for configuration and selectors, urls, locators, timeout, etc.) - D: Dependency Inversion (the code is not dependent on the details of the implementation)</summary>



- The .env file contains variables of environment for configuration and selectors, urls, locators, timeout, etc.
- This also avoid hardcode fixed islotes the variables values. 
- For example, if a locator with a unique attribute CSS (By.Id, "email") changes, it must be searched inside the test to change it.
- So Config is used as an abstraction to make the tests independent of fixed data
- This file should be added to .gitignore, because it contains sensitive data, so it should not be committed to the repository, for security reasons, r=for the same motive you can see the file .env includedd in the .gitignore file, and it is not show in this repository
>For complex locators with XPATH, it is recommended to use a file locators.py or a file .ymal to avoid hardcode fixed islotes the variables values, such as locators.yml


```
├── .env   
├──     
# Other posible files to manage the locators variables values.                        
├── locators.py
├── locators.yml

```

**Example of .env file to be used as template to create .env file**

To a better guide of this practice you can see the file on this same directory (`docs/english/.env_example`), this file is only for example purposes, so it is recommended to create a new .env file and add the variables of environment for configuration and selectors, urls, locators, timeout, etc.

**Note:** The original .env file is not this and it was not included on this Repository, for the reasons of security and privacy, so it is only for example purposes


</details>


----

### Important Configurations Files

<details>
<summary>`conftest.py` File (fixtures of Pytest: browser, setup, teardown,log info, manager)</summary>

**Pytest fixtures: browser, setup, teardown,log info, manager**

- This file contains the fixtures of Pytest, which are used to setup and teardown the browser, log info, manager and browser.
- The fixtures are special functions that pytest provides to share setup and teardown code across tests, in other words, it is a way to share code across tests, for example:
   - if a test used a browser, it will be shared across all tests, so it will not be necessary to create a new browser for each test.
   - if a test used a teardown method, it will be shared across all tests, so it will not be necessary to create a new teardown for each test.

- This is a pytest convention to used a centralized configurations to share utilities across tests.

```
├── conftest.py     
├──                     

```

</details>

<details>

<summary>`requirements.txt` File (dependencies of the project,libraries, fixed versions for greater control and reproducibility)</summary>

**Dependencies of the project,libraries, fixed versions for greater control and reproducibility**

- This files allow to install the project dependencies in this case using `pip install -r requirements.txt`

```
├── requirements.txt       
|

```

</details>

<details>

<summary>`pytest.ini` File (configurations of Pytest) </summary> 

**Pytest configurations: report of Allure, testpath for define "test" as the root directory of the tests, marker for tag the test as: smoke,regression,integration**

- This file contains Pytest general configurations, such as:
   - report of Allure
   - testpath for define "test" as the root directory of the tests
   - marker for tag the test as: smoke,regression,integration


```
├── pytest.ini             
├──                      

```

**The markers used on this files can be adapt to the needs of the project, for example:**
- smoke: tests that validate the most important functionality of the application
- regression: tests that validate that the previous functionality of the application is still working after new changes
- n+1: tests that validate that the previous functionality of the application is still working after introduced fixes
- end_to_end: tests that validates a complete specific flows of the application

>The markers are useful to tag the tests and run commands, with a specific tag, for example:

```
pytest -m smoke
pytest -m regression
pytest -m integration
pytest -m end_to_end
pytest -m performance

```

</details>

----

### Unit Tests for page objects

As we are QA making an automation framework with robustness in mind and quality in mind,  code best practices, we need to validate that the page objects are working as expected, so we need to validate that the methods are calling the expected helpers and that the return values and control flow are working as intended.
<details>
<summary>`tools/` Directory - Unit Tests for page objects: </summary>

- The tools directory contains lightweight unit tests for page objects under `pages/` that do not require launching a real browser. They use `pytest` and monkeypatching to validate that:
- Methods call the expected `BaseActions` helpers (e.g., `send_keys`, `click`).
- Return values and control flow (e.g., URL checks) work as intended.
- Text extraction and visibility checks are wired to the configured locators.

```
├── tools/                   # Unit tests for page objects
│   ├── __init__.py
│   ├── conftest.py          # Pytest global fixtures for unit tests
|   |__README.md             # Explaination of the unit tests and how to run them
│   ├── test_account_user_unit.py
│   ├── test_login_unit.py
│   ├── test_page_form_submission_unit.py
│   ├── test_search_product_unit.py
│   └── test_login_unit.py

```

</details>

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  