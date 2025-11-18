# Python para Automatización de Pruebas

## ¿Qué es Python?

**Python** es un lenguaje de programación interpretado de alto nivel conocido por su simplicidad y legibilidad. Es uno de los lenguajes más populares para automatización de pruebas.

**Documentación Oficial**: [https://docs.python.org/3/](https://docs.python.org/3/)

---

## ¿Por qué Python para Automatización QA?

### Ventajas

1. **Fácil de Aprender y Leer**
   - Sintaxis simple y limpia
   - Se lee como inglés
   - Baja barrera de entrada para ingenieros QA

2. **Ecosistema Rico**
   - Selenium, Pytest, Requests, etc.
   - Biblioteca estándar extensa
   - Comunidad activa y paquetes (PyPI)

3. **Multiplataforma**
   - Funciona en Windows, Linux, macOS
   - El mismo código se ejecuta en todas partes

4. **Desarrollo Rápido**
   - Menos código para escribir
   - Prototipado rápido
   - Shell interactivo para pruebas

5. **Adopción Industrial**
   - Ampliamente usado en automatización QA
   - Gran base de talento
   - Recursos de aprendizaje extensos

---

## Fundamentos de Python para Este Framework

### Variables y Tipos de Datos

```python
# Cadenas
username = "user@example.com"
password = "SecurePass123"

# Números
timeout = 10
retry_count = 3

# Booleanos
is_logged_in = True
test_passed = False

# Listas
locators = ["#email", "#password", "#submit"]
test_data = ["user1", "user2", "user3"]

# Diccionarios
user = {
    "email": "user@example.com",
    "password": "pass123",
    "name": "Test User"
}

# Tuplas (inmutables)
locator = ("css", "#email")
```

### Funciones

```python
def login(username, password):
    """Inicia sesión de un usuario."""
    # Cuerpo de la función
    print(f"Iniciando sesión {username}")
    return True

# Llamar función
result = login("user@example.com", "pass123")
```

### Clases y Objetos

```python
class LoginPage:
    """Representa la página de inicio de sesión."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        # Lógica de login
        pass

# Crear instancia
page = LoginPage(driver)
page.login("user@example.com", "pass123")
```

### Importaciones

```python
# Importar módulo completo
import os

# Importar elementos específicos
from selenium import webdriver
from selenium.webdriver.common.by import By

# Importar con alias
import pytest as pt
```

### Control de Flujo

```python
# Declaraciones if
if username and password:
    login(username, password)
else:
    print("Faltan credenciales")

# Bucles for
for locator in locators:
    element = driver.find_element(By.CSS_SELECTOR, locator)

# Bucles while
while not is_logged_in:
    attempt_login()
```

### Manejo de Excepciones

```python
try:
    element = driver.find_element(By.ID, "email")
    element.click()
except NoSuchElementException:
    print("Elemento no encontrado")
except TimeoutException:
    print("Tiempo de espera agotado")
finally:
    print("Limpieza")
```

---

## Entornos Virtuales de Python

### ¿Qué es un Entorno Virtual?

Un **entorno virtual** es un entorno Python aislado que mantiene las dependencias del proyecto separadas del Python del sistema.

### ¿Por qué Usar Entornos Virtuales?

1. **Aislamiento de Dependencias**
   - Cada proyecto tiene sus propios paquetes
   - Sin conflictos entre proyectos

2. **Control de Versiones**
   - Fijar versiones específicas de paquetes
   - Entornos reproducibles

3. **Sistema Limpio**
   - No contaminar el Python del sistema
   - Fácil de eliminar y recrear

### Crear Entornos Virtuales

#### Usando `venv` (Incorporado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Linux/macOS)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate

# Desactivar
deactivate
```

#### Usando `virtualenv` (Terceros)

```bash
# Instalar virtualenv
pip install virtualenv

# Crear entorno virtual
virtualenv venv

# Activar (igual que venv)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Gestionar Dependencias

```bash
# Instalar paquetes
pip install selenium pytest

# Instalar desde archivo de requisitos
pip install -r requiriments.txt

# Congelar paquetes actuales
pip freeze > requiriments.txt

# Listar paquetes instalados
pip list

# Desinstalar paquete
pip uninstall selenium
```

---

## Características de Python Usadas en Este Framework

### 1. Programación Orientada a Objetos (POO)

**Clases para Objetos de Página**:
```python
class LoginPage(BaseActions):
    """Objeto de página de login."""
    
    def __init__(self, driver):
        super().__init__(driver)  # Heredar de BaseActions
    
    def login(self, username, password):
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

**Beneficios**:
- Reutilización de código (herencia)
- Encapsulación (ocultar implementación)
- Estructura clara (una clase por página)

### 2. Type Hints (Opcional)

```python
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver

class BrowserManager:
    def __init__(self, browser: Optional[str] = None):
        self.driver: WebDriver = self._start_driver(browser)
    
    def _start_driver(self, browser: str) -> WebDriver:
        # Retorna instancia de WebDriver
        pass
```

**Beneficios**:
- Mejor soporte de IDE
- Código auto-documentado
- Detectar errores de tipo temprano

### 3. F-Strings (Formato de Cadenas)

```python
# Forma moderna (Python 3.6+)
username = "user@example.com"
print(f"Iniciando sesión {username}")

# Formas antiguas
print("Iniciando sesión {}".format(username))
print("Iniciando sesión " + username)
```

### 4. List Comprehensions

```python
# Obtener texto de múltiples elementos
elements = driver.find_elements(By.CSS_SELECTOR, ".product-name")
product_names = [el.text for el in elements]

# Filtrar resultados
jackets = [name for name in product_names if "jacket" in name.lower()]
```

### 5. Context Managers

```python
# Manejo de archivos
with open("test_data.txt", "r") as file:
    data = file.read()
# Archivo cerrado automáticamente

# Context manager personalizado (no usado en este framework, pero útil)
class BrowserContext:
    def __enter__(self):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def __exit__(self, *args):
        self.driver.quit()

with BrowserContext() as driver:
    driver.get("https://example.com")
# Driver cerrado automáticamente
```

### 6. Decoradores

```python
# Los fixtures de Pytest usan decoradores
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Markers de Pytest
@pytest.mark.smoke
def test_critical_feature():
    pass
```

### 7. Generadores y `yield`

```python
# Los fixtures de Pytest usan yield para setup/teardown
@pytest.fixture
def browser():
    # Setup
    driver = webdriver.Chrome()
    
    yield driver  # La prueba se ejecuta aquí
    
    # Teardown
    driver.quit()
```

---

## Biblioteca Estándar de Python

Módulos útiles para automatización de pruebas:

### `os` - Interfaz del Sistema Operativo

```python
import os

# Variables de entorno
base_url = os.getenv("BASE_URL")
username = os.getenv("USERNAME")

# Rutas de archivos
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "test_data.txt")

# Verificar si existe archivo
if os.path.exists(file_path):
    print("Archivo encontrado")
```

### `pathlib` - Rutas de Archivos Orientadas a Objetos

```python
from pathlib import Path

# Forma moderna de manejar rutas
project_root = Path(__file__).parent.parent
config_file = project_root / "config" / "settings.json"

# Verificar si existe
if config_file.exists():
    data = config_file.read_text()
```

### `json` - Datos JSON

```python
import json

# Parsear JSON
data = json.loads('{"name": "Test", "value": 42}')

# Crear JSON
json_string = json.dumps({"name": "Test", "value": 42})

# Leer desde archivo
with open("data.json") as f:
    data = json.load(f)
```

### `datetime` - Fecha y Hora

```python
from datetime import datetime

# Timestamp actual
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Usar en datos de prueba
email = f"test_{timestamp}@example.com"
```

### `random` - Números Aleatorios

```python
import random

# Elección aleatoria
browser = random.choice(["chrome", "firefox"])

# Número aleatorio
user_id = random.randint(1000, 9999)
```

---

## Mejores Prácticas de Python en Este Framework

### 1. Guía de Estilo PEP 8

```python
# Bueno - Seguir PEP 8
class LoginPage:
    def send_login_credentials(self, username, password):
        pass

# Evitar - Mala nomenclatura
class loginpage:
    def SendLoginCredentials(self, username, password):
        pass
```

**Reglas Clave de PEP 8**:
- Clases: `PascalCase`
- Funciones/variables: `snake_case`
- Constantes: `UPPER_SNAKE_CASE`
- 4 espacios para indentación
- Longitud máxima de línea: 79-100 caracteres

### 2. Docstrings

```python
def login(username: str, password: str) -> bool:
    """
    Inicia sesión de un usuario con las credenciales proporcionadas.
    
    Args:
        username: Dirección de correo del usuario
        password: Contraseña del usuario
    
    Returns:
        True si el login es exitoso, False en caso contrario
    """
    # Implementación
    pass
```

### 3. DRY (No Te Repitas)

```python
# Bueno - Función reutilizable
def send_keys(locator, text):
    element = driver.find_element(*locator)
    element.clear()
    element.send_keys(text)

# Usarla múltiples veces
send_keys(email_locator, "user@example.com")
send_keys(password_locator, "pass123")

# Evitar - Código repetido
element = driver.find_element(*email_locator)
element.clear()
element.send_keys("user@example.com")

element = driver.find_element(*password_locator)
element.clear()
element.send_keys("pass123")
```

### 4. Explícito es Mejor que Implícito

```python
# Bueno - Claro y explícito
from selenium.webdriver.common.by import By
locator = (By.CSS_SELECTOR, "#email")

# Evitar - Suposiciones implícitas
locator = "#email"  # ¿Qué tipo? ¿CSS? ¿ID?
```

---

## Gestión de Paquetes de Python

### pip - Instalador de Paquetes

```bash
# Instalar paquete
pip install selenium

# Instalar versión específica
pip install selenium==4.15.0

# Instalar desde requisitos
pip install -r requiriments.txt

# Actualizar paquete
pip install --upgrade selenium

# Desinstalar
pip uninstall selenium

# Mostrar info del paquete
pip show selenium

# Listar paquetes instalados
pip list

# Verificar paquetes desactualizados
pip list --outdated
```

### requirements.txt

```txt
# Dependencias de este framework
selenium>=4.15.0
pytest>=7.4.0
pytest-html>=3.2.0
python-dotenv>=1.0.0
faker>=20.0.0
allure-pytest>=2.13.0
```

---

## Python vs Otros Lenguajes para QA

| Lenguaje | Pros | Contras |
|----------|------|---------|
| **Python** | Fácil de aprender, ecosistema rico | Más lento que lenguajes compilados |
| **Java** | Estándar empresarial, tipado fuerte | Verboso, más código repetitivo |
| **JavaScript** | Nativo web, soporte async | Callback hell, problemas de tipos |
| **C#** | Integración .NET, tipado fuerte | Centrado en Windows |

**Este framework usa Python** por su simplicidad y rico ecosistema de automatización de pruebas.

---

## Recursos de Aprendizaje

### Documentación Oficial
- **Documentación Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Tutorial Python**: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- **Guía de Estilo PEP 8**: [https://pep8.org/](https://pep8.org/)

### Aprendizaje Interactivo
- **Guía para Principiantes Python.org**: [https://wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide)
- **Real Python**: [https://realpython.com/](https://realpython.com/)
- **Python Tutor** (Visualizar código): [https://pythontutor.com/](https://pythontutor.com/)

### Libros
- **"Automate the Boring Stuff with Python"** por Al Sweigart
- **"Python Crash Course"** por Eric Matthes
- **"Fluent Python"** por Luciano Ramalho (Avanzado)

### Comunidades
- **r/learnpython**: [https://www.reddit.com/r/learnpython/](https://www.reddit.com/r/learnpython/)
- **Python Discord**: [https://pythondiscord.com/](https://pythondiscord.com/)
- **Stack Overflow**: Tag `python`

---

## Resumen

Python es el lenguaje que impulsa este framework:
- **Sintaxis simple** - Fácil de aprender y leer
- **Ecosistema rico** - Selenium, Pytest, Faker y más
- **Entornos virtuales** - Configuraciones aisladas y reproducibles
- **Soporte POO** - Implementación limpia de objetos de página
- **Estándar industrial** - Ampliamente adoptado para automatización QA

**Próximos Pasos**:
- Revisa el código Python en `pages/`, `tests/` y `utils/`
- Practica con el shell interactivo de Python (`python`)
- Explora la documentación de [Selenium](selenium.md) y [Pytest](pytest.md)