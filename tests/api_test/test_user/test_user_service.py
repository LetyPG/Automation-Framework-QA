"""
English:
User Service API Tests - Comprehensive test suite for user API endpoints
This demonstrates API testing best practices with pytest framework

Educational Notes:
- Uses pytest fixtures from conftest.py for test setup and teardown
- Implements AAA pattern (Arrange, Act, Assert)
- Tests CRUD operations and edge cases
- Integrates with Allure for reporting
- Validates status codes, response structure, and data

Spanish:
Pruebas de API de Servicio de Usuario - Suite de pruebas completa para endpoints de API de usuario
Esto demuestra las mejores prácticas de pruebas de API con el framework pytest

Notas Educativas:
- Usa fixtures de pytest desde conftest.py para setup y teardown de pruebas
- Implementa patrón AAA (Arrange, Act, Assert)
- Prueba operaciones CRUD y casos límite
- Se integra con Allure para reportes
- Valida códigos de estado, estructura de respuesta y datos
"""

import pytest
import allure
import jsonschema
from jsonschema import validate
from faker import Faker

# Initialize Faker for additional test data if needed
fake = Faker()

# Note: Fixtures (user_api, sample_user_data, user_schema) are defined in conftest.py
# and are automatically discovered by pytest


# ==================== TEST CLASS: USER CRUD OPERATIONS ====================

@allure.feature("User Service API")
@allure.story("User CRUD Operations")
class TestUserCRUD:
    """
    Test class for User CRUD operations
    
    Educational: Organizing tests in classes helps group related tests
    """
    
    @allure.title("Test GET all users - Success scenario")
    @allure.description("Verify that API returns list of users successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_users_success(self, user_api):
        """
        Test: Get all users
        Expected: Status 200, list of users returned
        """
        # ARRANGE - Setup is done in fixture
        
        # ACT - Perform the action
        with allure.step("Send GET request to /users"):
            result = user_api.get_all_users()
        
        # ASSERT - Verify the results
        with allure.step("Verify response status code is 200"):
            assert result['status_code'] == 200, f"Expected 200, got {result['status_code']}"
        
        with allure.step("Verify response contains user data"):
            assert result['data'] is not None, "Response data should not be None"
            assert isinstance(result['data'], list), "Response should be a list"
            assert len(result['data']) > 0, "Should return at least one user"
        
        with allure.step("Verify first user has required fields"):
            first_user = result['data'][0]
            assert 'id' in first_user, "User should have 'id' field"
            assert 'name' in first_user, "User should have 'name' field"
            assert 'email' in first_user, "User should have 'email' field"
            assert 'username' in first_user, "User should have 'username' field"
        
        # Attach response to Allure report
        allure.attach(
            str(result['data']),
            name="Response Data",
            attachment_type=allure.attachment_type.JSON
        )
    
    @allure.title("Test GET all users with pagination")
    @allure.description("Verify that API supports pagination parameters")
    def test_get_all_users_with_limit(self, user_api):
        """
        Test: Get users with limit parameter
        Expected: Returns specified number of users
        """
        limit = 5
        
        with allure.step(f"Send GET request with limit={limit}"):
            result = user_api.get_all_users(params={'_limit': limit})
        
        with allure.step("Verify response status and data"):
            assert result['status_code'] == 200
            assert len(result['data']) == limit, f"Expected {limit} users, got {len(result['data'])}"
    
    @allure.title("Test GET user by ID - Success scenario")
    @allure.description("Verify that API returns specific user by ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_by_id_success(self, user_api, user_schema):
        """
        Test: Get specific user by ID
        Expected: Status 200, user data returned and validates against schema
        """
        user_id = 1
        
        with allure.step(f"Send GET request to /users/{user_id}"):
            result = user_api.get_user_by_id(user_id)
        
        with allure.step("Verify response status code is 200"):
            assert result['status_code'] == 200
        
        with allure.step("Verify user data is returned"):
            assert result['data'] is not None
            assert result['data']['id'] == user_id
        
        with allure.step("Validate response against JSON schema"):
            try:
                validate(instance=result['data'], schema=user_schema)
            except jsonschema.exceptions.ValidationError as e:
                pytest.fail(f"Schema validation failed: {e.message}")
    
    @allure.title("Test GET user by ID - User not found")
    @allure.description("Verify that API handles non-existent user ID correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_by_id_not_found(self, user_api):
        """
        Test: Get user with invalid ID
        Expected: Status 404 (Not Found)
        
        Educational: Testing negative scenarios is as important as positive ones
        """
        invalid_user_id = 99999
        
        with allure.step(f"Send GET request with invalid ID: {invalid_user_id}"):
            result = user_api.get_user_by_id(invalid_user_id)
        
        with allure.step("Verify response status code is 404"):
            assert result['status_code'] == 404, f"Expected 404, got {result['status_code']}"
    
    @allure.title("Test POST create new user")
    @allure.description("Verify that API can create a new user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_success(self, user_api, sample_user_data):
        """
        Test: Create new user
        Expected: Status 201, user created with ID
        """
        with allure.step("Send POST request with user data"):
            result = user_api.create_user(sample_user_data)
        
        with allure.step("Verify response status code is 201"):
            assert result['status_code'] == 201, f"Expected 201, got {result['status_code']}"
        
        with allure.step("Verify created user has ID assigned"):
            assert result['data'] is not None
            assert 'id' in result['data'], "Created user should have an ID"
        
        with allure.step("Verify created user data matches input"):
            assert result['data']['name'] == sample_user_data['name']
            assert result['data']['email'] == sample_user_data['email']
        
        allure.attach(
            str(result['data']),
            name="Created User",
            attachment_type=allure.attachment_type.JSON
        )
    
    @allure.title("Test PUT update user - Full update")
    @allure.description("Verify that API can fully update user data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_success(self, user_api):
        """
        Test: Update existing user (PUT)
        Expected: Status 200, user data updated
        """
        user_id = 1
        updated_data = {
            'id': user_id,
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email()
        }
        
        with allure.step(f"Send PUT request to update user {user_id}"):
            result = user_api.update_user(user_id, updated_data)
        
        with allure.step("Verify response status code is 200"):
            assert result['status_code'] == 200
        
        with allure.step("Verify user data was updated"):
            assert result['data'] is not None
            assert result['data']['id'] == user_id
    
    @allure.title("Test PATCH partial update user")
    @allure.description("Verify that API can partially update user data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_partial_update_user_success(self, user_api):
        """
        Test: Partially update user (PATCH)
        Expected: Status 200, only specified fields updated
        """
        user_id = 1
        partial_data = {
            'email': fake.email()
        }
        
        with allure.step(f"Send PATCH request to update user {user_id} email"):
            result = user_api.partial_update_user(user_id, partial_data)
        
        with allure.step("Verify response status code is 200"):
            assert result['status_code'] == 200
        
        with allure.step("Verify user data contains updated field"):
            assert result['data'] is not None
            assert result['data']['id'] == user_id
    
    @allure.title("Test DELETE user")
    @allure.description("Verify that API can delete a user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user_success(self, user_api):
        """
        Test: Delete user
        Expected: Status 200
        """
        user_id = 1
        
        with allure.step(f"Send DELETE request for user {user_id}"):
            result = user_api.delete_user(user_id)
        
        with allure.step("Verify response status code is 200"):
            assert result['status_code'] == 200, f"Expected 200, got {result['status_code']}"


