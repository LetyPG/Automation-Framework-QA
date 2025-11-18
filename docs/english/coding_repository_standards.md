## Code Principles Design SOLID 

- **S: Single Responsibility**  
  Each class represents a single responsibility, using the Page Object Model, representing a single page of the site.
  
- **O: Open/Closed**  
  The framework is open to new functionalities without modifying the existing code.
  
- **L: Liskov Substitution**  
  Supports multiple browsers with an interchangeable structure in the driver management.
  
- **I: Interface Segregation**  
  The tests consume only what is necessary from each class, without depending on unnecessary implementations.
  Originally this principle is used to centralize common methods, which should be the most general, without modifying the existing code, without the need to create a base class as an abstract interface and that can be reused in different interfaces.
     - In this framework it was tried to maintain a bit of the same logic, creating an abstract interface that has the most generic methods and then in each interface the specific methods of the web page are implemented and the most generic are imported.
  
- **D: Dependency Inversion**  
  The tests do not depend directly on Selenium: the details such as selectors and browser configuration are abstracted in layers (`utils`, `.env`, fixtures).



## DRY (Don't Repeat Yourself)
Were created a base class for reusable operations, and a base class for reusable API operations:
- `BaseActions` for reusable operations
- `BaseAPIClient` define la estructura de los metodos HTTP

For scale the framework, the Paradigm used is the Page Object Model (POM), which is a design pattern that creates an object repository for web UI elements. Each web page is represented as a class, and the web elements are defined as variables within that class.
This architecture allows for easy maintenance and scalability of the framework.

### How to use the Page Object Model and the DRY principle

To use the Page Object Model and the DRY principle, the following steps should be followed:

1. Create a new page object class for the page you want to test.
2. Define the web elements as variables within the class.
3. Use the page object class in your tests.
4. Use the DRY principle to avoid code duplication.


### Framework Structure and Directories Conventions

The framework is structured in the following way:

- `README.md` file: Contains the README to understand the framework and eductative purposes in English and Spanish.
- `src/` directory: Contains the page objects used for this framawork, it was used `src` as name of the directory to follow the convention of names of directories in English, that indicates that it contains the source code of the project, so `src` is the abbreviation of `source`.
- `ci-cd/` directory: Contains the ci-cd files for the web site.
- `docs/` directory: Contains the documentation to understand the framework and eductative purposes.
- `features/` directory: Contains the features to apply BDD (Behavior Driven Development).
- `tests/` directory: Contains all test suites.
- `tools/` directory: Contains the tools for the web site, at this moment, it contains a tool to execute unit tests over the pages functions.
- `utils/` directory: Contains the utils for the web site.
- `config.py` file: Contains the configuration for the web site.
- `.env` file: Contains the environment variables for the web site.




  ## Next Steps
  
  - Review [Page Object Model](programming_standards.md) for detailed POM examples
  - Check [Coding Standards](coding_repository_standards.md) for SOLID principles
  - Check [Coding Standards](programming_paradigm.md) for SOLID principles
  - Explore [Best Practices](selenium.md) for QA guidelines
  - Explore [Best Practices](pytest.md) for QA guidelines
  - Read [Getting Started](getting_started.md) to run the framework

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
  