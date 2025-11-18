# Base API Client - Provides reusable HTTP methods for API testing
# Clase Base para clientes API - Proporciona métodos HTTP reutilizables para pruebas de API

import requests
import logging
from typing import Dict, Optional, Any
import json


# Configure logging for educational purposes - helps trace API calls
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class BaseAPIClient:    
    def __init__(self, base_url: str, timeout: int = 30):
        """
        English: Initialize the API client
        
        Args:
            base_url (str): Base URL for the API (e.g., 'https://api.example.com')
            timeout (int): Default timeout for requests in seconds

        Returns:
            None

        Spanish: Inicializa el cliente API
        
        Argumentos que recibe la clase:
            base_url (str): URL base para la API (e.g., 'https://api.example.com')
            timeout (int): Tiempo de espera predeterminado para las peticiones en segundos

        Retorna:
            None
        """
        self.base_url = base_url.rstrip('/')  # Remove trailing slash # Elimina el slash final
        self.timeout = timeout
        self.session = requests.Session()  # Session for connection pooling # Sesión para el pooling de conexiones
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Default headers - can be overridden # Encabezados por defecto - pueden ser sobrescritos
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _build_url(self, endpoint: str) -> str:
        """
        Build complete URL from base URL and endpoint # Construye la URL completa a partir de la URL base y el endpoint
        
        Args:
            endpoint (str): API endpoint (e.g., '/users' or 'users')
            
        Returns:
            str: Complete URL
        """
        endpoint = endpoint.lstrip('/')  # Remove leading slash
        return f"{self.base_url}/{endpoint}"
    
    def _log_request(self, method: str, url: str, **kwargs):
        """
        Log request details for debugging (educational purpose)
        Registra los detalles de la petición para depuración (propósito educativo)
        
        """
        self.logger.info(f"Request: {method} {url}")
        if 'json' in kwargs:
            self.logger.debug(f"Request Body: {json.dumps(kwargs['json'], indent=2)}")
    
    def _log_response(self, response: requests.Response):
        """Log response details for debugging (as before)
         Registra los detalles de la respuesta para depuración (como antes)
         """
        self.logger.info(f"Response: {response.status_code} {response.reason}")
        try:
            self.logger.debug(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except ValueError:
            self.logger.debug(f"Response Body: {response.text}")
    
    def set_header(self, key: str, value: str):
        """
        Set a custom header for all requests # Establece un encabezado personalizado para todas las peticiones
        
        Args:
            key (str): Header name
            value (str): Header value
        """
        self.session.headers[key] = value
        self.logger.info(f"Header set: {key}")
    
    def set_auth_token(self, token: str, token_type: str = "Bearer"):
        """
        Set authentication token # Establece el token de autenticación
        
        Args:
            token (str): Authentication token
            token_type (str): Token type (Bearer, Basic, etc.)
        """
        self.set_header('Authorization', f'{token_type} {token}')
    
    def get(self, endpoint: str, params: Optional[Dict] = None, 
            headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        Perform GET request # Realiza una petición GET
        
        Args:
            endpoint (str): API endpoint
            params (dict): Query parameters
            headers (dict): Additional headers for this request
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: Response object
        """
        url = self._build_url(endpoint)
        self._log_request('GET', url, params=params)
        
        response = self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        
        self._log_response(response)
        return response
    
    def post(self, endpoint: str, json: Optional[Dict] = None, 
             data: Optional[Any] = None, headers: Optional[Dict] = None, 
             **kwargs) -> requests.Response:
        """
        Perform POST request # Realiza una petición POST
        
        Args:
            endpoint (str): API endpoint
            json (dict): JSON payload
            data: Form data or raw data
            headers (dict): Additional headers for this request
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: Response object
        """
        url = self._build_url(endpoint)
        self._log_request('POST', url, json=json, data=data)
        
        response = self.session.post(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        
        self._log_response(response)
        return response
    
    def put(self, endpoint: str, json: Optional[Dict] = None, 
            data: Optional[Any] = None, headers: Optional[Dict] = None, 
            **kwargs) -> requests.Response:
        """
        Perform PUT request # Realiza una petición PUT
        
        Args:
            endpoint (str): API endpoint
            json (dict): JSON payload
            data: Form data or raw data
            headers (dict): Additional headers for this request
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: Response object
        """
        url = self._build_url(endpoint)
        self._log_request('PUT', url, json=json, data=data)
        
        response = self.session.put(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        
        self._log_response(response)
        return response
    
    def patch(self, endpoint: str, json: Optional[Dict] = None, 
              data: Optional[Any] = None, headers: Optional[Dict] = None, 
              **kwargs) -> requests.Response:
        """
        Perform PATCH request # Realiza una petición PATCH
        
        Args:
            endpoint (str): API endpoint
            json (dict): JSON payload
            data: Form data or raw data
            headers (dict): Additional headers for this request
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: Response object
        """
        url = self._build_url(endpoint)
        self._log_request('PATCH', url, json=json, data=data)
        
        response = self.session.patch(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        
        self._log_response(response)
        return response
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None, 
               **kwargs) -> requests.Response:
        """
        Perform DELETE request # Realiza una petición DELETE
        
        Args:
            endpoint (str): API endpoint
            headers (dict): Additional headers for this request
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: Response object
        """
        url = self._build_url(endpoint)
        self._log_request('DELETE', url)
        
        response = self.session.delete(
            url,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )
        
        self._log_response(response)
        return response
    
    def close(self):
        """Close the session - good practice for cleanup # Cierra la sesión - buena práctica para limpieza"""
        self.session.close()
        self.logger.info("Session closed")
    
    def __enter__(self):
        """Context manager support - allows using 'with' statement # Soporte para administrador de contexto - permite usar 'with' statement"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager cleanup # Limpieza del administrador de contexto"""
        self.close()