
"""
English:
User Service API Tests - Comprehensive test suite for user data validation, in this case was used the user ID parameter to validate the data
This demonstrates API testing best practices with pytest framework

Educational Notes:
- Uses pytest fixtures from conftest.py for test setup and teardown, following pytest best practices
- Integrates with Allure for reporting
- Validates status codes, response structure, and data type 

Spanish:
Pruebas de API de Servicio de Usuario - Suite de pruebas completa para endpoints parametrizados, en este caso se utilizo el parametro ID de usuario para validar los datos
Esto demuestra las mejores prácticas de pruebas de API con el framework pytest

Notas Educativas:
- Usa fixtures de pytest desde conftest.py para setup y teardown de pruebas, siguiendo las mejores prácticas de pytest
- Se integra con Allure para reportes
- Valida códigos de estado, estructura de respuesta y tipo de datos para ID de usuario
"""



import pytest
import allure
from jsonschema import validate
from faker import Faker

# Initialize Faker for additional test data if needed
fake = Faker()

# Note: Fixtures (user_api, sample_user_data, user_schema) are defined in conftest.py
# and are automatically discovered by pytest


# ==================== PARAMETRIZED TESTS ====================

@allure.feature("User Service API")
@allure.story("Parametrized Tests")
class TestParametrized:
    """
    Parametrized tests - running same test with different data
    
    Educational: Parametrized tests reduce code duplication
    """
    
    @allure.title("Test multiple user IDs - Success scenarios")
    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
    def test_get_multiple_users_by_id(self, user_api, user_id):
        """
        Test: Get users by different IDs
        Educational: Demonstrates parametrized testing
        """
        with allure.step(f"Get user with ID: {user_id}"):
            result = user_api.get_user_by_id(user_id)
        
        with allure.step("Verify response"):
            assert result['status_code'] == 200
            assert result['data']['id'] == user_id
    
    @allure.title("Test invalid user IDs - Error scenarios")
    @pytest.mark.parametrize("invalid_id", [0, -1, 99999, 'abc'])
    def test_get_user_invalid_ids(self, user_api, invalid_id):
        """
        Test: Get users with invalid IDs
        Educational: Testing boundary and error conditions
        """
        with allure.step(f"Attempt to get user with invalid ID: {invalid_id}"):
            result = user_api.get_user_by_id(invalid_id)
        
        with allure.step("Verify error response"):
            assert result['status_code'] in [400, 404], \
                f"Expected error status, got {result['status_code']}"


