# Paradigma de Programación: Programación Orientada a Objetos (POO)

Este documento explica el paradigma de Programación Orientada a Objetos (POO) y cómo se aplica en este framework de automatización QA.

---

## ¿Qué es la Programación Orientada a Objetos?

**La Programación Orientada a Objetos (POO)** es un paradigma de programación basado en el concepto de "objetos" que contienen datos (atributos) y código (métodos). La POO organiza el diseño de software alrededor de datos y objetos en lugar de funciones y lógica.

---

## ¿Por qué POO para Automatización de Pruebas?

### Ventajas

1. **Modularidad** - Código organizado en objetos autocontenidos
2. **Reutilización** - Los objetos pueden reutilizarse en diferentes pruebas
3. **Mantenibilidad** - Cambios aislados a clases específicas
4. **Escalabilidad** - Fácil agregar nuevas características sin romper código existente
5. **Legibilidad** - La estructura del código refleja conceptos del mundo real

---

## Conceptos Fundamentales de POO

### 1. Clases y Objetos

#### Clase
Una **clase** es un plano o plantilla para crear objetos.

```python
# Definición de clase
class LoginPage:
    """Plano para objetos de página de login."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        # Lógica de login
        pass
```

#### Objeto
Un **objeto** es una instancia de una clase.

```python
# Crear objetos (instancias)
browser = webdriver.Chrome()
login_page = LoginPage(browser)  # Objeto creado de la clase LoginPage
account_page = AccountUserPage(browser)  # Otro objeto

# Cada objeto tiene sus propios datos
login_page.driver  # Instancia de navegador para página de login
account_page.driver  # Instancia de navegador para página de cuenta
```

**En Este Framework**:
- Cada página es una clase (`LoginPage`, `AccountUserPage`, `SearchProductPage`)
- Las pruebas crean objetos de estas clases
- Cada objeto representa una instancia específica de página

---

### 2. Encapsulación

**Encapsulación** significa agrupar datos y métodos que operan sobre esos datos dentro de una sola unidad (clase), y ocultar detalles internos de implementación.

#### Ejemplo Sin Encapsulación

```python
# ❌ Malo - Implementación expuesta
def test_login(browser):
    browser.find_element(By.ID, "email").send_keys("user@example.com")
    browser.find_element(By.ID, "password").send_keys("pass123")
    browser.find_element(By.ID, "submit").click()
    # La prueba sabe CÓMO hacer login (detalles de implementación)
```

#### Ejemplo Con Encapsulación

```python
# ✅ Bueno - Implementación oculta
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._email_input = (By.ID, "email")  # Atributo privado
        self._password_input = (By.ID, "password")
        self._submit_button = (By.ID, "submit")
    
    def login(self, username, password):
        """Método público - oculta implementación."""
        self.driver.find_element(*self._email_input).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.driver.find_element(*self._submit_button).click()

def test_login(browser):
    page = LoginPage(browser)
    page.login("user@example.com", "pass123")
    # La prueba sabe QUÉ hacer, no CÓMO
```

**Beneficios**:
- Las pruebas no conocen detalles de implementación
- Se pueden cambiar localizadores sin cambiar pruebas
- Interfaz clara (métodos públicos) vs implementación (atributos privados)

**En Este Framework**:
- Las clases de página encapsulan interacciones de página
- Las pruebas usan métodos públicos como `login()`, `search()`, `submit()`
- Los localizadores y detalles de implementación están ocultos

---

### 3. Herencia

**Herencia** permite que una clase herede atributos y métodos de otra clase.

#### Herencia Básica

```python
# Clase padre (Clase base)
class BaseActions:
    """Operaciones Selenium reutilizables."""
    
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

# Clase hija (Clase derivada)
class LoginPage(BaseActions):
    """Hereda todos los métodos de BaseActions."""
    
    def login(self, username, password):
        # Puede usar métodos heredados
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

#### Sobrescritura de Métodos

```python
class BaseActions:
    def open(self, url):
        """Implementación por defecto."""
        self.driver.get(url)

class LoginPage(BaseActions):
    def open(self, url):
        """Sobrescribir con comportamiento personalizado."""
        super().open(url)  # Llamar método padre
        self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        print("Página de login cargada")
```

**Beneficios**:
- Reutilización de código (principio DRY)
- Comportamiento consistente entre páginas
- Fácil extender funcionalidad

**En Este Framework**:
- `BaseActions` es la clase padre
- Todas las clases de página heredan de `BaseActions`
- Las clases de página obtienen `click()`, `send_keys()`, `get_text()`, etc. gratis

---

### 4. Polimorfismo

**Polimorfismo** significa "muchas formas" - la capacidad de usar una interfaz común para diferentes tipos.

#### Ejemplo: Mismo Método, Diferente Comportamiento

```python
class BaseActions:
    def get_page_title(self):
        """Implementación por defecto."""
        return self.driver.title

class LoginPage(BaseActions):
    def get_page_title(self):
        """Implementación personalizada para página de login."""
        return "Customer Login"

class AccountPage(BaseActions):
    def get_page_title(self):
        """Implementación personalizada para página de cuenta."""
        return "My Account"

# Polimorfismo en acción
def verify_page_title(page):
    """Funciona con cualquier objeto de página."""
    title = page.get_page_title()  # Comportamiento diferente según tipo de objeto
    assert title is not None

# Todos los tipos de página funcionan con la misma función
verify_page_title(LoginPage(driver))
verify_page_title(AccountPage(driver))
```

#### Duck Typing (Polimorfismo de Python)

```python
# Si camina como pato y grazna como pato, es un pato
def perform_login(page, username, password):
    """Funciona con cualquier objeto que tenga un método login."""
    page.login(username, password)

# Ambos funcionan porque tienen método login()
perform_login(LoginPage(driver), "user@example.com", "pass123")
perform_login(AdminLoginPage(driver), "admin@example.com", "admin123")
```

**Beneficios**:
- Código flexible que funciona con múltiples tipos
- Fácil agregar nuevos tipos de página
- Interfaz común para diferentes implementaciones

**En Este Framework**:
- Todas las páginas heredan de `BaseActions` (interfaz común)
- Las pruebas pueden trabajar con cualquier objeto de página
- Fácil agregar nuevas páginas sin cambiar estructura de pruebas

---

### 5. Abstracción

**Abstracción** significa ocultar detalles complejos de implementación y mostrar solo características esenciales.

#### Ejemplo: Conceptos Abstractos

```python
# Abstracción de alto nivel
def test_user_can_login(browser):
    page = LoginPage(browser)
    page.login(username, password)  # Abstracto - oculta complejidad
    assert page.is_login_successful()

# Lo que está oculto:
# - Encontrar elementos
# - Esperar por elementos
# - Limpiar campos
# - Enviar teclas
# - Hacer clic en botones
# - Manejar excepciones
```

#### Niveles de Abstracción

```python
# Nivel 1: Selenium Crudo (Baja abstracción)
driver.find_element(By.ID, "email").send_keys("user@example.com")

# Nivel 2: BaseActions (Abstracción media)
base_actions.send_keys((By.ID, "email"), "user@example.com")

# Nivel 3: Objeto de Página (Alta abstracción)
login_page.login("user@example.com", "pass123")

# Nivel 4: Prueba (Abstracción más alta)
test_login_success()  # Solo describe qué probar
```

**Beneficios**:
- Simplifica operaciones complejas
- Las pruebas se enfocan en lógica de negocio
- Detalles de implementación ocultos

**En Este Framework**:
- Las pruebas trabajan en el nivel más alto de abstracción
- Los objetos de página proporcionan métodos de nivel de negocio
- `BaseActions` maneja la complejidad de Selenium
- Las pruebas son legibles y mantenibles

---

## POO en Este Framework: Ejemplos Prácticos

### Ejemplo 1: Clase LoginPage

```python
class LoginPage(BaseActions):
    """
    Encapsulación: Agrupa datos y comportamiento de página de login
    Herencia: Hereda de BaseActions
    Abstracción: Oculta complejidad de Selenium
    """
    
    def __init__(self, driver):
        """Constructor - inicializa objeto."""
        super().__init__(driver)  # Llamar constructor padre
    
    def login(self, username, password):
        """
        Método público - abstracción de alto nivel.
        Encapsula lógica de login.
        """
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
    
    def is_login_successful(self):
        """Método público - verifica éxito de login."""
        return self.is_visible(Configuration.ACCOUNT_WELCOME_MESSAGE)
```

### Ejemplo 2: Usando el Objeto LoginPage

```python
def test_login_success(browser):
    """
    La prueba usa conceptos POO:
    - Crea objeto (LoginPage)
    - Llama métodos en objeto
    - Trabaja en alto nivel de abstracción
    """
    # Crear objeto
    page = LoginPage(browser)
    
    # Usar métodos del objeto (abstracción)
    page.open(Configuration.LOGIN_URL)
    page.login(Configuration.USERNAME, Configuration.PASSWORD)
    
    # Verificar (polimorfismo - funciona con cualquier página)
    assert page.is_login_successful()
```

### Ejemplo 3: Múltiples Objetos de Página

```python
def test_user_journey(browser):
    """
    Múltiples objetos trabajando juntos.
    Cada objeto encapsula el comportamiento de su página.
    """
    # Login
    login_page = LoginPage(browser)
    login_page.open(Configuration.LOGIN_URL)
    login_page.login(username, password)
    
    # Búsqueda
    search_page = SearchProductPage(browser)
    search_page.search("jacket")
    
    # Ver cuenta
    account_page = AccountUserPage(browser)
    assert account_page.is_welcome_message_visible()
```

---

## Resumen

Este framework usa POO para crear:
- **Modular** - Cada página es una clase separada
- **Reutilizable** - `BaseActions` compartido entre páginas
- **Mantenible** - Cambios aislados a clases específicas
- **Escalable** - Fácil agregar nuevas páginas
- **Legible** - Las pruebas se enfocan en lógica de negocio

**Conceptos Clave de POO Aplicados**:
1. ✅ **Clases y Objetos** - Los objetos de página representan páginas
2. ✅ **Encapsulación** - Ocultar detalles de implementación
3. ✅ **Herencia** - Reutilizar funcionalidad de `BaseActions`
4. ✅ **Polimorfismo** - Interfaz común para todas las páginas
5. ✅ **Abstracción** - Métodos de prueba de alto nivel

---

## Próximos Pasos

- Revisa [Estrategia de Automatización](automation_strategy.md) para decisiones arquitectónicas
- Consulta [Estándares de Código](coding_repository_standards.md) para principios SOLID
- Explora [Modelo de Objeto de Página](page_object_model.md) para detalles de POM
- Lee las clases de página reales en el directorio `pages/`

---

**La POO hace que este framework sea profesional, mantenible y escalable.**