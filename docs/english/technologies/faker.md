# Faker - Dynamic Test Data Generation

## What is Faker?

**Faker** is a Python library that generates fake (but realistic) data for testing purposes. It can create names, emails, addresses, phone numbers, and much more.

**Official Documentation**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)


## Summary

Faker enhances this framework with dynamic test data:
- **Realistic data** - Names, emails, addresses that look real
- **Randomization** - Different data each run
- **Localization** - Support for multiple languages/regions
- **Easy to use** - Simple API, extensive providers
- **Test coverage** - Better edge case detection
## Faker vs Manual Test Data

| Approach | Pros | Cons |
|----------|------|------|
| **Faker** | Realistic, randomized, no duplicates | Harder to debug specific failures |
| **Hardcoded** | Predictable, easy to debug | Unrealistic, duplicates, maintenance |
| **Hybrid** | Best of both worlds | Requires planning |

**This framework uses Faker** for realistic, dynamic test data.


---

## Why Faker for Test Automation?

### Advantages

1. **Realistic Test Data**
   - Generates data that looks real
   - Avoids hardcoded test values
   - Better test coverage

2. **Randomization**
   - Different data each test run
   - Catches edge cases
   - Prevents test data pollution

3. **Localization Support**
   - Generate data in multiple languages
   - Test internationalization
   - Region-specific formats

4. **Wide Range of Data Types**
   - Personal info (names, emails, phones)
   - Addresses and locations
   - Internet data (URLs, IPs, user agents)
   - Dates, numbers, text

5. **Easy to Use**
   - Simple API
   - Chainable methods
   - Extensible with custom providers

---

## Installation

```bash
pip install faker
```

---

## Basic Usage

```python
from faker import Faker

# Create Faker instance
fake = Faker()

# Generate data
name = fake.name()                    # "John Smith"
email = fake.email()                  # "john.smith@example.com"
address = fake.address()              # "123 Main St, City, State 12345"
phone = fake.phone_number()           # "+1-555-123-4567"
```

---

## How This Framework Uses Faker

### Data Generator (`utils/data_generator.py`)

Centralized test data generation:

```python
from faker import Faker
import random

class DataGenerator:
    """Generates dynamic test data using Faker."""
    
    def __init__(self, locale='en_US'):
        self.fake = Faker(locale)
    
    def generate_user(self):
        """Generate complete user data."""
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.generate_password(),
            "phone": self.fake.phone_number(),
            "address": self.fake.address()
        }
    
    def generate_password(self, length=12):
        """Generate secure password."""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
        return ''.join(random.choice(chars) for _ in range(length))
    
    def generate_email(self, domain="example.com"):
        """Generate email with specific domain."""
        username = self.fake.user_name()
        return f"{username}@{domain}"
```

### Usage in Tests

```python
from utils.data_generator import DataGenerator

def test_user_registration(browser):
    # Generate test data
    generator = DataGenerator()
    user_data = generator.generate_user()
    
    # Use in test
    page = RegistrationPage(browser)
    page.fill_form(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
        password=user_data["password"]
    )
    page.submit()
    
    assert page.is_success_message_visible()
```

**Benefits**:
- Fresh data every test run
- No hardcoded values
- Realistic test scenarios
- Avoid duplicate data issues

---

## Common Faker Providers

### Personal Information

```python
fake.name()                    # "Jane Doe"
fake.first_name()              # "Jane"
fake.last_name()               # "Doe"
fake.name_male()               # "John Smith"
fake.name_female()             # "Mary Johnson"
fake.prefix()                  # "Dr."
fake.suffix()                  # "Jr."
```

### Internet Data

```python
fake.email()                   # "user@example.com"
fake.safe_email()              # "user@example.org" (safe domains)
fake.free_email()              # "user@gmail.com"
fake.company_email()           # "user@company.com"
fake.user_name()               # "john_smith"
fake.password()                # "aB3$xY9#kL2@"
fake.url()                     # "https://example.com"
fake.ipv4()                    # "192.168.1.1"
fake.mac_address()             # "00:1B:63:84:45:E6"
```

### Address and Location

```python
fake.address()                 # "123 Main St\nCity, State 12345"
fake.street_address()          # "123 Main St"
fake.city()                    # "New York"
fake.state()                   # "California"
fake.state_abbr()              # "CA"
fake.zipcode()                 # "12345"
fake.country()                 # "United States"
fake.latitude()                # "40.7128"
fake.longitude()               # "-74.0060"
```

### Phone Numbers

```python
fake.phone_number()            # "+1-555-123-4567"
fake.msisdn()                  # "1234567890" (mobile)
```

### Dates and Times

```python
fake.date()                    # "2023-05-15"
fake.date_of_birth()           # "1990-03-20"
fake.date_between(start_date='-30d', end_date='today')  # Recent date
fake.future_date()             # Future date
fake.past_date()               # Past date
fake.time()                    # "14:30:00"
fake.iso8601()                 # "2023-05-15T14:30:00"
```

### Text and Lorem Ipsum

```python
fake.text()                    # Paragraph of text
fake.sentence()                # "Lorem ipsum dolor sit amet."
fake.word()                    # "lorem"
fake.words(5)                  # ["lorem", "ipsum", "dolor", "sit", "amet"]
fake.paragraph()               # Full paragraph
```

### Numbers

```python
fake.random_int(min=1, max=100)        # 42
fake.random_digit()                    # 7
fake.random_number(digits=5)           # 12345
fake.pyfloat(left_digits=2, right_digits=2)  # 12.34
```

### Company and Job

```python
fake.company()                 # "Acme Corporation"
fake.job()                     # "Software Engineer"
fake.bs()                      # "synergize innovative solutions"
```

### Credit Cards (Test Data Only!)

```python
fake.credit_card_number()      # "4532123456789012"
fake.credit_card_provider()    # "Visa"
fake.credit_card_expire()      # "12/25"
fake.credit_card_security_code()  # "123"
```

---

## Advanced Features

### Localization

Generate data in different languages:

```python
# English (US)
fake_us = Faker('en_US')
print(fake_us.address())  # US format

# Spanish
fake_es = Faker('es_ES')
print(fake_es.name())     # Spanish name

# French
fake_fr = Faker('fr_FR')
print(fake_fr.address())  # French address

# Multiple locales
fake_multi = Faker(['en_US', 'es_ES', 'fr_FR'])
print(fake_multi.name())  # Random from any locale
```

### Seeding for Reproducibility

Generate same data across runs:

```python
# Set seed for reproducible data
Faker.seed(12345)

fake1 = Faker()
print(fake1.name())  # Always same name

# Reset and use same seed
Faker.seed(12345)
fake2 = Faker()
print(fake2.name())  # Same name as fake1
```

**Use Case**: Debugging specific test failures

### Custom Providers

Create your own data generators:

```python
from faker.providers import BaseProvider

class CustomProvider(BaseProvider):
    def product_name(self):
        products = ["Laptop", "Phone", "Tablet", "Monitor"]
        return self.random_element(products)
    
    def product_price(self):
        return f"${self.random_int(100, 2000)}.99"

# Add to Faker
fake = Faker()
fake.add_provider(CustomProvider)

print(fake.product_name())  # "Laptop"
print(fake.product_price())  # "$599.99"
```

### Unique Values

Ensure no duplicates:

```python
fake = Faker()

# Generate unique emails
for _ in range(10):
    email = fake.unique.email()
    print(email)  # All different

# Reset unique tracker
fake.unique.clear()
```

---

## Practical Examples for This Framework

### 1. User Registration Test

```python
def test_user_registration(browser):
    generator = DataGenerator()
    
    # Generate unique user
    user = generator.generate_user()
    
    page = RegistrationPage(browser)
    page.open(Configuration.SUBMISSION_URL)
    page.fill_registration_form(
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"],
        password=user["password"]
    )
    page.submit()
    
    assert page.is_success_message_visible()
```

### 2. Multiple User Creation

```python
def test_create_multiple_users(browser):
    generator = DataGenerator()
    
    for _ in range(5):
        user = generator.generate_user()
        create_user(browser, user)
        verify_user_created(browser, user["email"])
```

### 3. Form Validation with Edge Cases

```python
def test_email_validation(browser):
    generator = DataGenerator()
    
    # Test with various email formats
    emails = [
        generator.fake.email(),           # Standard
        generator.fake.free_email(),      # Free provider
        generator.fake.company_email(),   # Company
        "invalid-email",                  # Invalid
        "",                               # Empty
    ]
    
    for email in emails:
        test_email_input(browser, email)
```

### 4. Search with Random Queries

```python
def test_product_search(browser):
    generator = DataGenerator()
    
    # Generate search terms
    search_terms = [
        generator.fake.word(),
        generator.fake.sentence(nb_words=3),
        "jacket",  # Known product
    ]
    
    for term in search_terms:
        page = SearchPage(browser)
        page.search(term)
        results = page.get_results()
        # Verify results
```

---

## Best Practices

### 1. Centralize Data Generation

```python
# Good - Centralized in DataGenerator
generator = DataGenerator()
user = generator.generate_user()

# Avoid - Scattered throughout tests
fake = Faker()
name = fake.name()  # In test 1
email = fake.email()  # In test 2
```

### 2. Use Meaningful Data

```python
# Good - Realistic data
email = fake.email()  # "john.smith@example.com"

# Avoid - Obvious fake data
email = "test@test.com"  # Less realistic
```

### 3. Combine with Real Data

```python
# Mix Faker with real test data
user = {
    "first_name": fake.first_name(),  # Random
    "last_name": fake.last_name(),    # Random
    "email": fake.email(),            # Random
    "country": "United States",       # Fixed for test
    "role": "customer"                # Fixed for test
}
```

### 4. Handle Unique Constraints

```python
# For fields that must be unique
def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    username = fake.user_name()
    return f"{username}_{timestamp}@example.com"
```

---

## Troubleshooting

### Issue: Same Data Every Run

**Solution**: Don't set seed (or use different seeds)
```python
# Avoid for random data
Faker.seed(12345)

# Or use timestamp as seed
import time
Faker.seed(int(time.time()))
```

### Issue: Need Specific Format

**Solution**: Customize with Python
```python
# Custom email format
username = fake.user_name()
email = f"{username}@mycompany.com"

# Custom phone format
area_code = fake.random_int(200, 999)
number = fake.random_int(1000000, 9999999)
phone = f"({area_code}) {number}"
```

### Issue: Locale Not Working

**Solution**: Install locale-specific data
```python
# Some locales need extra packages
pip install faker[locales]
```

---

## Learning Resources

### Official Documentation
- **Faker Docs**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)
- **Providers List**: [https://faker.readthedocs.io/en/master/providers.html](https://faker.readthedocs.io/en/master/providers.html)

### Tutorials
- **Real Python - Faker Guide**: [https://realpython.com/](https://realpython.com/)
- **GitHub Examples**: [https://github.com/joke2k/faker](https://github.com/joke2k/faker)

---

**Next Steps**:
- Review `utils/data_generator.py` for implementation
- Experiment with different Faker providers
- Add custom providers for domain-specific data
- Check [Best Practices](../automation_strategy.md) for data generation tips


**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
