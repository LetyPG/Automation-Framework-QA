


## Estrategia de Automatización

Este documento explica las decisiones arquitectónicas, patrones de diseño y elecciones estratégicas realizadas en la construcción de este framework de automatización QA.

## Objetivos

- Automatizar flujos críticos de un sitio web de comercio electrónico Magento, validando funcionalidades como login, registro de usuario, búsqueda, carrito de compras y checkout, de manera confiable y reutilizable.
- Crear un Framework de Automatización simple para la UI de un sitio web (Magento) como proyecto educativo.
- Comprender los conceptos básicos de un Framework de Automatización usando Python, Selenium WebDriver, Pytest, Faker, Allure Reports, y no es código listo para producción.


## Resumen de Decisiones Arquitectónicas

| Decisión | Justificación | Beneficio |
|----------|---------------|-----------|
| **Page Object Model** | Separar UI de tests | Mantenibilidad, reutilización |
| **Pytest** | Simple, fixtures poderosos | Tests limpios, ecosistema rico |
| **Fixtures sobre setUp** | Inyección de dependencias | Flexibilidad, composición |
| **Composición (BaseActions)** | Bajo acoplamiento | Testabilidad, flexibilidad |
| **Herencia superficial** | Simplicidad | Fácil de entender |
| **Directorio `pages/` separado** | Organización | Escalabilidad |
| **Directorio `tests/` separado** | Organización por estrategias de prueba | Escalabilidad |
| **`tools/` separado para unit tests** | Retroalimentación rápida | Validación rápida |
| **`.env` + `config.py`** | Gestión de configuración | Flexibilidad de entornos |
| **Faker para datos de prueba** | Datos dinámicos | Datos realistas, únicos |

---

## Principios de Diseño Aplicados

1. **DRY (Don't Repeat Yourself)** - `BaseActions` para operaciones reutilizables
2. **SOLID** - Ver [coding_repository_standards.md](coding_repository_standards.md)
3. **Separación de Responsabilidades** - Pages, tests, utils separados
4. **Responsabilidad Única** - Cada clase tiene un trabajo
5. **Inyección de Dependencias** - Fixtures inyectan dependencias
6. **Configuración sobre Código** - `.env` para configuraciones


---

## Estrategia Central: Page Object Model (POM)

### ¿Qué es el Page Object Model?

**Page Object Model (POM)** es un patrón de diseño que crea un repositorio de objetos para elementos de UI web. Cada página web se representa como una clase, y los elementos web se definen como variables dentro de esa clase.

### ¿Por qué POM?

#### 1. **Separación de Responsabilidades**
{{ ... }}

**Beneficios**:
- Los tests se enfocan en **qué** probar, no en **cómo** interactuar con la UI
- Lógica de negocio separada de la implementación técnica
- Los tests se leen como historias de usuario

#### 2. **Mantenibilidad**

Cuando la UI cambia, solo actualizas el objeto de página:


```python
# If login button locator changes from ID to CSS
# Update ONLY in LoginPage class:
class LoginPage:
    # Before: LOGIN_BUTTON = (By.ID, "submit")
    # After:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-btn")
    
# All tests using LoginPage automatically work!
```

**Beneficios**:
- Punto único de cambio
- Reduce el esfuerzo de mantenimiento
- Previene fragilidad en los tests

#### 3. **Reutilización**

Los métodos de página pueden reutilizarse en múltiples tests:

```python
# Multiples test usan el mismo metodo de login
def test_view_account(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Reused
    # Test account page

def test_view_orders(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Reused
    # Test orders page
```

#### 4. **Legibilidad**

Los tests se vuelven auto-explicativos:

```python
def test_user_can_search_products(browser):
    # Arrange
    search_page = SearchProductPage(browser)
    search_page.open(Configuration.SEARCH_URL)
    
    # Act
    search_page.search("jacket")
    
    # Assert
    results = search_page.get_results()
    assert len(results) > 0
    assert any("jacket" in r.lower() for r in results)
```

---

## ¿Por qué Pytest?

### 1. **Simple y Pythonic**

```python
# Pytest - simple y legible
def test_addition():
    assert 2 + 2 == 4

# unittest - mas "boilerplate", que significa código de apoyo
import unittest
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
```

### 2. **Potentes Fixtures**

Fixtures proporcionan un `setup/teardown` limpio:

```python
@pytest.fixture
def browser():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

def test_login(browser):  # Fixture injected automatically
    # Test uses browser without manual setup
    pass
```



## Estrategia de Automatización

Este documento explica las decisiones arquitectónicas, patrones de diseño y elecciones estratégicas realizadas en la construcción de este framework de automatización QA.

## Objetivos

- Automatizar flujos críticos de un sitio web de comercio electrónico Magento, validando funcionalidades como login, registro de usuario, búsqueda, carrito de compras y checkout, de manera confiable y reutilizable.
- Crear un Framework de Automatización simple para la UI de un sitio web (Magento) como proyecto educativo.
- Comprender los conceptos básicos de un Framework de Automatización usando Python, Selenium WebDriver, Pytest, Faker, Allure Reports, y no es código listo para producción.


## Resumen de Decisiones Arquitectónicas

| Decisión | Justificación | Beneficio |
|----------|---------------|-----------|
| **Page Object Model** | Separar UI de tests | Mantenibilidad, reutilización |
| **Pytest** | Simple, fixtures poderosos | Tests limpios, ecosistema rico |
| **Fixtures sobre setUp** | Inyección de dependencias | Flexibilidad, composición |
| **Composición (BaseActions)** | Bajo acoplamiento | Testabilidad, flexibilidad |
| **Herencia superficial** | Simplicidad | Fácil de entender |
| **Directorio `pages/` separado** | Organización | Escalabilidad |
| **Directorio `tests/` separado** | Organización por estrategias de prueba | Escalabilidad |
| **`tools/` separado para unit tests** | Retroalimentación rápida | Validación rápida |
| **`.env` + `config.py`** | Gestión de configuración | Flexibilidad de entornos |
| **Faker para datos de prueba** | Datos dinámicos | Datos realistas, únicos |

---

## Principios de Diseño Aplicados

1. **DRY (Don't Repeat Yourself)** - `BaseActions` para operaciones reutilizables
2. **SOLID** - Ver [coding_repository_standards.md](coding_repository_standards.md)
3. **Separación de Responsabilidades** - Pages, tests, utils separados
4. **Responsabilidad Única** - Cada clase tiene un trabajo
5. **Inyección de Dependencias** - Fixtures inyectan dependencias
6. **Configuración sobre Código** - `.env` para configuraciones


---

## Estrategia Central: Page Object Model (POM)

### ¿Qué es el Page Object Model?

**Page Object Model (POM)** es un patrón de diseño que crea un repositorio de objetos para elementos de UI web. Cada página web se representa como una clase, y los elementos web se definen como variables dentro de esa clase.

### ¿Por qué POM?

#### 1. **Separación de Responsabilidades**
{{ ... }}

**Beneficios**:
- Los tests se enfocan en **qué** probar, no en **cómo** interactuar con la UI
- Lógica de negocio separada de la implementación técnica
- Los tests se leen como historias de usuario

#### 2. **Mantenibilidad**

Cuando la UI cambia, solo actualizas el objeto de página:

{{ ... }}

**Beneficios**:
- Punto único de cambio
- Reduce el esfuerzo de mantenimiento
- Previene fragilidad en los tests

#### 3. **Reutilización**

Los métodos de página pueden reutilizarse en múltiples tests:

{{ ... }}

#### 4. **Legibilidad**

Los tests se vuelven auto-documentados:

{{ ... }}

---

## ¿Por qué Pytest?

### 1. **Simple y Pythónico**

{{ ... }}

### 2. **Fixtures Poderosos**

Los fixtures proporcionan configuración/limpieza limpia:

{{ ... }}

**Beneficios**:
- Sin código de configuración repetitivo
- Limpieza automática
- Inyección de dependencias
- Control de alcance (function, class, module, session)

### 3. **Ecosistema Enriquecido**

- `pytest-html` - Reportes HTML
- `pytest-xdist` - Ejecución Paralela
- `allure-pytest` - Informes Avanzados
- `pytest-bdd` - Soporte BDD

### 4. **Reportes Detallados**

Pytest proporciona mensajes de afirmación introspectivos:

```python
def test_example():
    expected = "Hello World"
    actual = "Hello Python"
    assert expected == actual

# Output:
# AssertionError: assert 'Hello World' == 'Hello Python'
#   - Hello Python
#   + Hello World
```

---

## ¿Por qué Fixtures sobre Setup/Teardown?

### Enfoque Tradicional (unittest)

```python
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_login(self):
        # Test code
        pass
```

**Problemas**:
- Atado a la estructura de clase
- Difícil de compartir entre archivos de test
- Sin inyección de dependencias
- Control de alcance limitado

### Enfoque de Fixture (Pytest)

```python
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):  # Clean, injected
    # Test code
    pass
```

**Ventajas**:
- Compartido entre archivos (via `conftest.py`)
- Inyección de dependencias
- Alcance flexible
- Composable (fixtures pueden usar otras fixtures)
- Dependencias explícitas

### Composición de `Fixtures`

```python
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(browser):  # Utiliza la fixture del navegador
    page = LoginPage(browser)
    page.login(username, password)
    return page

def test_account_page(logged_in_user):  # Utiliza la fixture compuesta
    # Los tests comienzan con el usuario ya logueado
    pass
```

---

## Composición sobre Herencia

### ¿Por qué Composición?

**Herencia** crea acoplamiento fuerte:

```python
# Herencia - Acoplamiento fuerte
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        # Implementation
        pass

class LoginPage(BasePage):
    # Hereda todo de BasePage
    pass
```

**Problemas**:
- Cambios en `BasePage` afectan a todas las clases hijas
- Difícil de probar en aislamiento
- Problema de clase base frágil

**Composición** proporciona flexibilidad:

```python
# Composition - Flexible
class BaseActions:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        # Implementation
        pass

class LoginPage:
    def __init__(self, driver):
        self.actions = BaseActions(driver)  # Composition
    
    def login(self, username, password):
        self.actions.click(locator)  # Use composed object
```

**Ventajas**:
- Desacoplamiento
- Fácil de probar (puede mockear `BaseActions`)
- Flexible (puede intercambiar implementaciones)

### Enfoque de este Framework

Usamos **herencia para conveniencia**, pero se mantiene la herencia `shallow`:

```python
class BaseActions:
    """Reusable Selenium operations."""
    def click(self, locator): pass
    def send_keys(self, locator, text): pass

class LoginPage(BaseActions):
    """Inherits BaseActions for convenience."""
    def login(self, username, password):
        self.send_keys(USER_INPUT, username)
        self.send_keys(PASS_INPUT, password)
        self.click(LOGIN_BUTTON)
```

**¿Por qué funciona esto?**:
-  Un solo nivel de herencia (shallow)
- `BaseActions` es estable (casi no cambia)
- Page objects focus on page-specific logic
- Fácil de entender y mantener

---

## Estructura de carpetas explicada

```
Automation-Framework-QA/
├── docs/                    # Documentación
├── driver/                  # Drivers de navegador opcionales
├── src/                     # Código fuente del proyecto
│   ├── pages/               # Clases de Page Object
│   │   ├── base_actions.py  # Operaciones Selenium reutilizables
│   │   ├── login.py         # LoginPage
│   │   └── page_account_user.py # AccountUserPage
│   ├── api/                 # Módulo de API Client
│   │   ├── __init__.py      # Exporta el módulo
│   │   ├── base_api_client.py   # Base HTTP client (reusable)
│   │   ├── user_service_api.py  # Implementación del User service
│   │   ├── product_service_api.py  # Implementación del Product service
│   │   └── README.md            # Este archivo explica el módulo api y su uso
├── ci_cd/                   # Módulo de CI/CD
|     ├── README.md          # Este archivo explica el módulo ci_cd, la logica de la pipeline y su uso
|     ├── jenkins_api/
|     |     ├── jenkinsfile
|     |     └── 
|     └── jenkins_staging/
|     |     |     ├── jenkinsfile
|     |     |     └── 
|     |     └── jenkins_smoke/
|     |     |     ├── jenkinsfile
|     |     |     └── 
|     |     └── jenkins_ui/
|     |           ├── jenkinsfile
|     |           └── 
── features/
|           ├── README.md
|           ├── api/
|           |     ├── user_service.feature
|           |     └── product_service.feature
|           |     └── order_payment_service.feature
|           └── ui/
|             ├── login.feature
|             └── account_user.feature
|             └── search_product_page.feature
|
├── tests/                # Módulo de Tests (test suites, agrupados por estrategias de test)
|     |___ bdd_steps_definition/ # Módulo de BDD Steps Definition
|     |     |__ conftest.py
|     |     ├── test_api_user_steps_definition.py
|     |     └── test_ui_login_steps_definition.py
|     ├── smoke_test/
|     |     ├── test_login.py
|     |     └── test_account_user.py
|     |     ├── test_form_submission.py
|     |     └── test_search_product_page.py
|     ├── sanity_test/
|     |     ├── 
|     |     └── 
|     ├── regression_test/
|     |     ├── 
|     |     └── 
|     ├── e2e_test/
|     |     ├── 
|     |     └── 
|     ├── performance_test/
|     |     ├── 
|     |     └── 
|     |___ db_test/
|     |     ├── 
|     |     └── 
|     ├── api_test/
|     |     ├── test_user/
|     |     |     ├── conftest.py
|     |     |     ├── test_user_service.py
|     |     |     └── test_user_search.py
|     |     |     └── test_user_data_validation.py
|     |     |     └── test_user_service_integration.py
|     |     └── test_product/
|     |     |     ├── 
|     |     |     └── 
|     |     └── test_order/
|     |     |     ├── 
|     |     |     └── 
|     |     └── 
|     ├── security_test/
|     |     ├── 
|     |     └── 
|     ├── load_test/
|     |     ├── 
|     |     └── 
|     ├── install_test/
|     |     ├── 
|     |     └── 
|
├── tools/                   # Pruebas unitarias de Page Objects
│   ├── conftest.py          # Fixtures de pruebas unitarias
│   └── test_login_unit.py
├── utils/                   # Utilities
│   ├── browser_manager.py   # Setup del navegador
│   ├── config.py            # Configuración
│   ├── data_generator.py    # Generador de datos de prueba con Faker
│   └── assertions.py        # Aserciones personalizadas
│   ├── logger.py            # Logger

├── .env                     # Variables de entorno
├── conftest.py              # Fixtures globales
├── pytest.ini               # Configuración de Pytest
└── requiriments.txt         # Dependencias
```

### ¿Por qué esta estructura?

#### 1. **`pages/` - Page Objects**

**Propósito**: Una clase por página, encapsulando las interacciones de la página.

**¿Por qué una carpeta separada?**
- Organización clara
- Fácil de encontrar objetos de página
- Escala con el crecimiento de las páginas

**Example**:
```python
# pages/login.py
class LoginPage(BaseActions):
    def login(self, username, password):
        # Page-specific logic
        pass
```


## Distribución Recomendada de Pruebas

Para un framework QA equilibrado:

| Tipo de Prueba | % de Pruebas | Propósito |
|-----------|-----------|---------|
| **BDD (Acceptance)** | 15-20% | Flujos críticos de usuario, criterios de aceptación |
| **Integration/Functional** | 60-70% | Pruebas detalladas de API/UI, casos de borde |
| **Unit Tests** | 10-15% | Test framework components (POMs, utils) |
| **E2E** | 5-10% | Full system integration |

**Áreas de enfoque BDD:**
- Caminos felices críticos
- Escenarios negativos clave
- Flujos de negocio críticos
- Validación de criterios de aceptación

**Áreas de enfoque estándar de Pytest:**
- Casos de borde
- Pruebas de límites
- Pruebas de rendimiento
- Pruebas de seguridad
- Validación de datos
- Escenarios técnicos


#### 2. **`tests/` -  Tests Suites**

**Propósito**: 
- Tests que usan un navegador real.
- Donde se crearon las suites de pruebas agrupadas por estrategia de pruebas.
- Algunos subdirectorios importantes dentro de `tests/` están planificados para ser desarrollados en el futuro, por eso puedes verificar su existencia incluso si están vacíos, solo `smoke_test/` y el `api_test/` están desarrollados en la versión actual de este framework.

- En este ámbito se creó un directorio único para cada estrategia de pruebas, en la versión actual del framework solo se desarrolló `smoke test` como una guía de estrategia de pruebas, pero en el futuro agregaré más estrategias de pruebas, por lo que por ahora solo se han creado las suites de pruebas agrupadas por estrategia de pruebas (dentro de cada directorio o para un directorio más grande, como `smoke_test/`).
But therefore it was not already develope the rest of test strategies  you could be able to find inside of each test strategy directory an explanatory doc, to undertsand how to use the test strategy and the logical proposal for the architecture of this framework.
- En el alcance de este proyecto se desarrollaron los test modules agrupados por estrategia de pruebas (como se mencionó antes),para desarrollar cada estrategia de pruebas debes crear un test module, pero dependiendo de tus necesidades recomiendo esta dos prácticas:

**1. Organice los test_strategy como se mencionó antes, pero dentro de cada test_strategy directorio, cree subdirectorios atendiendo a las funcionalidades específicas:**


```
      test/
      |__smoke_test/
      |          |__test_login/
      |          |    |__test_login_success.py
      |          |    |__test_login_negative.py
      |          |    |__test_login_desviation.py
      |          |    |__test_login_multiples_inputs_combinations.py
      |          |    |__test_login_multiples_users.py
      |          |___test_account_user/
      |          |    |__test_account_user_success.py
      |          |    |__test_account_user_negative.py
      |          |    |__test_account_user_desviation.py
      |          |    |__test_account_user_multiples_inputs_combinations.py
      |          |    |__test_account_user_multiples_users.py
      

```

**2. Organice los test en subdirectorios atendiendo a las funcionalidades específicas:** 

```
      test/
      |__test_login/
      |    |__test_login.py
      |    |__test_login_negative.py
      |    |__test_login_api.py
      |    |__test_login_security.py
      |    |__test_login_load.py
      |    |__test_login_performance.py
      |    |__test_login_regressio
      |__test_search/
      |    |__test_search.py
      |    |__test_search_negative.py
      |    |__test_search_api.py
      |    |__test_search_security.py
      |    |__test_search_load.py
      |    |__test_search_performance.py
      |    |__test_search_regression.py

```
 

### Sobre Pruebas API

Este **API module** proporciona un marco robusto y escalable para la prueba de API REST utilizando **Programación Orientada a Objetos (OOP)** y **principios SOLID**. Demuestra patrones de automatización de pruebas de grado profesional adecuados para propósitos educativos y proyectos del mundo real.

- **Arquitectura en capas**
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

>En la version actual del framework se desarrollo la api base class y una instancia de ella (user_api), por la misma razón se desarrollo un subdirectorio de test para la instancia user_api para validar la api a través de las funcionalidades del usuario, pero otros subdirectorios importantes están planificados para ser desarrollados en el futuro, por eso puedes verificar su existencia incluso si están vacíos.



### Sobre Pruebas Unitarias
     
**Por qué separar las pruebas unitarias?**
- Diferentes velocidades de ejecución (lento vs rápido)
- Diferentes dependencias (navegador vs mocks)
- Diferentes estrategias CI/CD

**Ejemplo**:
```python
# tests/test_login.py
def test_login_success(browser):
    page = LoginPage(browser)
    page.login(username, password)
    assert page.is_login_successful()
```

#### 3. **`tools/` - Pruebas Unitarias**

**Propósito**: Pruebas rápidas para objetos de página sin navegador.

**Por qué separar directorio?**
- Bucle de retroalimentación rápido
- Sin sobrecarga del navegador
- Prueba la lógica de la página en isolation

**Ejemplo**:
```python
# tools/test_login_unit.py
def test_login_calls_correct_methods(mock_driver):
    page = LoginPage(mock_driver)
    page.login("user@example.com", "pass123")
    # Verify methods were called
```

#### 4. **`utils/` - Utilities**

**Propósito**: Funciones y clases auxiliares compartidas.

**Por qué separar?**
- Reutilizables en páginas y pruebas
- Responsabilidad única
- Fácil de probar

**Contenido**:
- `browser_manager.py` - Ciclo de vida del navegador
- `config.py` - Gestión de configuración
- `data_generator.py` - Generación de datos de prueba
- `assertions.py` - Aserciones personalizadas

#### 5. **`conftest.py` - Global Fixtures**

**Propósito**: Pytest fixtures shared across all tests.

**Por qué en la raíz?**
- Automaticamente descubiertos por pytest
- Disponibles para todos los archivos de test
- Logica de configuración centralizada

**Ejemplo**:
```python
# conftest.py
@pytest.fixture
def browser():
    manager = BrowserManager()
    driver = manager.driver
    yield driver
    driver.quit()
```

#### 6. **`.env` - Variables de Entorno**

**Propósito**: Almacena configuración y secretos.

**Por qué `.env`?**
- Mantener secretos fuera del código
- Fácil de cambiar por entorno
- No se comitea al control de versiones

**Example**:
```bash
BASE_URL=https://magento.softwaretestingboard.com
USERNAME=user@example.com
PASSWORD=SecurePass123
```

---

## Por qué `BaseActions`

### Problema sin `BaseActions`

```python
# Cada página repite el mismo código
**Ejemplo: Login Page**

```
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
    
    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
```

**Ejemplo: Account Page**

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):  # Duplicated!
        element = self.driver.find_element(*locator)
        element.click()
```

### Solución: `BaseActions`

```python
# pages/base_actions.py
class BaseActions:
    """Reusable Selenium operations."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

# pages/login.py
class LoginPage(BaseActions):
    """Inherits all BaseActions methods."""
    def login(self, username, password):
        self.send_keys(USER_INPUT, username)  # From BaseActions
        self.send_keys(PASS_INPUT, password)  # From BaseActions
        self.click(LOGIN_BUTTON)              # From BaseActions
```

**Beneficios**:
- DRY (Don't Repeat Yourself/ No se repita a si mismo/ no repetir código)
- Consistencia en el comportamiento de las páginas
- Tiempos de espera y manejo de errores incorporados
- Fácil de extender con nuevas operaciones

---

## Configuration Management Strategy

### Why `.env` + `config.py`?

#### Problem: Hardcoded Values

```python
# Bad - Hardcoded
def test_login():
    driver.get("https://magento.softwaretestingboard.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
```

**Problemas**:
- No se puede cambiar la URL sin modificar el código
- Credenciales expuestas en el código
- Diferentes entornos necesitan diferentes valores

#### Solución: Capa de configuración

```bash
# .env
BASE_URL=https://magento.softwaretestingboard.com
LOGIN_URL=https://magento.softwaretestingboard.com/customer/account/login
USERNAME=user@example.com
PASSWORD=SecurePass123
USER_NAME_INPUT=css,#email
```

```python
# utils/config.py
class Configuration:
    BASE_URL = os.getenv('BASE_URL')
    LOGIN_URL = os.getenv('LOGIN_URL')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    USER_NAME_INPUT = parse_locator(os.getenv('USER_NAME_INPUT'))
```

```python
# tests/test_login.py - Clean!
def test_login(browser):
    page = LoginPage(browser)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
```

**Beneficios**:
- No hardcodear valores
- Fácil de cambiar por entorno
- No expuestos secretos en el código
- Un solo fuente de verdad

---

## Estrategia de datos de prueba: `Faker`

### Por qué datos dinámicos?

#### Problema: Datos de prueba hardcodeados

```python
# Bad - Hardcoded data
def test_registration():
    page.register(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"  # Falla si ya existe!
    )
```

**Problemas**:
- Error de datos duplicados
- Escenarios de prueba no realistas
- Cobertura limitada de pruebas

#### Solución: Faker

```python
# Good - Dynamic data with Faker
from utils.data_generator import DataGenerator

def test_registration():
    generator = DataGenerator()
    user = generator.generate_user()
    
    page.register(
        first_name=user["first_name"],   # "Alice" (random)
        last_name=user["last_name"],     # "Johnson" (random)
        email=user["email"]              # "alice.j@example.com" (unique)
    )
```

**Beneficios**:
- Datos únicos cada ejecución
- Escenarios de prueba realistas
- Cobertura mejorada de casos borde
- No contaminación de datos

---
---

## Next Steps

- Review [Page Object Model](programming_standards.md) para ejemplos detallados del POM
- Check [Coding Standards](coding_repository_standards.md) para principios SOLID
- Check [Coding Standards](programm_paradigm.md) para Programación Orientada a Objetos
- Explore [Best Practices](selenium.md) para QA guidelines
- Explore [Best Practices](pytest.md) para QA guidelines
- Read [Getting Started](getting_started.md) para ejecutar el framework

---

**Esta estrategia de automatización garantiza un framework QA mantenible, escalable y profesional.**

----
**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  
