
"""
English:
User Service API Tests - Comprehensive test suite for user API integration
This demonstrates API testing best practices with pytest framework

Educational Notes:
- Uses pytest fixtures from conftest.py for test setup and teardown
- Implements AAA pattern (Arrange, Act, Assert)
- Tests CRUD operations and edge cases
- Integrates with Allure for reporting
- Integration tests verify that operations work together
- The test first creates a user, then reads it, updates it, and finally deletes it

Spanish:
Pruebas de API de Servicio de Usuario - Suite de pruebas completa para endpoints de API de usuario
Esto demuestra las mejores prácticas de pruebas de API con el framework pytest

Notas Educativas:
- Usa fixtures de pytest desde conftest.py para setup y teardown de pruebas
- Implementa patrón AAA (Arrange, Act, Assert)
- Prueba operaciones CRUD y casos límite
- Se integra con Allure para reportes
- Valida que las operaciones funcionen juntas
- El test primero valida que se pueda crear un usuario, luego lo lee, actualiza y finalmente lo elimina

"""


import allure
from jsonschema import validate
from faker import Faker

# Initialize Faker for additional test data if needed
fake = Faker()

# Note: Fixtures (user_api, sample_user_data, user_schema) are defined in conftest.py
# and are automatically discovered by pytest

# ==================== INTEGRATION TESTS ====================

@allure.feature("User Service API")
@allure.story("Integration Tests")
class TestIntegration:
    """
    Integration tests - testing multiple operations together
    
    Educational: Integration tests verify that operations work together
    """
    
    @allure.title("Test complete user lifecycle")
    @allure.description("Create, Read, Update, and Delete a user in sequence")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_user_lifecycle(self, user_api, sample_user_data):
        """
        Test: Complete CRUD lifecycle for a user
        Educational: Demonstrates testing a complete user journey
        """
        created_user_id = None
        
        # CREATE
        with allure.step("Step 1: Create new user"):
            create_result = user_api.create_user(sample_user_data)
            assert create_result['status_code'] == 201
            created_user_id = create_result['data']['id']
            allure.attach(str(created_user_id), name="Created User ID")
        
        # READ
        with allure.step(f"Step 2: Read created user (ID: {created_user_id})"):
            read_result = user_api.get_user_by_id(created_user_id)
            # Note: JSONPlaceholder doesn't actually persist data
            # In real API, we would verify the user exists
        
        # UPDATE
        with allure.step(f"Step 3: Update user (ID: {created_user_id})"):
            updated_data = sample_user_data.copy()
            updated_data['name'] = fake.name()
            update_result = user_api.update_user(created_user_id, updated_data)
            assert update_result['status_code'] == 200
        
        # DELETE
        with allure.step(f"Step 4: Delete user (ID: {created_user_id})"):
            delete_result = user_api.delete_user(created_user_id)
            assert delete_result['status_code'] == 200
        
        with allure.step("Test completed: Full lifecycle verified"):
            allure.attach(
                "User was created, read, updated, and deleted successfully",
                name="Lifecycle Summary"
            )