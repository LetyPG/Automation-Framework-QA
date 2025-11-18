"""
English:
Pytest Configuration and Fixtures for API Tests
This file contains shared fixtures that are automatically discovered by pytest
Placing fixtures here keeps test files clean and focused on test logic

Educational Notes:
- conftest.py is automatically discovered by pytest
- Fixtures defined here are available to all tests in this directory and subdirectories
- Promotes code reuse and separation of concerns
- Follows pytest best practices for test organization

Spanish:
Configuración de Pytest y Fixtures para Pruebas de API
Este archivo contiene fixtures compartidos que pytest descubre automáticamente
Colocar fixtures aquí mantiene los archivos de prueba limpios y enfocados en la lógica de prueba

Notas Educativas:
- conftest.py es descubierto automáticamente por pytest
- Los fixtures definidos aquí están disponibles para todas las pruebas en este directorio y subdirectorios
- Promueve la reutilización de código y separación de responsabilidades
- Sigue las mejores prácticas de pytest para organización de pruebas
"""

import pytest
import allure
from api.user_service_api import UserServiceAPI
from faker import Faker

# Initialize Faker for test data generation
fake = Faker()


# ==================== PYTEST FIXTURES ====================

@pytest.fixture(scope="module")
def user_api():
    """
    Fixture that provides UserServiceAPI instance for all tests
    Scope='module' means it's created once per test module
    
    Educational: Fixtures promote code reuse and clean test setup
    
    Returns:
        UserServiceAPI: Initialized API client instance
    """
    with allure.step("Initialize User Service API client"):
        api = UserServiceAPI()
        yield api  # Provide the API client to tests
        api.close()  # Cleanup after all tests


@pytest.fixture
def sample_user_data():
    """
    Fixture that generates random user data for testing
    Uses Faker library to generate realistic test data
    
    Educational: This demonstrates test data generation best practices
    Each test gets fresh random data, preventing test interdependencies
    
    Returns:
        dict: Dictionary containing random user data
    """
    return {
        'name': fake.name(),
        'username': fake.user_name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'website': fake.domain_name(),
        'address': {
            'street': fake.street_address(),
            'city': fake.city(),
            'zipcode': fake.zipcode()
        },
        'company': {
            'name': fake.company(),
            'catchPhrase': fake.catch_phrase()
        }
    }


@pytest.fixture
def user_schema():
    """
    JSON Schema for user validation
    
    Educational: Schema validation ensures API contracts are maintained
    This fixture provides a reusable schema definition for all tests
    
    Returns:
        dict: JSON Schema definition for user objects
    """
    return {
        "type": "object",
        "required": ["id", "name", "username", "email"],
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string", "format": "email"}
        }
    }


# ==================== PYTEST HOOKS (Optional - for educational purposes) ====================

def pytest_configure(config):
    """
    Pytest hook that runs before test collection
    Educational: Can be used for test environment setup
    """
    # Add custom markers
    config.addinivalue_line(
        "markers", "api: mark test as an API test"
    )
    config.addinivalue_line(
        "markers", "crud: mark test as a CRUD operation test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
