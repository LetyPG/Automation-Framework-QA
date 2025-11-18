# Pytest - Framework de Pruebas de Python

## ¿Qué es Pytest?

**Pytest** es un framework de pruebas maduro y rico en características para Python. Facilita escribir pruebas pequeñas y legibles, y escala para soportar pruebas funcionales complejas.

**Documentación Oficial**: [https://docs.pytest.org/](https://docs.pytest.org/)

---

## ¿Por qué Pytest para Automatización de Pruebas?

### Ventajas

1. **Sintaxis Simple**
   - Escribir pruebas como funciones simples
   - No requiere código repetitivo
   - Aserciones legibles con `assert`

2. **Fixtures Poderosos**
   - Lógica de configuración/limpieza reutilizable
   - Inyección de dependencias
   - Control de alcance (function, class, module, session)

3. **Ecosistema Rico de Plugins**
   - Reportes HTML, ejecución paralela, cobertura
   - Integración con Allure, soporte BDD
   - Arquitectura extensible

4. **Reportes Detallados de Fallos**
   - Introspección clara de aserciones
   - Mensajes de error útiles
   - Trazas de pila con contexto

5. **Descubrimiento Flexible de Pruebas**
   - Descubrimiento automático de pruebas
   - Selección basada en patrones
   - Markers para organización de pruebas

---

## Pytest vs Otros Frameworks

| Framework | Pros | Contras |
|-----------|------|---------|
| **Pytest** | Simple, fixtures poderosos, plugins, BDD | Curva de aprendizaje para fixtures |
| **unittest** | Incorporado, familiar para devs Java | Más código repetitivo, menos flexible |
| **nose2** | Similar a pytest | Menos desarrollo activo |
| **Robot Framework** | Basado en palabras clave, no programadores | Verboso, menos flexible |

**Este framework usa Pytest** por su simplicidad, poder y ecosistema.


## Conceptos Fundamentales

### Funciones de Prueba

Funciones simples que comienzan con `test_`:

```python
def test_addition():
    result = 2 + 2
    assert result == 4
```

### Aserciones

Usa la declaración `assert` incorporada de Python:

```python
def test_string():
    name = "Python"
    assert name == "Python"
    assert len(name) == 6
    assert name.startswith("Py")
```

**Pytest proporciona mensajes detallados de fallo**:
```
AssertionError: assert 'Python' == 'python'
  - python
  + Python
```

### Fixtures

Lógica de configuración/limpieza reutilizable:

```python
import pytest

@pytest.fixture
def sample_data():
    # Configuración
    data = {"name": "Test", "value": 42}
    yield data
    # Limpieza (opcional)
    print("Cleanup")

def test_with_fixture(sample_data):
    assert sample_data["name"] == "Test"
```

---

## Cómo Este Framework Usa Pytest

### 1. Estructura de Pruebas

Las pruebas están organizadas en el directorio `tests/`:

```
tests/
├── __init__.py
├── test_login.py
├── test_account_user.py
├── test_form_submission.py
└── test_search_product.py
```

**Ejemplo de Prueba**:
```python
# tests/test_login.py
def test_login_success_if_credentials_present(browser):
    page = LoginPage(browser)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
    assert page.is_redirected_to_account()
```

### 2. Fixtures (`conftest.py`)

Fixtures globales definidos en `conftest.py`:

```python
# conftest.py
import pytest
from utils.browser_manager import BrowserManager

@pytest.fixture(scope="function")
def browser(request):
    """Proporciona una instancia de WebDriver para cada prueba."""
    browser_name = request.config.getoption("--browser", default="chrome")
    manager = BrowserManager(browser=browser_name)
    driver = manager.driver
    
    yield driver  # La prueba se ejecuta aquí
    
    driver.quit()  # Limpieza después de la prueba
```

**Beneficios**:
- Configuración/limpieza automática del navegador
- Sin código repetitivo en las pruebas
- Compartido entre todos los archivos de prueba

### 3. Configuración (`pytest.ini`)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    smoke: Pruebas smoke rápidas
    regression: Suite de regresión completa
    integration: Pruebas de integración
```

### 4. Markers

Organizar y filtrar pruebas:

```python
import pytest

@pytest.mark.smoke
def test_critical_feature(browser):
    # Prueba crítica
    pass

@pytest.mark.regression
def test_detailed_scenario(browser):
    # Prueba detallada
    pass
```

**Ejecutar markers específicos**:
```bash
pytest -m smoke        # Ejecutar solo pruebas smoke
pytest -m regression   # Ejecutar solo pruebas de regresión
```

---

## Características de Pytest Usadas en el Framework

### Opciones de Línea de Comandos

```bash
# Ejecutar todas las pruebas
pytest

# Salida detallada
pytest -v

# Mostrar declaraciones print
pytest -s

# Ejecutar archivo específico
pytest tests/test_login.py

# Ejecutar prueba específica
pytest tests/test_login.py::test_login_success

# Ejecutar por patrón
pytest -k login

# Ejecutar por marker
pytest -m smoke

# Detener en primer fallo
pytest -x

# Ejecutar últimas pruebas fallidas
pytest --lf

# Generar reporte HTML
pytest --html=report.html --self-contained-html
```

### Opciones Personalizadas de Línea de Comandos

Este framework agrega la opción `--browser`:

```python
# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador para ejecutar pruebas: chrome o firefox"
    )
```

**Uso**:
```bash
pytest --browser=chrome
pytest --browser=firefox
```

### Parametrización

Ejecutar la misma prueba con diferentes datos:

```python
import pytest

@pytest.mark.parametrize("username,password", [
    ("user1@example.com", "pass1"),
    ("user2@example.com", "pass2"),
    ("user3@example.com", "pass3"),
])
def test_login_multiple_users(browser, username, password):
    page = LoginPage(browser)
    page.login(username, password)
    assert page.is_redirected_to_account()
```

### Alcances de Fixtures

Controlar el ciclo de vida del fixture:

```python
@pytest.fixture(scope="function")  # Por defecto: nueva instancia por prueba
def browser_function():
    pass

@pytest.fixture(scope="class")  # Compartido entre clase de prueba
def browser_class():
    pass

@pytest.fixture(scope="module")  # Compartido entre archivo de prueba
def browser_module():
    pass

@pytest.fixture(scope="session")  # Compartido entre toda la sesión de prueba
def browser_session():
    pass
```

**Este framework usa `scope="function"`** para aislamiento de pruebas.

---

## Plugins de Pytest Usados

### pytest-html

Generar reportes HTML de pruebas:

```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

### allure-pytest

Reportes avanzados con Allure:

```bash
pip install allure-pytest
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### pytest-xdist (Opcional)

Ejecución paralela de pruebas:

```bash
pip install pytest-xdist
pytest -n 4  # Ejecutar con 4 workers
```

---

## Mejores Prácticas en Este Framework

### 1. Nomenclatura de Pruebas

```python
# Bueno - Nombres descriptivos
def test_login_success_with_valid_credentials(browser):
    pass

def test_login_fails_with_invalid_password(browser):
    pass

# Evitar - Nombres vagos
def test1(browser):
    pass

def test_login(browser):
    pass
```

### 2. Independencia de Pruebas

```python
# Bueno - Cada prueba es independiente
def test_create_account(browser):
    # Crea cuenta
    pass

def test_login(browser):
    # Inicia sesión (no depende de test_create_account)
    pass

# Evitar - Las pruebas dependen entre sí
def test_step1(browser):
    global user_id
    user_id = create_user()

def test_step2(browser):
    login(user_id)  # Depende de test_step1
```

### 3. Patrón AAA (Arrange-Act-Assert)

```python
def test_search_product(browser):
    # Arrange - Preparar
    page = SearchProductPage(browser)
    page.open(Configuration.SEARCH_URL)
    
    # Act - Actuar
    page.search("jacket")
    
    # Assert - Verificar
    results = page.get_results()
    assert len(results) > 0
    assert any("jacket" in r.lower() for r in results)
```

### 4. Usar Fixtures para Configuración

```python
# Bueno - Fixture maneja la configuración
@pytest.fixture
def logged_in_user(browser):
    page = LoginPage(browser)
    page.login(username, password)
    return page

def test_account_page(logged_in_user):
    # La prueba comienza con usuario ya logueado
    pass

# Evitar - Configuración en cada prueba
def test_account_page(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Configuración repetida
    # Lógica de prueba
```

---

---

## Características Avanzadas

### Fixtures con Parámetros

```python
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    manager = BrowserManager(browser=request.param)
    driver = manager.driver
    yield driver
    driver.quit()

# La prueba se ejecuta dos veces: una con Chrome, otra con Firefox
def test_cross_browser(browser):
    pass
```

## Otro Uso de pytest es la  `capability` de BDD (Behavior-Driven Development)

Para este framework se implemento una capa extra de validacion de QA usando BDD (Behavior-Driven Development), esta es una forma de validar la experiencia real del usuario y el recorrido real del usuario.
No es necesario instalar extra, porque usando `pytest-bdd` (incluido en el requirements.txt) es suficiente, este es un plugin increible que extiende las capacidades de pytest y proporciona una forma de escribir pruebas en un lenguaje mas natural.

## ¿Qué es BDD (Behavior-Driven Development)?

**Behavior-Driven Development (BDD)** es una enfoque de desarrollo de software que extiende Test-Driven Development (TDD) escribiendo casos de pruebas en un lenguaje natural que los no programadores pueden leer. BDD se centra en el **comportamiento** de la aplicacion desde la perspectiva del usuario.

### Componentes Clave:

1. **Gherkin Language**: Humano legible sintaxis usando Given-When-Then
2. **Feature Files**: `.feature` archivos que contienen escenarios en ingles plano
3. **Step Definitions**: Python code que implementa cada paso Gherkin
4. **Living Documentation**: Tests que sirven como documentacion actualizada
5. **Extra QA Best Practices**: Usando BDD es otra capa de garantia de calidad, ayuda a cerrar el agujero entre QA y Desarrollo, y tambien mantiene el negocio cerca de los escenarios y flujos reales del usuario, de esta manera puede validar la experiencia real del usuario y el recorrido real del usuario.


**El Concepto Central:**
En BDD con pytest-bdd, los archivos 
.feature
 son los TESTS, no los archivos de definicion de pasos.

 ```
features/user_service.feature  ← This is the TEST (executable scenarios)
         │
         │ calls
         ▼
tests/bdd_steps_definitions/   ← This is the IMPLEMENTATION (glue code)

```
**Como pytest-bdd descubre los tests:**
Feature files define test cases: Each Scenario in a 
.feature
 file becomes a pytest test
Step definitions provide implementation: The Python code in tests/bdd_steps_definitions/ is glue code that gets called

**Flujo de Ejecucion:**
Cuando ejecutas pytest features/user_service.feature:

```
1. pytest-bdd lee el archivo .feature
   └─> Encuentra: Scenario: Retrieve a specific user

2. Para cada paso Gherkin, busca las definiciones de pasos:
   └─> "Given the user service is available"
       → Busca el decorador @given con este texto
       → Finds it in tests/bdd_steps_definitions/test_api_user_steps_definition.py
       → Executes the Python function
```

3. Reporta `pass/fail` basado en todos los pasos en el escenario


---


### Fixtures de Uso Automático

Ejecutar automáticamente sin solicitud explícita:

```python
@pytest.fixture(autouse=True)
def log_test_name(request):
    print(f"\nEjecutando: {request.node.name}")
```

### Factories de Fixtures

Crear múltiples instancias:

```python
@pytest.fixture
def make_user():
    def _make_user(name, email):
        return {"name": name, "email": email}
    return _make_user

def test_users(make_user):
    user1 = make_user("Alice", "alice@example.com")
    user2 = make_user("Bob", "bob@example.com")
```

### Omisión Condicional

```python
import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Solo Linux")
def test_linux_feature():
    pass

@pytest.mark.xfail(reason="Bug conocido #123")
def test_known_issue():
    pass
```

---

## Depuración de Pruebas

### Depuración con Print
```bash
pytest -s  # Mostrar declaraciones print
```

### Depurador PDB
```python
def test_debug(browser):
    page = LoginPage(browser)
    import pdb; pdb.set_trace()  # Punto de interrupción
    page.login(username, password)
```

### Fallos Detallados
```bash
pytest -vv  # Extra detallado
pytest --tb=long  # Traceback largo
```

---

## Recursos de Aprendizaje

### Documentación Oficial
- **Documentación Pytest**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **Guía de Fixtures**: [https://docs.pytest.org/en/stable/fixture.html](https://docs.pytest.org/en/stable/fixture.html)

### Tutoriales
- **Real Python**: [https://realpython.com/pytest-python-testing/](https://realpython.com/pytest-python-testing/)
- **Test Automation University**: Cursos de Pytest

### Libros
- **Python Testing with pytest** por Brian Okken

---

## Resumen

Pytest es el framework de pruebas que impulsa esta automatización:
- **Sintaxis simple** - Escribir pruebas como funciones con `assert`
- **Fixtures poderosos** - Lógica de configuración/limpieza reutilizable
- **Ecosistema rico** - Plugins para reportes, ejecución paralela, etc.
- **Organización flexible** - Markers, parametrización, descubrimiento

**Próximos Pasos**:
- Revisa `conftest.py` para ver fixtures en acción
- Explora el directorio `tests/` para ejemplos de pruebas
- Consulta [Mejores Prácticas](../best_practices.md) para guías de pruebas

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  