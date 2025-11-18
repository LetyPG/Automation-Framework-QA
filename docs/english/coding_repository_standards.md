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
- `BaseActions` for reusable operations
- `BaseAPIClient` define la estructura de los metodos HTTP


  ## Next Steps
  
  - Review [Page Object Model](programming_standards.md) for detailed POM examples
  - Check [Coding Standards](coding_repository_standards.md) for SOLID principles
  - Check [Coding Standards](programming_paradigm.md) for SOLID principles
  - Explore [Best Practices](selenium.md) for QA guidelines
  - Explore [Best Practices](pytest.md) for QA guidelines
  - Read [Getting Started](getting_started.md) to run the framework

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
  