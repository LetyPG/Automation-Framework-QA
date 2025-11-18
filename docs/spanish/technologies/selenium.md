# Selenium WebDriver

## ¿Qué es Selenium WebDriver?

**Selenium WebDriver** es un framework de automatización de navegadores que permite controlar navegadores web programáticamente. Es el estándar de la industria para automatización de pruebas UI.

**Documentación Oficial**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)

---

## ¿Por qué Selenium para Pruebas UI?

### Ventajas

1. **Soporte Multi-Navegador**
   - Chrome, Firefox, Safari, Edge
   - El mismo código de prueba funciona en todos los navegadores

2. **Múltiples Bindings de Lenguajes**
   - Python, Java, C#, JavaScript, Ruby
   - Este framework usa Python

3. **Pruebas en Navegador Real**
   - Las pruebas se ejecutan en navegadores reales
   - Valida la experiencia real del usuario

4. **Código Abierto y Comunidad Activa**
   - Gratis para usar
   - Documentación extensa y soporte

5. **Estándar de la Industria**
   - Ampliamente adoptado en automatización QA
   - Gran ecosistema de herramientas y plugins

---

## Conceptos Fundamentales

### WebDriver

La interfaz principal para controlar el navegador.

```python
from selenium import webdriver

# Crear una instancia de WebDriver
driver = webdriver.Chrome()

# Navegar a una URL
driver.get("https://example.com")

# Cerrar el navegador
driver.quit()
```

### Localizadores

Estrategias para encontrar elementos en una página:

| Estrategia | Ejemplo | Caso de Uso |
|----------|---------|----------|
| `ID` | `By.ID, "email"` | Identificador único de elemento |
| `CSS_SELECTOR` | `By.CSS_SELECTOR, "#email"` | Selección basada en CSS |
| `XPATH` | `By.XPATH, "//input[@id='email']"` | Rutas complejas de elementos |
| `CLASS_NAME` | `By.CLASS_NAME, "btn-primary"` | Elementos por clase |
| `NAME` | `By.NAME, "username"` | Elementos de formulario |
| `TAG_NAME` | `By.TAG_NAME, "button"` | Elementos por etiqueta |
| `LINK_TEXT` | `By.LINK_TEXT, "Sign In"` | Texto exacto del enlace |
| `PARTIAL_LINK_TEXT` | `By.PARTIAL_LINK_TEXT, "Sign"` | Texto parcial del enlace |

**Mejor Práctica**: Preferir `ID` y `CSS_SELECTOR` por velocidad y confiabilidad.

### WebElement

Representa un elemento HTML en la página.

```python
from selenium.webdriver.common.by import By

# Encontrar un elemento
element = driver.find_element(By.ID, "email")

# Interactuar con el elemento
element.send_keys("user@example.com")  # Escribir texto
element.click()                         # Hacer clic
element.clear()                         # Limpiar entrada
text = element.text                     # Obtener texto
```

### Esperas

Manejar contenido dinámico y problemas de tiempo:

#### Espera Implícita
```python
driver.implicitly_wait(10)  # Esperar hasta 10 segundos por elementos
```

#### Espera Explícita (Recomendada)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "email")))
```

**Este framework usa esperas explícitas** en `BaseActions` para confiabilidad.

---

## Cómo Este Framework Usa Selenium

### 1. Gestión de Navegador (`utils/browser_manager.py`)

Abstrae la creación de WebDriver:

```python
class BrowserManager:
    def __init__(self, browser="chrome"):
        self.driver = self._start_driver(browser)
    
    def _start_driver(self, browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)
        # ... Firefox, etc.
```

**Beneficios**:
- Fácil cambio de navegador
- Configuración centralizada
- Selenium Manager maneja drivers automáticamente

### 2. Acciones Base (`pages/base_actions.py`)

Envuelve operaciones comunes de Selenium:

```python
class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
```

**Beneficios**:
- Esperas automáticas
- Manejo de errores
- Reutilizable en todas las páginas

### 3. Objetos de Página

Usar `BaseActions` para interactuar con páginas:

```python
class LoginPage(BaseActions):
    def login(self, username, password):
        self.send_keys(Configuration.USER_NAME_INPUT, username)
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)
        self.click(Configuration.LOGIN_BUTTON)
```

---

## Selenium Manager (Nuevo en 4.6+)

**Selenium Manager** descarga y gestiona automáticamente los drivers de navegador.

### Antes de Selenium Manager
```bash
# Pasos manuales:
1. Descargar chromedriver
2. Agregar al PATH o especificar ubicación
3. Actualizar cuando el navegador se actualiza
```

### Con Selenium Manager
```python
# Solo esto:
driver = webdriver.Chrome()
# ¡Selenium Manager maneja el resto!
```

**Este framework aprovecha Selenium Manager** - no se necesita gestión manual de drivers.

**Anulación Opcional**:
```bash
# Si necesitas un driver específico
export CHROME_DRIVER_PATH=/ruta/a/chromedriver
```

---

## Operaciones Comunes de Selenium

### Navegación
```python
driver.get("https://example.com")      # Navegar a URL
driver.back()                          # Retroceder
driver.forward()                       # Avanzar
driver.refresh()                       # Refrescar página
current_url = driver.current_url       # Obtener URL actual
```

### Interacción con Elementos
```python
element.click()                        # Hacer clic
element.send_keys("text")              # Escribir
element.clear()                        # Limpiar entrada
element.submit()                       # Enviar formulario
```

### Información del Elemento
```python
text = element.text                    # Texto visible
value = element.get_attribute("value") # Valor del atributo
is_displayed = element.is_displayed()  # Visibilidad
is_enabled = element.is_enabled()      # Estado habilitado
```

### Ejecución de JavaScript
```python
driver.execute_script("window.scrollTo(0, 500);")
driver.execute_script("arguments[0].click();", element)
```

### Alertas
```python
alert = driver.switch_to.alert
alert.accept()      # Hacer clic en OK
alert.dismiss()     # Hacer clic en Cancelar
alert.send_keys()   # Escribir en alerta
```

### Ventanas/Pestañas
```python
driver.switch_to.window(window_handle)
driver.window_handles  # Lista de todas las ventanas
```

---

## Condiciones Esperadas

Usadas con esperas explícitas:

```python
from selenium.webdriver.support import expected_conditions as EC

# Presencia del elemento
EC.presence_of_element_located((By.ID, "email"))

# Visibilidad del elemento
EC.visibility_of_element_located((By.ID, "email"))

# Elemento clickeable
EC.element_to_be_clickable((By.ID, "submit"))

# Texto en elemento
EC.text_to_be_present_in_element((By.ID, "message"), "Success")

# URL contiene
EC.url_contains("dashboard")

# Título es
EC.title_is("Home Page")
```

---

## Mejores Prácticas en Este Framework

### 1. Usar Esperas Explícitas
```python
# Bueno - BaseActions usa esperas explícitas
self.wait.until(EC.element_to_be_clickable(locator))

# Evitar - Esperas implícitas o sleep
time.sleep(5)
```

### 2. Preferir Selectores CSS
```python
# Bueno - Rápido y legible
locator = (By.CSS_SELECTOR, "#email")

# Usar con moderación - Más lento, frágil
locator = (By.XPATH, "//div[@class='form']//input[@id='email']")
```

### 3. Abstraer Detalles de Selenium
```python
# Bueno - El objeto de página oculta Selenium
page.login(username, password)

# Evitar - Selenium en pruebas
driver.find_element(By.ID, "email").send_keys(username)
```

### 4. Manejar Elementos Obsoletos
```python
def click(self, locator):
    try:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    except StaleElementReferenceException:
        # Re-encontrar elemento
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
```

---

## Solución de Problemas

### Elemento No Encontrado
```python
# Verificar que el localizador sea correcto
# Aumentar tiempo de espera
# Verificar que el elemento esté en el DOM (no en iframe)
```

### Elemento No Clickeable
```python
# Esperar a que el elemento sea clickeable
# Verificar si el elemento está cubierto por otro elemento
# Desplazar elemento a la vista
```

### Referencia de Elemento Obsoleto
```python
# Re-encontrar elemento después de cambios en la página
# Usar localizadores frescos, no elementos almacenados
```

### Excepciones de Timeout
```python
# Aumentar tiempo de espera
# Verificar si el elemento realmente aparece
# Verificar estrategia del localizador
```

---

## Selenium vs Otras Herramientas

| Herramienta | Caso de Uso | Pros | Contras |
|------|----------|------|------|
| **Selenium** | Automatización UI | Navegadores reales, multi-navegador | Más lento que headless |
| **Playwright** | Apps web modernas | Rápido, API moderna | Más nuevo, comunidad más pequeña |
| **Cypress** | Apps JavaScript | Amigable para desarrolladores | Solo JavaScript |
| **Puppeteer** | Automatización Chrome | Rápido, headless | Solo Chrome |

**Este framework usa Selenium** por su madurez, comunidad y soporte multi-navegador.

---

## Recursos de Aprendizaje

### Documentación Oficial
- **Documentación Selenium**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- **Especificación WebDriver**: [https://w3c.github.io/webdriver/](https://w3c.github.io/webdriver/)

### Tutoriales
- **Selenium con Python**: [https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/)
- **Test Automation University**: [https://testautomationu.applitools.com/](https://testautomationu.applitools.com/)

### Comunidad
- **Foro Selenium**: [https://groups.google.com/g/selenium-users](https://groups.google.com/g/selenium-users)
- **Stack Overflow**: Tags `selenium` y `selenium-webdriver`

---

## Resumen

Selenium WebDriver es la base de este framework:
- **Automatización de navegadores** - Controlar navegadores reales programáticamente
- **Pruebas multi-navegador** - Mismas pruebas en Chrome, Firefox, etc.
- **Estándar de la industria** - Ampliamente adoptado, bien documentado
- **Abstraído en el framework** - Oculto detrás de `BaseActions` y objetos de página

**Próximos Pasos**:
- Revisa [BaseActions](../base_actions.md) para ver Selenium en acción
- Explora [Modelo de Objeto de Página](../page_object_model.md) para patrones de abstracción
- Consulta [Mejores Prácticas](../best_practices.md) para consejos de Selenium