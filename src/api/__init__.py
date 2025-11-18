"""
API Module - Exposes API clients for testing

This module exports all API clients for easy import in tests.
Following Python best practices for package initialization.

Usage:
    from api import BaseAPIClient, UserServiceAPI
    
    # Or import directly
    from api.user_service_api import UserServiceAPI
"""

from api.base_api_client import BaseAPIClient
from api.user_service_api import UserServiceAPI

# Define what gets exported when using "from api import *"
__all__ = [
    'BaseAPIClient',
    'UserServiceAPI'
]

# Version information
__version__ = '0.1.2'
__author__ = 'C-QA Automation Framework'