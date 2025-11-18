# QA Automation Framework - Documentation Index

Welcome to the comprehensive documentation for this educational QA Automation Framework. This framework demonstrates best practices for UI test automation using Python, Selenium WebDriver, and Pytest.

---

## 📚 Documentation Structure

### Getting Started
- **[Getting Started Guide](getting_started.md)** - Step-by-step setup and first test execution
- **[Project Overview](project_overview.md)** - Complete project structure and SOLID principles application
- **[Environment Configuration](.env_example.txt)** - Example .env file with all required variables

### Core Concepts
- **[Automation Strategy](automation_strategy.md)** - Why Page Object Model, fixtures, and architectural decisions
- **[Coding Standards](coding_repository_standards.md)** - SOLID principles and design patterns applied
- **[Best Practices](best_practices.md)** - QA automation guidelines and recommendations

### Technologies Used
- **[Python](technologies/python.md)** - Language fundamentals and virtual environments
- **[Selenium WebDriver](technologies/selenium.md)** - Browser automation and WebDriver concepts
- **[Pytest](technologies/pytest.md)** - Test framework, fixtures, and markers
- **[Faker](technologies/faker.md)** - Dynamic test data generation
- **[Allure Reports](technologies/allure.md)** - Test reporting and visualization

### Framework Components
- **[Page Object Model](page_object_model.md)** - POM pattern implementation
- **[Base Actions](base_actions.md)** - Reusable Selenium operations
- **[Configuration Management](configuration.md)** - Environment variables and locators
- **[Unit Tests](../tools/README.md)** - Testing page objects without browser

---

## Quick Links

### For Beginners
1. Start with [Getting Started Guide](getting_started.md)
2. Understand [Project Overview](project_overview.md)
3. Learn about [Page Object Model](page_object_model.md)
4. Review [Best Practices](best_practices.md)

### For Experienced QA Engineers
1. Review [Automation Strategy](automation_strategy.md)
2. Examine [Coding Standards](coding_repository_standards.md)
3. Explore [Unit Tests](../tools/README.md)


---

## 🌐 Official Documentation Links

- **Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Selenium**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- **Pytest**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **Faker**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)
- **Allure**: [https://docs.qameta.io/allure/](https://docs.qameta.io/allure/)

---

## About This Framework

This is an **educational project** designed to demonstrate:
- SOLID principles in test automation
- Page Object Model (POM) design pattern
- Pytest fixtures and markers
- Configuration management with .env
- Unit testing for page objects
- Browser driver management with Selenium Manager
- Dynamic test data with Faker
- Comprehensive reporting with Allure

**Target Audience**: QA Engineers, Test Automation beginners, and anyone learning Python-based UI automation.

**Note**: This is a demo project for educational purposes, not production-ready code.

---

## Repository Structure

```
Automation-Framework-QA/
├── docs/                    # Documentation (you are here!)
├── driver/                  # Optional browser drivers
├── pages/                   # Page Object classes
├── tests/                   # Test cases modules grouped by testing strategy as diffrent suite tests (smoke, regression, api, e2e, etc)
├── tools/                   # Unit tests for page objects
├── utils/                   # Utilities (config, data, browser, assertions)
├── .env                     # Environment variables (not in repo)
├── conftest.py              # Pytest global fixtures
├── pytest.ini               # Pytest configuration
└── requiriments.txt         # Python dependencies
```

---

## Contributing

This is an educational framework. Feel free to:
- Fork and experiment
- Suggest improvements
- Report issues
- Share with others learning QA automation

---

**Version**: 0.1.2  
**Last Updated**: 2025  
**Language**: English | [Español](../spanish/index.md)
