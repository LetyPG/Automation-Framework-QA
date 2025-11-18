>English Version: At the Top of this file you are going to see the English version indicated by this symbol 🟦, and below you are going to see the Spanish version indicated by this symbol 🟩, you can choose the one you want to use.

>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.  

# 🟦 API Helpers Module

This module provides utility classes and helpers for API testing in the C-QA Automation Framework.

## 📚 Contents

### SchemaValidator

JSON Schema validation utility for API response validation in BDD and traditional test scenarios.

**Location**: `utils/api_helpers/schema_validator.py`

**Purpose**: 
- Validate API responses against predefined JSON schemas
- Ensure API contract compliance
- Support BDD test scenarios
- Provide detailed validation error reporting

## Usage

### Basic Schema Validation

```python
from utils.api_helpers.schema_validator import SchemaValidator

# Initialize validator with schema file
validator = SchemaValidator(schema_name='user_schema.json')

# Validate API response
response = api_client.get_user(2)
is_valid = validator.validate(response.json())

assert is_valid, "API response schema validation failed"
```

### In BDD Step Definitions

```python
from pytest_bdd import scenario, given, when, then
from utils.api_helpers.schema_validator import SchemaValidator

@then('the response schema should be valid')
def validate_schema():
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(scenario_context['response'].json())
    assert is_valid, "API response schema is invalid"
```

### Detailed Validation

```python
validator = SchemaValidator('user_schema.json')
result = validator.validate_with_details(response.json())

if not result['is_valid']:
    for error in result['errors']:
        print(f"Error: {error['message']}")
        print(f"Path: {error['path']}")
```

### Inline Schema Validation

```python
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "email"]
}

is_valid = SchemaValidator.validate_against_schema_string(data, schema)
```

## Directory Structure

```
|__utils
|    |__api_helpers/
|    |    |____init__.py              # Module initialization
|    |    |__schema_validator.py      # SchemaValidator class
|    |    |__schemas/                 # JSON schema files
|    |    |   |__user_schema.json     # User API response schema
|    |    |   |__product_schema.json  # Product API response schema (future)
|    |    |   |__order_schema.json    # Order API response schema (future)
|    |    └── README.md                # This file
```

## Available Schemas

### user_schema.json

Validates user API responses with the following structure:

```json
{
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://..."
  },
  "support": {
    "url": "https://...",
    "text": "..."
  }
}
```

**Fields:**
- `id`: integer (required)
- `email`: string with email format (required)
- `first_name`: string (required)
- `last_name`: string (required)
- `avatar`: string with URI format (required)

## Creating New Schemas

1. Create a new JSON file in `utils/api_helpers/schemas/`
2. Define the JSON Schema following JSON Schema Draft 7 specification
3. Use the schema in your tests:

```python
validator = SchemaValidator('your_new_schema.json')
```

### Example Schema Template

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Your Schema Title",
  "description": "Schema description",
  "type": "object",
  "properties": {
    "field_name": {
      "type": "string",
      "description": "Field description"
    }
  },
  "required": ["field_name"],
  "additionalProperties": false
}
```

##  SchemaValidator Methods

### `__init__(schema_name, schemas_dir=None)`
Initialize validator with schema file.

**Parameters:**
- `schema_name` (str): Name of schema file (e.g., 'user_schema.json')
- `schemas_dir` (Path, optional): Custom schemas directory

### `validate(data, raise_error=False)`
Validate JSON data against schema.

**Parameters:**
- `data` (dict): JSON data to validate
- `raise_error` (bool): If True, raises ValidationError on failure

**Returns:** bool - True if valid, False otherwise

### `validate_with_details(data)`
Validate and return detailed results.

**Returns:** dict with validation results and error details

### `get_schema()`
Get the loaded schema dictionary.

### `validate_against_schema_string(data, schema)` (class method)
Validate data against inline schema dictionary.

##  Integration with Framework

### With conftest.py Fixtures

```python
# conftest.py
import pytest
from api.user_service_api import UserServiceAPI

@pytest.fixture(scope='module')
def user_api_client():
    return UserServiceAPI(base_url='https://reqres.in/api')
```

### With BDD Step Definitions

```python
# tests/steps_definitions/test_api_user_steps_definition.py
from pytest_bdd import scenario, given, when, then, parsers
from api.user_service_api import UserServiceAPI
from utils.api_helpers.schema_validator import SchemaValidator

scenario_context = {}

@when(parsers.parse('I request the user with ID "{user_id}"'))
def request_user(user_api_client: UserServiceAPI, user_id):
    response = user_api_client.get_user(user_id)
    scenario_context['response'] = response

@then('the response schema should be valid')
def validate_schema():
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(scenario_context['response'].json())
    assert is_valid, "API response schema is invalid"
```

## Dependencies

- `jsonschema` - JSON Schema validation library
- `utils.logger` - Framework logging utility

## Related Documentation

- [API Module README](../../api/README.md)
- [JSON Schema Specification](https://json-schema.org/)
- [jsonschema Python Library](https://python-jsonschema.readthedocs.io/)

## 🎓 Best Practices

1. **Create specific schemas** for each API endpoint
2. **Use descriptive schema names** (e.g., `user_detail_schema.json`, `user_list_schema.json`)
3. **Include descriptions** in schema properties for documentation
4. **Version schemas** if API changes (e.g., `user_schema_v1.json`, `user_schema_v2.json`)
5. **Validate early** in test execution for faster feedback
6. **Log validation errors** for debugging

## Troubleshooting

### FileNotFoundError: Schema file not found

**Issue:** Schema file doesn't exist in the schemas directory.

**Solution:** 
```python
# Check available schemas
validator = SchemaValidator('user_schema.json')
print(validator._list_available_schemas())
```

### ValidationError: Schema validation failed

**Issue:** API response doesn't match schema.

**Solution:**
```python
# Get detailed validation results
result = validator.validate_with_details(response.json())
print(result['errors'])
```

---

**Version**: 0.1.2  
**Author**: C-QA Automation Framework Team


>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.  

# 🟩 Módulo API Helpers

Este módulo proporciona clases de utilidad y helpers para pruebas API en el C-QA Automation Framework.

## 📚 Contenidos

### SchemaValidator

Utilidad de validación de Esquema JSON para validación de respuestas API en escenarios de prueba BDD y tradicionales.

**Ubicación**: `utils/api_helpers/schema_validator.py`

**Propósito**: 
- Validar respuestas API contra esquemas JSON predefinidos
- Asegurar cumplimiento de contrato API
- Soportar escenarios de prueba BDD
- Proporcionar reporte detallado de errores de validación

## Uso

### Validación Básica de Esquema

```python
from utils.api_helpers.schema_validator import SchemaValidator

# Inicializar validador con archivo de esquema
validator = SchemaValidator(schema_name='user_schema.json')

# Validar respuesta API
response = api_client.get_user(2)
is_valid = validator.validate(response.json())

assert is_valid, "API response schema validation failed"
```

### En Definiciones de Pasos BDD

```python
from pytest_bdd import scenario, given, when, then
from utils.api_helpers.schema_validator import SchemaValidator

@then('the response schema should be valid')
def validate_schema():
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(scenario_context['response'].json())
    assert is_valid, "API response schema is invalid"
```

### Validación Detallada

```python
validator = SchemaValidator('user_schema.json')
result = validator.validate_with_details(response.json())

if not result['is_valid']:
    for error in result['errors']:
        print(f"Error: {error['message']}")
        print(f"Path: {error['path']}")
```

### Validación de Esquema en Línea

```python
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "email"]
}

is_valid = SchemaValidator.validate_against_schema_string(data, schema)
```

## Estructura del Directorio

```
|__utils
|    |__api_helpers/
|    |    |____init__.py              # Inicialización del módulo
|    |    |__schema_validator.py      # Clase SchemaValidator
|    |    |__schemas/                 # Archivos de esquema JSON
|    |    |   |__user_schema.json     # Esquema de respuesta API de usuario
|    |    |   |__product_schema.json  # Esquema de respuesta API de producto (futuro)
|    |    |   |__order_schema.json    # Esquema de respuesta API de orden (futuro)
|    |    └── README.md                # Este archivo
```

## Esquemas Disponibles

### user_schema.json

Valida respuestas API de usuario con la siguiente estructura:

```json
{
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://..."
  },
  "support": {
    "url": "https://...",
    "text": "..."
  }
}
```

**Campos:**
- `id`: entero (requerido)
- `email`: cadena con formato email (requerido)
- `first_name`: cadena (requerido)
- `last_name`: cadena (requerido)
- `avatar`: cadena con formato URI (requerido)

## Crear Nuevos Esquemas

1. Crear un nuevo archivo JSON en `utils/api_helpers/schemas/`
2. Definir el Esquema JSON siguiendo la especificación JSON Schema Draft 7
3. Usar el esquema en tus pruebas:

```python
validator = SchemaValidator('your_new_schema.json')
```

### Plantilla de Ejemplo de Esquema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Your Schema Title",
  "description": "Schema description",
  "type": "object",
  "properties": {
    "field_name": {
      "type": "string",
      "description": "Field description"
    }
  },
  "required": ["field_name"],
  "additionalProperties": false
}
```

##  Métodos de SchemaValidator

### `__init__(schema_name, schemas_dir=None)`
Inicializar validador con archivo de esquema.

**Parámetros:**
- `schema_name` (str): Nombre del archivo de esquema (ej., 'user_schema.json')
- `schemas_dir` (Path, opcional): Directorio de esquemas personalizado

### `validate(data, raise_error=False)`
Validar datos JSON contra esquema.

**Parámetros:**
- `data` (dict): Datos JSON a validar
- `raise_error` (bool): Si es True, lanza ValidationError en caso de falla

**Retorna:** bool - True si es válido, False en caso contrario

### `validate_with_details(data)`
Validar y retornar resultados detallados.

**Retorna:** dict con resultados de validación y detalles de errores

### `get_schema()`
Obtener el diccionario de esquema cargado.

### `validate_against_schema_string(data, schema)` (método de clase)
Validar datos contra diccionario de esquema en línea.

##  Integración con el Framework

### Con Fixtures de conftest.py

```python
# conftest.py
import pytest
from api.user_service_api import UserServiceAPI

@pytest.fixture(scope='module')
def user_api_client():
    return UserServiceAPI(base_url='https://reqres.in/api')
```

### Con Definiciones de Pasos BDD

```python
# tests/steps_definitions/test_api_user_steps_definition.py
from pytest_bdd import scenario, given, when, then, parsers
from api.user_service_api import UserServiceAPI
from utils.api_helpers.schema_validator import SchemaValidator

scenario_context = {}

@when(parsers.parse('I request the user with ID "{user_id}"'))
def request_user(user_api_client: UserServiceAPI, user_id):
    response = user_api_client.get_user(user_id)
    scenario_context['response'] = response

@then('the response schema should be valid')
def validate_schema():
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(scenario_context['response'].json())
    assert is_valid, "API response schema is invalid"
```

## Dependencias

- `jsonschema` - Librería de validación de Esquema JSON
- `utils.logger` - Utilidad de logging del framework

## Documentación Relacionada

- [API Module README](../../api/README.md)
- [JSON Schema Specification](https://json-schema.org/)
- [jsonschema Python Library](https://python-jsonschema.readthedocs.io/)

## 🎓 Mejores Prácticas

1. **Crear esquemas específicos** para cada endpoint de API
2. **Usar nombres de esquema descriptivos** (ej., `user_detail_schema.json`, `user_list_schema.json`)
3. **Incluir descripciones** en propiedades de esquema para documentación
4. **Versionar esquemas** si la API cambia (ej., `user_schema_v1.json`, `user_schema_v2.json`)
5. **Validar temprano** en la ejecución de pruebas para retroalimentación más rápida
6. **Registrar errores de validación** para depuración

## Solución de Problemas

### FileNotFoundError: Archivo de esquema no encontrado

**Problema:** El archivo de esquema no existe en el directorio de esquemas.

**Solución:** 
```python
# Verificar esquemas disponibles
validator = SchemaValidator('user_schema.json')
print(validator._list_available_schemas())
```

### ValidationError: Falló la validación de esquema

**Problema:** La respuesta API no coincide con el esquema.

**Solución:**
```python
# Obtener resultados de validación detallados
result = validator.validate_with_details(response.json())
print(result['errors'])
```

---

**Version**: 0.1.2  
**Author**: C-QA Automation Framework Team
