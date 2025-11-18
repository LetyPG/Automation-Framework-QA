"""
Schema Validator - JSON Schema validation utility for API testing

This module provides JSON schema validation capabilities for API responses.
It supports BDD testing scenarios and follows the framework's architecture patterns.

Educational Notes:
- Uses jsonschema library for validation
- Supports external schema files (JSON format)
- Provides detailed error reporting
- Integrates with the framework's logger

Usage:
    from utils.api_helpers.schema_validator import SchemaValidator
    
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(response_data)
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from jsonschema import validate, ValidationError, Draft7Validator
from utils.logger import logger


class SchemaValidator:
    """
    JSON Schema Validator for API Response Validation
    
    This class validates JSON data against predefined schemas stored in JSON files.
    It's designed to work seamlessly with BDD step definitions and API tests.
    
    Attributes:
        schema_name (str): Name of the schema file
        schema_path (Path): Full path to the schema file
        schema (dict): Loaded JSON schema
    
    Example:
        # In BDD step definition
        validator = SchemaValidator(schema_name='user_schema.json')
        is_valid = validator.validate(api_response.json())
        assert is_valid, "API response schema validation failed"
    """
    
    # Default schemas directory relative to this file
    SCHEMAS_DIR = Path(__file__).parent / 'schemas'
    
    def __init__(self, schema_name: str, schemas_dir: Optional[Path] = None):
        """
        Initialize the Schema Validator
        
        Args:
            schema_name (str): Name of the schema file (e.g., 'user_schema.json')
            schemas_dir (Path, optional): Custom directory for schemas. 
                                         Defaults to utils/api_helpers/schemas/
        
        Raises:
            FileNotFoundError: If schema file doesn't exist
            json.JSONDecodeError: If schema file is not valid JSON
        """
        self.schema_name = schema_name
        
        # Use custom directory or default
        self.schemas_directory = schemas_dir if schemas_dir else self.SCHEMAS_DIR
        
        # Ensure schemas directory exists
        self.schemas_directory.mkdir(parents=True, exist_ok=True)
        
        # Build full path to schema file
        self.schema_path = self.schemas_directory / schema_name
        
        # Load the schema
        self.schema = self._load_schema()
        
        logger.info(f"SchemaValidator initialized with schema: {schema_name}")
    
    def _load_schema(self) -> Dict[str, Any]:
        """
        Load JSON schema from file
        
        Returns:
            dict: Parsed JSON schema
            
        Raises:
            FileNotFoundError: If schema file doesn't exist
            json.JSONDecodeError: If schema file is invalid JSON
        """
        if not self.schema_path.exists():
            error_msg = (
                f"Schema file not found: {self.schema_path}\n"
                f"Available schemas: {self._list_available_schemas()}"
            )
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)
        
        try:
            with open(self.schema_path, 'r', encoding='utf-8') as schema_file:
                schema = json.load(schema_file)
                logger.debug(f"Successfully loaded schema from: {self.schema_path}")
                return schema
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON in schema file {self.schema_path}: {str(e)}"
            logger.error(error_msg)
            raise json.JSONDecodeError(error_msg, e.doc, e.pos)
    
    def _list_available_schemas(self) -> List[str]:
        """
        List all available schema files in the schemas directory
        
        Returns:
            list: List of available schema file names
        """
        if not self.schemas_directory.exists():
            return []
        
        return [f.name for f in self.schemas_directory.glob('*.json')]
    
    def validate(self, data: Dict[str, Any], raise_error: bool = False) -> bool:
        """
        Validate JSON data against the loaded schema
        
        Args:
            data (dict): JSON data to validate (typically API response)
            raise_error (bool): If True, raises ValidationError on failure.
                               If False, returns False and logs error.
        
        Returns:
            bool: True if validation passes, False otherwise
            
        Raises:
            ValidationError: If validation fails and raise_error=True
        
        Example:
            validator = SchemaValidator('user_schema.json')
            response_data = api_client.get_user(1).json()
            
            # Option 1: Return boolean
            if validator.validate(response_data):
                print("Valid!")
            
            # Option 2: Raise exception on failure
            validator.validate(response_data, raise_error=True)
        """
        try:
            # Validate using jsonschema
            validate(instance=data, schema=self.schema)
            logger.info(f"Schema validation PASSED for: {self.schema_name}")
            return True
            
        except ValidationError as e:
            error_msg = (
                f"Schema validation FAILED for: {self.schema_name}\n"
                f"Validation Error: {e.message}\n"
                f"Failed at path: {' -> '.join(str(p) for p in e.path)}\n"
                f"Schema path: {' -> '.join(str(p) for p in e.schema_path)}"
            )
            logger.error(error_msg)
            
            if raise_error:
                raise ValidationError(error_msg)
            
            return False
    
    def validate_with_details(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and return detailed validation results
        
        Args:
            data (dict): JSON data to validate
            
        Returns:
            dict: Validation results with details
                {
                    'is_valid': bool,
                    'errors': list of error messages (if any),
                    'schema_name': str
                }
        
        Example:
            validator = SchemaValidator('user_schema.json')
            result = validator.validate_with_details(response_data)
            
            if not result['is_valid']:
                print(f"Errors: {result['errors']}")
        """
        validator_obj = Draft7Validator(self.schema)
        errors = list(validator_obj.iter_errors(data))
        
        result = {
            'is_valid': len(errors) == 0,
            'schema_name': self.schema_name,
            'errors': []
        }
        
        if errors:
            for error in errors:
                result['errors'].append({
                    'message': error.message,
                    'path': ' -> '.join(str(p) for p in error.path),
                    'schema_path': ' -> '.join(str(p) for p in error.schema_path),
                    'validator': error.validator
                })
            
            logger.warning(f"Schema validation found {len(errors)} error(s)")
        else:
            logger.info(f"Schema validation passed with no errors")
        
        return result
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get the loaded schema
        
        Returns:
            dict: The JSON schema
        """
        return self.schema
    
    @classmethod
    def validate_against_schema_string(cls, data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        """
        Validate data against a schema provided as a dictionary (not from file)
        
        Args:
            data (dict): JSON data to validate
            schema (dict): JSON schema as dictionary
            
        Returns:
            bool: True if validation passes, False otherwise
            
        Example:
            schema = {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "number"}
                },
                "required": ["name"]
            }
            
            is_valid = SchemaValidator.validate_against_schema_string(
                {"name": "John", "age": 30},
                schema
            )
        """
        try:
            validate(instance=data, schema=schema)
            logger.info("Schema validation PASSED (inline schema)")
            return True
        except ValidationError as e:
            logger.error(f"Schema validation FAILED: {e.message}")
            return False
    
    def __repr__(self) -> str:
        """String representation of the validator"""
        return f"SchemaValidator(schema_name='{self.schema_name}', schema_path='{self.schema_path}')"
    
    def __str__(self) -> str:
        """User-friendly string representation"""
        return f"Schema Validator for '{self.schema_name}'"
