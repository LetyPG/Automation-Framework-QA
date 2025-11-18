
"""
English:
User Service API - Specific implementation for User-related API endpoints
This class extends BaseAPIClient following the Open/Closed Principle
It demonstrates how to create service-specific API clients for testing

Educational Notes:
- Inherits from BaseAPIClient to reuse HTTP methods
- Encapsulates business logic for user operations (CRUD)
- Uses type hints for better code documentation
- Provides methods that map to real API endpoints
- Example uses JSONPlaceholder as a free testing API

Spanish:
API de Servicio de Usuario - Implementación específica para endpoints API relacionados con usuarios
Esta clase extiende BaseAPIClient siguiendo el Principio Abierto/Cerrado
Demuestra cómo crear clientes API específicos de servicio para pruebas

Notas Educativas:
- Hereda de BaseAPIClient para reutilizar métodos HTTP
- Encapsula lógica de negocio para operaciones de usuario (CRUD)
- Usa type hints para mejor documentación del código
- Proporciona métodos que mapean a endpoints API reales
- Ejemplo usa JSONPlaceholder como API de prueba gratuita
"""

from api.base_api_client import BaseAPIClient
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()


class UserServiceAPI(BaseAPIClient):
    """
    User Service API Client - Handles all user-related API operations
    
    This demonstrates:
    - Inheritance (extends BaseAPIClient)
    - Encapsulation (hides HTTP implementation details)
    - Single Responsibility (only handles user operations)
    """
    
    def __init__(self, base_url: Optional[str] = None):
        """
        Initialize User Service API client
        
        Args:
            base_url (str): Base URL for the API. If None, reads from environment variable
        """
        # Read from environment or use default test API
        if base_url is None:
            base_url = os.getenv('API_BASE_URL', 'https://jsonplaceholder.typicode.com')
        
        super().__init__(base_url)
        self.logger.info(f"UserServiceAPI initialized with base URL: {base_url}")
    
    # ==================== USER CRUD OPERATIONS ====================
    
    def get_all_users(self, params: Optional[Dict] = None) -> Dict:
        """
        Get all users
        
        Args:
            params (dict): Optional query parameters (e.g., pagination, filters)
            
        Returns:
            dict: Response containing user list
            
        Example:
            users = user_api.get_all_users()
            users = user_api.get_all_users({'_limit': 5})
        """
        response = self.get('/users', params=params)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def get_user_by_id(self, user_id: int) -> Dict:
        """
        Get specific user by ID
        
        Args:
            user_id (int): User ID
            
        Returns:
            dict: Response containing user data
            
        Example:
            user = user_api.get_user_by_id(1)
        """
        response = self.get(f'/users/{user_id}')
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def create_user(self, user_data: Dict) -> Dict:
        """
        Create a new user
        
        Args:
            user_data (dict): User information (name, email, etc.)
            
        Returns:
            dict: Response containing created user data
            
        Example:
            user_data = {
                'name': 'John Doe',
                'username': 'johndoe',
                'email': 'john@example.com'
            }
            result = user_api.create_user(user_data)
        """
        response = self.post('/users', json=user_data)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code in [200, 201] else None,
            'response': response
        }
    
    def update_user(self, user_id: int, user_data: Dict) -> Dict:
        """
        Update existing user (full update - PUT)
        
        Args:
            user_id (int): User ID
            user_data (dict): Complete user information
            
        Returns:
            dict: Response containing updated user data
            
        Example:
            updated_data = {
                'id': 1,
                'name': 'Jane Doe',
                'username': 'janedoe',
                'email': 'jane@example.com'
            }
            result = user_api.update_user(1, updated_data)
        """
        response = self.put(f'/users/{user_id}', json=user_data)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def partial_update_user(self, user_id: int, user_data: Dict) -> Dict:
        """
        Partially update user (PATCH)
        
        Args:
            user_id (int): User ID
            user_data (dict): Partial user information (only fields to update)
            
        Returns:
            dict: Response containing updated user data
            
        Example:
            partial_data = {'email': 'newemail@example.com'}
            result = user_api.partial_update_user(1, partial_data)
        """
        response = self.patch(f'/users/{user_id}', json=user_data)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def delete_user(self, user_id: int) -> Dict:
        """
        Delete a user
        
        Args:
            user_id (int): User ID
            
        Returns:
            dict: Response containing deletion result
            
        Example:
            result = user_api.delete_user(1)
        """
        response = self.delete(f'/users/{user_id}')
        return {
            'status_code': response.status_code,
            'data': None,
            'response': response
        }
    
    # ==================== ADDITIONAL USER OPERATIONS ====================
    
    def get_user_posts(self, user_id: int) -> Dict:
        """
        Get all posts by a specific user
        
        Args:
            user_id (int): User ID
            
        Returns:
            dict: Response containing user's posts
            
        Example:
            posts = user_api.get_user_posts(1)
        """
        response = self.get(f'/users/{user_id}/posts')
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def get_user_albums(self, user_id: int) -> Dict:
        """
        Get all albums by a specific user
        
        Args:
            user_id (int): User ID
            
        Returns:
            dict: Response containing user's albums
            
        Example:
            albums = user_api.get_user_albums(1)
        """
        response = self.get(f'/users/{user_id}/albums')
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def get_user_todos(self, user_id: int, completed: Optional[bool] = None) -> Dict:
        """
        Get all todos by a specific user
        
        Args:
            user_id (int): User ID
            completed (bool): Filter by completion status (optional)
            
        Returns:
            dict: Response containing user's todos
            
        Example:
            todos = user_api.get_user_todos(1)
            completed_todos = user_api.get_user_todos(1, completed=True)
        """
        params = {}
        if completed is not None:
            params['completed'] = str(completed).lower()
        
        response = self.get(f'/users/{user_id}/todos', params=params)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    # ==================== SEARCH AND FILTER OPERATIONS ====================
    
    def search_users_by_email(self, email: str) -> Dict:
        """
        Search users by email
        
        Args:
            email (str): Email to search for
            
        Returns:
            dict: Response containing matching users
            
        Example:
            users = user_api.search_users_by_email('Sincere@april.biz')
        """
        response = self.get('/users', params={'email': email})
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def search_users_by_username(self, username: str) -> Dict:
        """
        Search users by username
        
        Args:
            username (str): Username to search for
            
        Returns:
            dict: Response containing matching users
            
        Example:
            users = user_api.search_users_by_username('Bret')
        """
        response = self.get('/users', params={'username': username})
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }