
"""
English:
User Service API Tests - Comprehensive test suite for search and filter functionality
This demonstrates API testing best practices with pytest framework

Educational Notes:
- Uses pytest fixtures from conftest.py for test setup and teardown
- Integrates with Allure for reporting


Spanish:
Pruebas de API de Servicio de Usuario - Suite de pruebas completa para búsqueda y filtrado de endpoints de API de usuario
Esto demuestra las mejores prácticas de pruebas de API con el framework pytest

Notas Educativas:
- Usa fixtures de pytest desde conftest.py para setup y teardown de pruebas
- Se integra con Allure para reportes
"""

import allure       
from faker import Faker

# Initialize Faker for additional test data if needed
fake = Faker()

# Note: Fixtures (user_api, sample_user_data, user_schema) are defined in conftest.py
# and are automatically discovered by pytest


# ==================== TEST CLASS: SEARCH AND FILTER ====================

class TestUserSearchFilter:
    """
    Tests for search and filter functionality
    
    Educational: Demonstrates testing of query parameters and filtering
    """
    
    @allure.title("Test search users by email")
    @allure.description("Verify that API can search users by email address")
    def test_search_users_by_email(self, user_api):
        """
        Test: Search users by email
        Expected: Status 200, matching users returned
        """
        # First get a user to know a valid email
        with allure.step("Get first user to obtain valid email"):
            users = user_api.get_all_users(params={'_limit': 1})
            test_email = users['data'][0]['email']
        
        with allure.step(f"Search for user with email: {test_email}"):
            result = user_api.search_users_by_email(test_email)
        
        with allure.step("Verify search results"):
            assert result['status_code'] == 200
            assert len(result['data']) >= 1
            assert result['data'][0]['email'] == test_email
    
    @allure.title("Test search users by username")
    @allure.description("Verify that API can search users by username")
    def test_search_users_by_username(self, user_api):
        """
        Test: Search users by username
        Expected: Status 200, matching users returned
        """
        # First get a user to know a valid username
        with allure.step("Get first user to obtain valid username"):
            users = user_api.get_all_users(params={'_limit': 1})
            test_username = users['data'][0]['username']
        
        with allure.step(f"Search for user with username: {test_username}"):
            result = user_api.search_users_by_username(test_username)
        
        with allure.step("Verify search results"):
            assert result['status_code'] == 200
            assert len(result['data']) >= 1
            assert result['data'][0]['username'] == test_username

