# Guía de Inicio

Esta guía te ayudará a configurar y ejecutar tu primera prueba automatizada con este framework. Antes de empezar a usar este `framework`, recomiendo que estudies y comprendas los conceptos básicos necesarios para usarlo. 
Por otro lado, debes entender el uso principal del `terminal`, teniendo en cuenta que vas a ejecutar la instalación y la ejecución de los tests desde el terminal.

---

## Requisitos Previos

Antes de comenzar, te debes asegurar de tener instalado lo siguiente:

### Software Requerido
- **Python 3.12+** - [Descargar Python](https://www.python.org/downloads/)
- **Git** - [Descargar Git](https://git-scm.com/downloads)
- **Selenium WebDriver** - [Descargar Selenium WebDriver](https://www.selenium.dev/downloads/)
- **Google Chrome o Firefox** - Última versión

### Comandos para verificar la instalación

- **Verificar versión de Python**
Debe mostrar 3.12 o superior
```bash
python --version 
```

- **Verificar pip (gestor de paquetes de Python)**
Debe mostrar la versión de pip instalada
```bash
pip --version
```

- **Verificar Git**
Debe mostrar la versión de Git instalada
```bash
git --version
```
- **Verificar Selenium WebDriver**
Debe mostrar la versión de Selenium WebDriver instalada
```bash
pip show selenium
```

En caso de no tener estos programas instalados, debes instalarlos antes de continuar, desde la web oficial de cada uno, o si tienes conocimientos avanzados de terminal puedes usar un gestor de paquetes como `apt` en Linux o `brew` en macOS.

- **Git**
```
sudo apt update
sudo apt install git
```

- **Python**
```
sudo apt update
sudo apt install python3
```

- **pip**
```
sudo apt update
sudo apt install python3-pip
```

- **Selenium WebDriver**
```
pip install selenium
```


**Using the terminal for installing: Windows**

Attending to the specific Shell of Windows (CMD or PowerShell) the commands migth be different, but the process is the same, in that case ensure searching for the specific command for each one.

- **Git**
```
pip install git
```

- **Python**
```
pip install python
```

- **pip**
```
pip install pip
```

- **Selenium WebDriver**
```
pip install selenium
```

---- 

# Iniciando el Proyecto
## Paso 1: Clonar el Repositorio

```bash
# Clonar el repositorio
git clone https://github.com/LetyPG/Automation-Framework-QA.git

# Navegar al directorio del proyecto
cd Automation-Framework-QA
```

---

## Paso 2: Configurar Entorno Virtual de Python (Recomendado)

Usar un entorno virtual aísla las dependencias del proyecto de tu Python del sistema.

### En Linux/macOS:
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

### En Windows:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate
```

Deberías ver `(venv)` en tu prompt de terminal cuando esté activado.

---

## Paso 3: Instalar Dependencias

```bash
# Instalar todos los paquetes requeridos
pip install -r requiriments.txt
```

**Nota**: El archivo se llama `requiriments.txt` (no `requirements.txt`) en este repositorio.

### Lo que se Instala:
- `selenium` - Automatización de navegadores
- `pytest` - Framework de pruebas
- `pytest-html` - Reportes HTML de pruebas
- `python-dotenv` - Gestión de variables de entorno
- `faker` - Generación de datos de prueba
- `allure-pytest` - Reportes avanzados (opcional)

---

## Paso 4: Configurar Variables de Entorno

Crear un archivo `.env` en el directorio raíz del proyecto:

```bash
# Copiar el archivo de ejemplo
cp docs/spanish/.env_example.txt .env
```

### Editar Archivo `.env`

Abre `.env` y configura los valores de las variables para que coincidan con tu entorno. Por ejemplo, si quieres probar un sitio web diferente, puedes cambiar la variable `BASE_URL` a la URL del sitio web que quieres probar.
Para este proyecto se proporciona como ejemplo un archivo `.env_example.txt`, puedes usarlo como plantilla, ubicado en este mismo directorio `docs/spanish/.env_example.txt`

**Importante**: 
- Reemplaza `USERNAME` y `PASSWORD` con credenciales reales para pruebas de login positivas
- Nunca hagas commit de `.env` al control de versiones (está en `.gitignore`)

---

## Paso 5: Verificar Configuración del Driver del Navegador

Este framework usa **Selenium Manager** (integrado en Selenium 4.6+), que descarga y gestiona automáticamente los drivers de navegador. ¡No necesitas descargar drivers manualmente!

### Opcional: Configuración Manual del Driver

Si prefieres usar un driver local o tu entorno no permite descargas automáticas:

1. Descarga el driver apropiado:
   - **Chrome**: [ChromeDriver](https://chromedriver.chromium.org/)
   - **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Establecer variable de entorno:
   ```bash
   # Para Chrome
   export CHROME_DRIVER_PATH=/ruta/a/chromedriver
   
   # Para Firefox
   export FIREFOX_DRIVER_PATH=/ruta/a/geckodriver
   ```

Ver [driver/README.md](../../driver/README.md) para más detalles.

---

## Paso 6: Ejecutar tu Primera Prueba

- Tests Selenium-based generales :

```
pytest`  (or `pytest -v`)

- Ejecutar todos los tests en un directorio específico <tests/test_directory_name>: 

```
pytest tests/ui_tests -v

```

- Ejecutar un archivo de test específico <tests/test_directory_name/test_file_name.py>:

```
pytest tests/ui_tests/test_account_user.py -v
```

- Ejecutar un test específico por nombre (cualquier suite) con -k:

```
pytest -k test_login_success_if_credentials_present -v
```

- Ejecutar tests por marker (solo si los tests están marcados de manera correspondiente):

```
pytest -m smoke -v
```

```
pytest -m regression -v
```
---

## Paso 7: Generar Reportes de Pruebas

### Reporte HTML
```bash
pytest -v --html=report.html --self-contained-html
```

Abre `report.html` en tu navegador para ver los resultados.

### Reporte Allure (Opcional)
```bash
# Generar resultados de Allure
pytest --alluredir=reports/allure-results

# Servir reporte de Allure
allure serve reports/allure-results
```

---

## Paso 8: Ejecutar Pruebas Unitarias (Sin Navegador Requerido)

Este framework incluye pruebas unitarias para objetos de página que se ejecutan sin lanzar un navegador:

```bash
# Ejecutar todas las pruebas unitarias
pytest tools -v

# Ejecutar archivo de prueba unitaria específico
pytest tools/test_login_unit.py -v

# Ejecutar en modo silencioso
pytest tools -q
```

Ver [tools/README.md](../../tools/README.md) para más detalles.

---

## Problemas Comunes y Soluciones

### Problema: `ModuleNotFoundError: No module named 'selenium'`
**Solución**: Activar entorno virtual e instalar dependencias:
```bash
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requiriments.txt
```

### Problema: `WebDriverException: Message: 'chromedriver' executable needs to be in PATH`
**Solución**: Selenium Manager debería manejar esto automáticamente. Si no:
1. Asegúrate de tener Selenium 4.6+: `pip install --upgrade selenium`
2. O establece la variable de entorno `CHROME_DRIVER_PATH`

### Problema: Las pruebas fallan con "Element not found"
**Solución**: 
1. Verifica si los localizadores en `.env` coinciden con la estructura del sitio web
2. Aumenta el tiempo de espera implícito: Agrega `IMPLICIT_WAIT=5` a `.env`
3. El sitio web puede haber cambiado - actualiza los localizadores en consecuencia

### Problema: Las pruebas de login fallan
**Solución**: 
1. Verifica que `USERNAME` y `PASSWORD` en `.env` sean correctos
2. Asegúrate de que la cuenta existe en el sitio web de prueba
3. Verifica si el sitio web requiere CAPTCHA o 2FA

---

## Próximos Pasos

Ahora que tienes el framework funcionando:

1. **Explora el Código**:
   - Revisa el directorio `pages/` para entender el Modelo de Objeto de Página
   - Consulta `tests/` para ver la estructura de las pruebas
   - Examina `utils/` para funciones auxiliares

2. **Lee la Documentación**:
   - [Resumen del Proyecto](project_overview.md) - Comprende la arquitectura
   - [Estrategia de Automatización](automation_strategy.md) - Aprende las decisiones de diseño
   - [Mejores Prácticas](best_practices.md) - Sigue las guías QA

3. **Experimenta**:
   - Modifica pruebas existentes
   - Agrega nuevos objetos de página
   - Crea nuevos escenarios de prueba
   - Prueba diferentes navegadores (establece `BROWSER=firefox` en `.env`)

4. **Aprende Características Avanzadas**:
   - Datos de prueba dinámicos con Faker
   - Aserciones personalizadas
   - Ejecución paralela de pruebas
   - Integración CI/CD

---

## Comandos de Referencia Rápida

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Ejecutar todas las pruebas
pytest

# Ejecutar con salida detallada
pytest -v

# Ejecutar archivo de prueba específico
pytest tests/test_login.py -v

# Ejecutar por patrón de nombre de prueba
pytest -k login -v

# Ejecutar por marker
pytest -m smoke -v

# Generar reporte HTML
pytest --html=report.html --self-contained-html

# Ejecutar solo pruebas unitarias
pytest tools -v

# Desactivar entorno virtual
deactivate
```

---

## Obtener Ayuda

- **Documentación**: Consulta otros archivos en `docs/spanish/`
- **Problemas**: Revisa los problemas comunes arriba
- **Ejemplos**: Mira las pruebas existentes en el directorio `tests/`
- **Comunidad**: Comparte y aprende con otros ingenieros QA

---

**¡Felicitaciones!** 🎉 Has configurado exitosamente el Marco de Automatización QA. ¡Felices pruebas!
