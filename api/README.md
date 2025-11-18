>English Version: At the Top of this file you are going to see the English version indicated by this sy  mbol 🟦, and below you are going to see the Spanish version indicated by this symbol 🟩, you can choose the one you want to use.

>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.   


# 🟦 API Testing Module - Comprehensive Guide 🟦

## Table of Contents
1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Architecture & Design Patterns](#architecture--design-patterns)
4. [SOLID Principles Applied](#solid-principles-applied)
5. [Module Components](#module-components)
6. [Running Tests](#running-tests)
7. [Examples](#examples)
8. [Best Practices](#best-practices)

---

## Overview

This API module provides a robust, scalable framework for REST API testing using **Object-Oriented Programming (OOP)** and **SOLID principles**. It demonstrates professional-grade test automation patterns suitable for educational purposes and real-world projects.

### Key Features:
- Reusable HTTP client with session management
- Service-specific API clients (User, Product, Order)
- Comprehensive test suites with pytest
- Allure integration for beautiful reports
- Schema validation for API contracts
- Fixture-based test organization
- Parametrized and data-driven tests

---

## Directory Structure

```
C-QA-Automation-Framework/
│
├── api/                                    # API Client Module
│   ├── __init__.py                        # Module exports
│   ├── base_api_client.py                 # Base HTTP client (reusable)
│   ├── user_service_api.py                # User service implementation
│   ├── product_service_api.py             # Product service (future)
│   └── README.md                          # This file
│
├── tests/
│   ├── api_test/                          # API Tests Directory
│   │   ├── conftest.py                    # Shared fixtures & configuration
│   │   │
│   │   ├── test_user/                     # User API tests (organized by feature)
│   │   │   ├── __init__.py
│   │   │   ├── test_user_service.py       # CRUD operations tests (Create, Read, Update, Delete)
│   │   │   ├── test_user_search.py        # Search/filter tests
│   │   │   ├── test_user_data_validation.py  # Parametrized validation tests
│   │   │   └── test_user_service_integration.py  # Integration/lifecycle tests
│   │   │
│   │   ├── test_product/                  # Product API tests (future)
│   │   │   └── __init__.py
│   │   │
│   │   └── test_order_payment/            # Order/Payment API tests (future)
│   │       └── __init__.py
```

## Best Practices

### **1. Test Organization**
**DO:**
- Organize tests by feature/service in separate directories
- Use `conftest.py` for shared fixtures
- Keep test files focused on specific functionality
- Use descriptive test method names

 **DO NOT:**
- Mix different service tests in one file
- Define fixtures in test files
- Create overly complex test scenarios

### **2. Fixture Usage**
**DO:**
- Use `scope="module"` for expensive fixtures (API clients)
- Use `scope="function"` for test data that should be fresh
- Place fixtures in `conftest.py` for reusability

**DO NOT:**
- Import pytest just to use fixtures (they're auto-discovered)
- Create fixtures that depend on test execution order

### **3. Assertions**
**DO:**
- Use descriptive assertion messages
- Validate multiple aspects (status code, data structure, values)
- Use JSON schema validation for contract testing

**DO NOT:**
- Only check status code (validate response data too)
- Use generic assertion messages

### **4. Test Data**
**DO:**
- Use Faker for realistic test data
- Create fixtures for reusable data structures
- Use parametrized tests for multiple scenarios

**DO NOT:**
- Hardcode test data in test methods
- Reuse same data across tests (unless intentional)


---

## 🏗️ Architecture & Design Patterns

### 1. **Layered Architecture**

```
┌─────────────────────────────────────┐
│        Test Layer                   │  ← Test files with assertions
│  (test_user_service.py, etc.)       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Service Layer                   │  ← Business logic for each API
│  (UserServiceAPI, ProductAPI, etc.) │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Base Client Layer               │  ← HTTP communication (reusable)
│     (BaseAPIClient)                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     External API                    │  ← Actual REST API endpoints
└─────────────────────────────────────┘
```

### 2. **Design Patterns Used**
- **Template Method Pattern**: BaseAPIClient defines HTTP methods structure
- **Factory Pattern**: Fixtures create test data and API instances
- **Page Object Model (POM) Equivalent**: Service APIs encapsulate endpoints
- **AAA Pattern**: Arrange-Act-Assert in all tests

---

## SOLID Principles Applied

### **S - Single Responsibility Principle (SRP)**
**Each class has ONE responsibility:**
- `BaseAPIClient`: Only handles HTTP communication
- `UserServiceAPI`: Only handles user-related operations
- Test classes: Only test specific features (CRUD, Search, Integration)
- `conftest.py`: Only provides fixtures and configuration

**Example:**
```python
class BaseAPIClient:
    """Responsible ONLY for HTTP operations"""
    def get(self, endpoint): ...
    def post(self, endpoint, data): ...

class UserServiceAPI(BaseAPIClient):
    """Responsible ONLY for user business logic"""
    def get_all_users(self): ...
    def create_user(self, data): ...
```

### **O - Open/Closed Principle (OCP)**
✅ **Open for extension, closed for modification:**
- `BaseAPIClient` can be extended without changing its code
- New service APIs inherit from base without modifying it

**Example:**
```python
# Adding new API service WITHOUT modifying BaseAPIClient
class ProductServiceAPI(BaseAPIClient):  # Extends, not modifies
    def get_all_products(self):
        return self.get('/products')  # Uses inherited method
```

### **L - Liskov Substitution Principle (LSP)**
✅ **Subclasses can replace parent class:**
- Any `UserServiceAPI` instance can be used where `BaseAPIClient` is expected
- All service APIs maintain the same HTTP method contracts

**Example:**
```python
def make_request(api_client: BaseAPIClient):
    return api_client.get('/endpoint')

# Both work without breaking
make_request(BaseAPIClient('https://api.example.com'))
make_request(UserServiceAPI())  # Substitutes parent seamlessly
```

### **I - Interface Segregation Principle (ISP)**
✅ **Clients not forced to depend on unused methods:**
- Each service API exposes only relevant methods
- Tests only depend on fixtures they actually use

**Example:**
```python
# UserServiceAPI doesn't force product-related methods
class UserServiceAPI:
    def get_users(self): ...     # User-specific
    def create_user(self): ...   # User-specific
    # NO product methods here!

# Separate interface for products
class ProductServiceAPI:
    def get_products(self): ...  # Product-specific
```

### **D - Dependency Inversion Principle (DIP)**
✅ **Depend on abstractions, not concretions:**
- High-level modules depend on `requests` library interface (abstraction)
- Easy to swap HTTP library if needed
- Tests depend on fixture interfaces, not implementations

**Example:**
```python
class BaseAPIClient:
    def __init__(self, base_url: str):
        self.session = requests.Session()  # Depends on interface
        # Could easily swap to httpx, aiohttp, etc.
```

---

## Module Components

### **1. base_api_client.py**
**Purpose**: Provides reusable HTTP methods for all API clients

**Key Features:**
- Session management for connection pooling
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Centralized logging and error handling
- Authentication token support
- Custom headers configuration
- Context manager support (`with` statement)

**Usage:**
```python
from api import BaseAPIClient

client = BaseAPIClient('https://api.example.com')
response = client.get('/users')
print(response.status_code)
```

### **2. user_service_api.py**
**Purpose**: User-specific API operations extending BaseAPIClient

**Key Features:**
- CRUD operations (Create, Read, Update, Delete)
- Search and filter functionality
- Related resources (posts, albums, todos)
- Returns structured response dictionaries

**Usage:**
```python
from api import UserServiceAPI

user_api = UserServiceAPI()
result = user_api.get_all_users()
print(result['status_code'])  # 200
print(result['data'])         # List of users
```

### **3. tests/api_test/conftest.py**
**Purpose**: Shared pytest fixtures and configuration

**Fixtures Provided:**
- `user_api`: API client instance (module scope)
- `sample_user_data`: Random test data using Faker
- `user_schema`: JSON schema for validation

**Custom Markers:**
- `@pytest.mark.api`: Mark as API test
- `@pytest.mark.crud`: Mark as CRUD operation test
- `@pytest.mark.integration`: Mark as integration test

---

##  Running Tests

### **Install Dependencies**
```bash
pip install -r requiriments.txt
```

### **Configure Environment**
Create a `.env` file in the project root:
```env
API_BASE_URL=https://jsonplaceholder.typicode.com
```

### **Run All API Tests**
```bash
# Run all tests in api_test directory
pytest tests/api_test/ -v

# With detailed output
pytest tests/api_test/ -v -s
```

### **Run Specific Test Suites**
```bash
# Run only user service tests
pytest tests/api_test/test_user/ -v

# Run specific test file
pytest tests/api_test/test_user/test_user_service.py -v

# Run specific test class
pytest tests/api_test/test_user/test_user_service.py::TestUserCRUD -v

# Run specific test method
pytest tests/api_test/test_user/test_user_service.py::TestUserCRUD::test_get_all_users_success -v
```

### **Run Tests by Markers**
```bash
# Run only API tests
pytest -m api -v

# Run only CRUD tests
pytest -m crud -v

# Run integration tests
pytest -m integration -v
```

### **Generate Allure Reports**
```bash
# Run tests and generate Allure results
pytest tests/api_test/ --alluredir=reports/allure-results

# Serve Allure report in browser
allure serve reports/allure-results

# Generate HTML report
allure generate reports/allure-results -o reports/allure-report --clean
```

### **Run Tests with Coverage**
```bash
# Install coverage
pip install pytest-cov

# Run with coverage report
pytest tests/api_test/ --cov=api --cov-report=html
```

### **Parallel Execution**
```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel (4 workers)
pytest tests/api_test/ -n 4
```

---

## Examples

### **Example 1: Create a New Service API**
```python
# api/product_service_api.py
from api.base_api_client import BaseAPIClient
from typing import Dict, Optional
import os

class ProductServiceAPI(BaseAPIClient):
    def __init__(self, base_url: Optional[str] = None):
        if base_url is None:
            base_url = os.getenv('API_BASE_URL', 'https://api.example.com')
        super().__init__(base_url)
    
    def get_all_products(self, params: Optional[Dict] = None) -> Dict:
        response = self.get('/products', params=params)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def get_product_by_id(self, product_id: int) -> Dict:
        response = self.get(f'/products/{product_id}')
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
```

### **Example 2: Write a Simple Test**
```python
# tests/api_test/test_product/test_product_service.py
import allure
from api.product_service_api import ProductServiceAPI

class TestProductCRUD:
    @allure.title("Test GET all products")
    def test_get_all_products(self):
        product_api = ProductServiceAPI()
        result = product_api.get_all_products()
        
        assert result['status_code'] == 200
        assert result['data'] is not None
        assert isinstance(result['data'], list)
```

### **Example 3: Add Custom Fixture**
```python
# tests/api_test/conftest.py
@pytest.fixture(scope="module")
def product_api():
    """Fixture for Product API client"""
    api = ProductServiceAPI()
    yield api
    api.close()
```

---


### **5. Imports**
 **DO:**
```python
import allure                    # Used for decorators
from faker import Faker          # Used for test data
import pytest                    # Only if using @pytest.mark.parametrize
```

**DON'T:**
```python
import pytest  # If you only use fixtures (not needed!)
```

---

## Key Takeaways

1. **Separation of Concerns**: Base client → Service API → Tests
2. **SOLID Principles**: Applied throughout the architecture
3. **Reusability**: Fixtures and base classes prevent code duplication
4. **Scalability**: Easy to add new services and tests
5. **Maintainability**: Clear structure and documentation
6. **Professional Grade**: Follows industry best practices

---

## 📚 Additional Resources

- **pytest Documentation**: https://docs.pytest.org/
- **Allure Framework**: https://docs.qameta.io/allure/
- **Requests Library**: https://requests.readthedocs.io/
- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID

---

## 📧 Contributing

This is an educational framework. Suggestions for improvements:
- Add more service APIs (Product, Order, Payment)
- Implement authentication strategies (OAuth2, JWT)
- Add response caching mechanisms
- Include retry logic for flaky tests
- Add mock API server for offline testing

---
---

# 🟩 Modulo de API Testing- Guia 🟩 

## Tabala 
1. [Introducción](#introducción)
2. [Estructura del directorio](#estructura-del-directorio)
3. [Arquitectura & Patrones de diseño](#arquitectura--patrones-de-diseño)
4. [Principios SOLID Aplicados](#principios-solid-aplicados)
5. [Componentes del módulo](#componentes-del-módulo)
6. [Ejecución de pruebas](#ejecución-de-pruebas)
7. [Ejemplos](#ejemplos)
8. [Prácticas recomendadas](#prácticas-recomendadas)

---

## Introducción

Este modulo proporciona un framework robusto y escalable para la pruebas de APIs REST utilizando **Programación Orientada a Objetos (OOP)** y **Principios SOLID**. Demuestra patrones de automatización de pruebas de grado profesional apropiados para proyectos educativos y de mundo real.

### Características clave:
- Cliente HTTP reutilizable con gestión de sesión
- Clientes API específicos para servicios (User, Product, Order)
- Comprehensive test suites with pytest
- Allure integration for beautiful reports
- Schema validation for API contracts
- Fixture-based test organization
- Parametrized and data-driven tests

---

## Directory Structure

```
C-QA-Automation-Framework/
│
├── api/                                    # Modulo de API Client
│   ├── __init__.py                        # Exporta modulos
│   ├── base_api_client.py                 # Clase que implementa un Cliente HTTP base (reutilizable- Programación Orientada a Objetos)
│   ├── user_service_api.py                # Implementación del servicio de usuario
│   ├── product_service_api.py             # Implementación del servicio de producto (futuro)
│   └── README.md                          # Este archivo
│
├── tests/
│   ├── api_test/                          # Directorio de pruebas de API
│   │   ├── conftest.py                    # Fixtures y configuración compartida
│   │   │
│   │   ├── test_user/                     # Directorio de pruebas de usuario
│   │   │   ├── __init__.py
│   │   │   ├── test_user_service.py       # Test para validar operaciones CRUD (crear, leer, actualizar, borrar)
│   │   │   ├── test_user_search.py        # Test para validar operaciones de búsqueda y filtrado
│   │   │   ├── test_user_data_validation.py  # Test para validar operaciones de validación de datos
│   │   │   └── test_user_service_integration.py  # Test para validar operaciones de integración y ciclo de vida
│   │   │
│   │   ├── test_product/                  # Directorio de pruebas de producto
│   │   │   └── __init__.py
│   │   │
│   │   └── test_order_payment/            # Directorio de pruebas de orden y pago (futuro)
│   │       └── __init__.py
```

## Buenas Prácticas

### **1. Organización de Pruebas**
**Hacer:**
- Organizar pruebas por funcionalidad/servicio en directorios separados
- Usar `conftest.py` para fixtures compartidos
- Mantener archivos de pruebas enfocados en funcionalidad específica
- Usar nombres descriptivos para los métodos de prueba

 **No hacer:**
- No mezclar pruebas de diferentes servicios en un solo archivo
- No definir fixtures en archivos de pruebas
- No crear escenarios de pruebas demasiado complejos

### **2. Uso de Fixtures**
**Hacer:**
- Usar `scope="module"` para fixtures caros (clientes API)
- Usar `scope="function"` para datos de prueba que deben ser frescos
- Colocar fixtures en `conftest.py` para reutilización

**No hacer:**
- Importar pytest solo para usar fixtures (son descubiertos automáticamente)
- No crear fixtures que dependan del orden de ejecución de las pruebas

### **3. Assertions**
**Hacer:**
- Use descriptive assertion messages
- Validate multiple aspects (status code, data structure, values)
- Use JSON schema validation for contract testing

**No hacer:**
- Solo verificar el código de estado (validar datos de respuesta también)
- Usar mensajes de afirmación genéricos

### **4. Test Data**
**Hacer:**
- Usar `Faker` para datos de prueba realistas
- Crear fixtures para estructuras de datos reutilizables
- Usar parametrized tests para múltiples escenarios

**No hacer:**
- Hardcode test data in test methods
- Reuse same data across tests (unless intentional)


---

## Arquitectura & Patrones de Diseño

### 1. **Arquitectura en Capas**

` **Arquitectura en capas**
```
┌─────────────────────────────────────┐
│        Capa de test                   │  ← Archivos de test y las aserciones
│  (test_user_service.py, etc.)       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Capa de servicio                   │  ← Logica de negocio para cada servicio de API
│  (UserServiceAPI, ProductAPI, etc.) │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     Capa de cliente base               │  ← Comunicación HTTP (reusable)
│     (BaseAPIClient)                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     API externa                    │  ← Endpoints de la API REST
└─────────────────────────────────────┘
```

**Patrones de diseño utilizados**
- **Patrón de plantilla para métodos HTTP**:  `BaseAPIClient` define la estructura de los metodos HTTP
- **Patrón Factory**: Fixtures crean datos de prueba y instancias de API
- **Patrón Equivalente al Page Object Model (POM)**: Service APIs encapsulan endpoints
- **Patrón AAA**: Arrange-Act-Assert en todos los tests

**Principios SOLID explicados con ejemplos reales de tu framework**

- Single Responsibility Principle: BaseAPIClient maneja HTTP, UserServiceAPI maneja la lógica de negocio
- Open/Closed Principle: Extendido BaseAPIClient sin modificarlo
- Liskov Substitution Principle: Service APIs puede sustituir la base de la clase
- Interface Segregation Principle: Cada API expone solo los métodos relevantes
- Dependency Inversion Principle: Depende de abstracciones (interfaz de requests)


#### API Tests Directory Structure

```
├── tests/
│   ├── api_test/                          # Directorio de pruebas API 
│   │   ├── conftest.py                    # Fixtures & configuración
│   │   │
│   │   ├── test_user/                     # User API tests (organizados por funcionalidad)
│   │   │   ├── __init__.py
│   │   │   ├── test_user_service.py       # Test de operaciones CRUD (crear, leer, actualizar, borrar)
│   │   │   ├── test_user_search.py        # Test de búsqueda
│   │   │   ├── test_user_data_validation.py  # Test de validación de datos por parámetros (user_id)
│   │   │   └── test_user_service_integration.py  # Test de integración
│   │   │
│   │   ├── test_product/                  # Product API tests (future)
│   │   │   └── __init__.py
│   │   │
│   │   └── test_order_payment/            # Order/Payment API tests (future)
│   │       └── __init__.py

```
### **1. Organización de los tests**
- Organiza los tests por funcionalidad/servicio en directorios separados
- Usa  `conftest.py` para fixtures compartidos
- Mantiene los archivos de test enfocados en funcionalidad específica
- Usa nombres descriptivos para los métodos de test


### **2. Uso de Fixtures**
- Usa `scope="module"` para fixtures costosos (clientes API)
- Usa `scope="function"` para datos de prueba que deben ser frescos
- Coloca los fixtures en `conftest.py` para reutilización



### **3. Assertivas**
- Usa mensajes descriptivos para las assertivas
- Valida múltiples aspectos (código de estado, estructura de datos, valores)
- Usa validación de esquema JSON para pruebas de contrato
- Solo verifica código de estado (valida datos de respuesta también)
- Usa assertivas generales

### **4. Datos de Prueba**
- Usa Faker para datos de prueba realistas
- Crea fixtures para estructuras de datos reutilizables
- Usa pruebas parametrizadas para múltiples escenarios
- Codifica datos de prueba en métodos de test (evita `hardcode`)
- Reutiliza datos en múltiples tests (a menos que sea intencional)

### 2. **Design Patterns Used**
- **Template Method Pattern**: BaseAPIClient defines HTTP methods structure
- **Factory Pattern**: Fixtures create test data and API instances
- **Page Object Model (POM) Equivalent**: Service APIs encapsulate endpoints
- **AAA Pattern**: Arrange-Act-Assert in all tests

---

## SOLID Principles Applied

### **S - Responsabilidad Unica (SRP)**
**Cada clase tiene UNA responsabilidad:**
- `BaseAPIClient`: Solo maneja la comunicación HTTP
- `UserServiceAPI`: Solo maneja operaciones relacionadas con el usuario
- Clases de prueba: Solo prueban características específicas (CRUD, Búsqueda, Integración)
- `conftest.py`: Solo proporciona fixtures y configuración

**Example:**
```python
class BaseAPIClient:
    """Responsable solo de la comunicación HTTP"""
    def get(self, endpoint): ...
    def post(self, endpoint, data): ...

class UserServiceAPI(BaseAPIClient):
    """Responsable solo de la lógica de negocio del usuario"""
    def get_all_users(self): ...
    def create_user(self, data): ...
```

### **O - Principio Abierto/Cerrado (OCP)**
 **Abierto para extensión, cerrado para modificación:**
- `BaseAPIClient` puede ser extendido sin modificar su código
- Nuevos servicios de API heredan de la base sin modificarla

**Example:**
```python
# Agregando nuevo servicio de API sin modificar BaseAPIClient
class ProductServiceAPI(BaseAPIClient):  # Extends, not modifies
    def get_all_products(self):
        return self.get('/products')  # Uses inherited method
```

### **L - Principio de Sustitución de Liskov (LSP)**
 **Subclasses can replace parent class:**
- Any `UserServiceAPI` instance can be used where `BaseAPIClient` is expected
- All service APIs maintain the same HTTP method contracts

**Example:**
```python
def make_request(api_client: BaseAPIClient):
    return api_client.get('/endpoint')

# Both work without breaking
make_request(BaseAPIClient('https://api.example.com'))
make_request(UserServiceAPI())  # Substitutes parent seamlessly
```

### **I - Principio de segregación de interfaces (ISP)**
 **los clientes no están forzados a depender de métodos no utilizados:**
- Cada servicio API expone solo métodos relevantes
- Los tests solo dependen de fixtures que realmente usan

**Example:**
```python
# UserServiceAPI no fuerza métodos relacionados con productos
class UserServiceAPI:
    def get_users(self): ...     # User-specific
    def create_user(self): ...   # User-specific
    # NO product methods here!

# Interface para productos
class ProductServiceAPI:
    def get_products(self): ...  # Product-specific
```

### **D - Principio de inversión de dependencias (DIP)**
 **Dependencia sobre abstracciones, no sobre concretas:**
- Modulos de alto nivel dependen de la interfaz de la libreria `requests` (abstracción)
- Fácil de cambiar la libreria HTTP si es necesario
- Los tests dependen de interfaces de fixture, no implementaciones

**Example:**
```python
class BaseAPIClient:
    def __init__(self, base_url: str):
        self.session = requests.Session()  # Depends on interface
        # Could easily swap to httpx, aiohttp, etc.
```

---

## Componentes del módulo

### **1. base_api_client.py**
**Propósito**: Proporciona métodos HTTP reutilizables para todos los clientes de API

**Características clave:**
- Gestión de sesiones para agrupación de conexiones
- Métodos HTTP: GET, POST, PUT, PATCH, DELETE
- Registro centralizado y manejo de errores
- Soporte de tokens de autenticación
- Configuración de encabezados personalizados
- Soporte de gestor de contexto (`with` statement)

**Uso:**
```python
from api import BaseAPIClient

client = BaseAPIClient('https://api.example.com')
response = client.get('/users')
print(response.status_code)
```

### **2. user_service_api.py**
**Propósito**: Operaciones API específicas de usuario extendiendo BaseAPIClient

**Características clave:**
- Operaciones CRUD (Crear, Leer, Actualizar, Borrar)
- Funcionalidad de búsqueda y filtrado
- Recursos relacionados (posts, albums, todos)
- Devuelve diccionarios de respuesta estructurados

**Usage:**
```python
from api import UserServiceAPI

user_api = UserServiceAPI()
result = user_api.get_all_users()
print(result['status_code'])  # 200
print(result['data'])         # List of users
```

### **3. tests/api_test/conftest.py**
**Propósito**: Fixtures y configuración compartida para pytest

**Fixtures proporcionadas:**
- `user_api`: Instancia del cliente API (alcance de módulo)
- `sample_user_data`: Datos de prueba aleatorios usando Faker
- `user_schema`: Esquema JSON para validación

**Marcadores personalizados:**
- `@pytest.mark.api`: Marca como prueba API
- `@pytest.mark.crud`: Marca como operación CRUD
- `@pytest.mark.integration`: Marca como prueba de integración

---

##  Ejecución de pruebas

### **Instalación de dependencias**
```bash
pip install -r requiriments.txt
```

### **Configuración del entorno**
Create a `.env` file in the project root:
```env
API_BASE_URL=https://jsonplaceholder.typicode.com
```

### **Ejecución de todas las pruebas API**
```bash
# Run all tests in api_test directory
pytest tests/api_test/ -v

# With detailed output
pytest tests/api_test/ -v -s
```

### **Ejecución de pruebas específicas**

- Ejecutar solo pruebas de un directorio específico
```
pytest tests/api_test/test_user/ -v
```

- Ejecutar solo uno de los archivos de pruebas de un directorio específico
```
pytest tests/api_test/test_user/test_user_service.py -v
```

- Ejecutar solo una de las pruebas de un archivo de pruebas de un directorio específico
```
pytest tests/api_test/test_user/test_user_service.py::TestUserCRUD -v
```

- Ejecutar solo una de las pruebas de un archivo de pruebas de un directorio específico
```
pytest tests/api_test/test_user/test_user_service.py::TestUserCRUD::test_get_all_users_success -v
```

### **Ejecución de pruebas por marcadores**
```bash
# Ejecutar solo pruebas API
pytest -m api -v

# Ejecutar solo pruebas CRUD
pytest -m crud -v

# Ejecutar solo pruebas de integración
pytest -m integration -v
```

### **Generación de reportes Allure**
```bash
# Ejecutar pruebas y generar resultados Allure
pytest tests/api_test/ --alluredir=reports/allure-results

# Ver reporte Allure en navegador
allure serve reports/allure-results

# Generar reporte HTML
allure generate reports/allure-results -o reports/allure-report --clean
```

### **Ejecución de pruebas con cobertura**
```bash
# Instalar pytest-cov
pip install pytest-cov

# Ejecutar pruebas con reporte de cobertura
pytest tests/api_test/ --cov=api --cov-report=html
```

### **Ejecución paralela de pruebas**
```bash
# Instalar pytest-xdist
pip install pytest-xdist

# Ejecutar pruebas en paralelo (4 workers)
pytest tests/api_test/ -n 4
```

---

## Ejemplos

### **Ejemplo 1: Crear un nuevo servicio API**
```python
# api/product_service_api.py
from api.base_api_client import BaseAPIClient
from typing import Dict, Optional
import os

class ProductServiceAPI(BaseAPIClient):
    def __init__(self, base_url: Optional[str] = None):
        if base_url is None:
            base_url = os.getenv('API_BASE_URL', 'https://api.example.com')
        super().__init__(base_url)
    
    def get_all_products(self, params: Optional[Dict] = None) -> Dict:
        response = self.get('/products', params=params)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
    
    def get_product_by_id(self, product_id: int) -> Dict:
        response = self.get(f'/products/{product_id}')
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'response': response
        }
```

### **Ejemplo 2: Escribir una Prueba Simple**
```python
# tests/api_test/test_product/test_product_service.py
import allure
from api.product_service_api import ProductServiceAPI

class TestProductCRUD:
    @allure.title("Test GET all products")
    def test_get_all_products(self):
        product_api = ProductServiceAPI()
        result = product_api.get_all_products()
        
        assert result['status_code'] == 200
        assert result['data'] is not None
        assert isinstance(result['data'], list)
```

### **Ejemplo 3: Agregar un Fixture Personalizado**
```python
# tests/api_test/conftest.py
@pytest.fixture(scope="module")
def product_api():
    """Fixture for Product API client"""
    api = ProductServiceAPI()
    yield api
    api.close()
```

---


### **5. Imports**
Para importar librerías en Python, se debe seguir ciertas convenciones. Aquí se presentan las mejores prácticas, en caso de los nuevos servicios API y los arcghivso de test que vaya a crear:
 **DO:**
```python
import allure                    # Se utiliza para decoradores
from faker import Faker          # Se utiliza para datos de prueba
import pytest                    # Se utiliza para marcar parámetros
```

**DON'T:**
```python
import pytest  # Si solo se usan fixtures (no es necesario!)
```

---

## Key Takeaways

1. **Separación de preocupaciones**: Base client → Service API → Tests
2. **Principios SOLID**: Aplicados a lo largo de la arquitectura
3. **Reutilización**: Fixtures y clases base previenen la duplicación de código
4. **Escalabilidad**: Fácil de agregar nuevos servicios y pruebas
5. **Mantenibilidad**: Estructura clara y documentación
6. **Calidad profesional**: Seguir las mejores prácticas del sector

---

## 📚 Recursos adicionales

- **pytest Documentation**: https://docs.pytest.org/
- **Allure Framework**: https://docs.qameta.io/allure/
- **Requests Library**: https://requests.readthedocs.io/
- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID

---

## Contribución

Este es un marco educativo. Sugerencias para mejoras:
- Agregar más APIs de servicios (Producto, Pedido, Pago)
- Implementar estrategias de autenticación (OAuth2, JWT)
- Agregar mecanismos de caché de respuestas
- Incluir lógica de reintentos para pruebas fallibles
- Agregar un servidor de API simulada para pruebas offline

---

**Version**: 0.1.2  
**Author**: C-QA Automation Framework Team