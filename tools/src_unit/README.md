>English Version: At the Top of this file you are going to see the English version indicated by this sy  mbol 🟦, and below you are going to see the Spanish version indicated by this symbol 🟩, you can choose the one you want to use.

>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.  

# Unit tests as a QA better practice 🟦
>English Version

- Unit tests are a QA practice that helps ensure the quality and reliability of software by testing individual units of code in isolation. They are an important part of the software development process and can help catch bugs and other issues early in the development cycle.

- If we apply this practice to our automation framework, we can catch bugs and other issues early in the development cycle, and can help ensure the quality and reliability of our automation framework.

- If we want to inspirate quality in our role as a QA Engineer, we can start by our own code practices, for that reason we should apply Unit Tests to our automation framework.


## tools/ unit tests

This directory contains lightweight unit tests for page objects under `pages/` that do not require launching a real browser. They use `pytest` and monkeypatching to validate that:

- Methods call the expected `BaseActions` helpers (e.g., `send_keys`, `click`).
- Return values and control flow (e.g., URL checks) work as intended.
- Text extraction and visibility checks are wired to the configured locators.

## How these tests work
  - The tests use a [DummyDriver](cci:2://file:///home/lety/GuideProject/Pro03/Automation-Framework-QA/tools/conftest.py:88:0-88:18) and monkeypatch instance methods to avoid Selenium calls.
  - [tools/conftest.py](cci:7://file:///home/lety/GuideProject/Pro03/Automation-Framework-QA/tools/conftest.py:0:0-0:0) seeds minimal environment variables, provides a dummy `dotenv`, and stubs the minimal `selenium` APIs so imports succeed without installing Selenium.
  - These tests are fast and deterministic; they complement the Selenium integration tests in `tests/`.

## Run unit tests (only tools/)

  - All unit tests (quiet):
    - `pytest tools/src_unit -q`
  - All unit tests (verbose):
    - `pytest tools/src_unit -v`
  - One file:
    - `pytest tools/src_unit/test_login_unit.py -v`
  - One test by name (using -k):
    - `pytest tools/src_unit -k test_search_results_parsing -v`
  - Optional HTML report:
    - `pytest tools/src_unit -v --html=report.unit.html --self-contained-html`

Note: these unit tests are independent of `.env` and do not need Selenium or a browser.

These tests complement the integration-style tests under `tests/` that drive a real browser via Selenium. Use both to get fast feedback (unit) and end-to-end validation (integration).

## Allure reports (optional)

Allure is not forced via [pytest.ini](cci:7://file:///home/lety/GuideProject/Pro03/Automation-Framework-QA/pytest.ini:0:0-0:0) to keep the setup flexible. When you want to generate an Allure report, pass the argument via CLI:

- For integration tests:
  - `pytest tests --alluredir=reports/allure-results`
- For unit tests (tools/):
  - `pytest tools --alluredir=reports/allure-results`

>Monkeypatching is a technique used in unit testing to modify the behavior of a function or method at runtime. It is often used to replace or mock the behavior of a function or method in order to test the behavior of a larger system or component.



-----
# Prruebas Unitarias como Buenas Prácticas de QA  🟩
>Version en Español

- Las pruebas unitarias son una práctica de QA que ayuda a asegurar la calidad y la fiabilidad del software al probar unidades individuales de código en aislamiento. Son una parte importante del proceso de desarrollo de software y pueden ayudar a detectar errores y otros problemas temprano en el ciclo de desarrollo.

- Si aplicamos esta práctica a nuestro framework de automatización, podemos detectar errores y otros problemas temprano en el ciclo de desarrollo, y podemos ayudar a asegurar la calidad y la fiabilidad de nuestro framework de automatización.

- Si queremos inspirar calidad en nuestro rol como QA Engineer, podemos comenzar por nuestras propias prácticas de código, por eso debemos aplicar pruebas unitarias a nuestro framework de automatización.




>Version en Español

# Pruebas Unitarias para Objetos de Página (tools/)

Este repositorio incluye un módulo de pruebas unitarias aislado en `tools/` para validar la lógica de `pages/` sin abrir un navegador real ni requerir Selenium.

- Qué se valida
  - Llamadas a los helpers de `BaseActions` (por ejemplo, `send_keys`, `click`).
  - Flujo de control y valores de retorno (por ejemplo, verificación de URL tras una acción).
  - Rutas de visibilidad y extracción de textos (por ejemplo, `get_text`, `get_texts`).

- Cómo funciona
  - Las pruebas usan un `DummyDriver` y aplican monkeypatch a métodos de instancia para evitar llamadas reales a Selenium.
  - `tools/conftest.py` inicializa variables de entorno mínimas, provee un `dotenv` de prueba y simula las APIs mínimas de `selenium` para que las importaciones funcionen sin instalar Selenium.
  - Estas pruebas son rápidas y determinísticas; complementan las pruebas de integración con Selenium ubicadas en `tests/`.

- Ejecutar solo las pruebas unitarias (tools/)
  - Todas las pruebas unitarias (silencioso/quiet):
    - `pytest tools -q`
  - Todas las pruebas unitarias (detallado/verbose):
    - `pytest tools -v`
  - Un archivo específico:
    - `pytest tools/test_login_unit.py -v`
  - Un test por nombre (usando -k):
    - `pytest tools -k test_search_results_parsing -v`
  - Reporte HTML opcional:
    - `pytest tools -v --html=report.unit.html --self-contained-html`

Nota: estas pruebas unitarias son independientes de `.env` y no requieren Selenium ni un navegador real.


- Marcadores (solo si los tests están marcados):
  - `pytest -m smoke -v`
  - `pytest -m regression -v`

Nota: `-m` filtra por marcador (marker), no por nombre de archivo. Para ejecutar un archivo concreto, pasa la ruta del archivo; para localizar por nombre de test, usa `-k`.

## Dependencias

- Para ejecutar pruebas de integración con Selenium:
  - `pip install -r requiriments.txt`   # Nota: el archivo en este repo se llama `requiriments.txt`
- Para ejecutar únicamente las pruebas unitarias (tools/), no se requieren dependencias extra porque la suite simula Selenium y dotenv.

## Gestión de drivers (drivers de navegador)

- Con Selenium 4.6+ se recomienda usar Selenium Manager, que resuelve y descarga el driver automáticamente. En la mayoría de los casos NO necesitas binarios locales.
- Si tu entorno no permite descargas (red restringida, offline) o deseas fijar una versión concreta de driver, puedes colocar el binario en `driver/` y apuntar su ruta por variable de entorno:
  - Chrome: `CHROME_DRIVER_PATH=/ruta/absoluta/a/chromedriver`
  - Firefox: `FIREFOX_DRIVER_PATH=/ruta/absoluta/a/geckodriver`
- En Linux/macOS no uses `.exe` (solo Windows). Asegura permisos de ejecución (ej. `chmod +x chromedriver`).
- Consulta `driver/README.md` para más detalles educativos y recomendaciones de buenas prácticas.



## Example execution:

**Example execution (quiet): `pytest tools/src_unit -q`**

```
user@user-my-pc:~/GuideProject/Automation-Framework-QA$ pytest tools/src_unit -q

tools/test_account_user_unit.py::test_account_welcome_visibility_and_text PASSED                [ 16%]
tools/test_form_submission_unit.py::test_form_submission_fills_and_submits PASSED               [ 33%]
tools/test_login_unit.py::test_login_calls_and_redirect PASSED                                  [ 50%]
tools/test_login_unit.py::test_login_negative_error_visible PASSED                              [ 66%]
tools/test_search_product_unit.py::test_search_types_query_and_submits PASSED                   [ 83%]
tools/test_search_product_unit.py::test_search_results_parsing PASSED                           [100%]

========================================== 6 passed in 0.01s ==========================================
user@user-my-pc:~/GuideProject/Automation-Framework-QA$ 

```

**Example execution (verbose): `pytest tools/src_unit -v`**

```
user@user-my-pc:~/GuideProject/Automation-Framework-QA$ pytest tools/src_unit -v
================================================================ test session starts ================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/user/GuideProject/Automation-Framework-QA
configfile: pytest.ini
collected 6 items                                                                                                                                   

tools/test_account_user_unit.py::test_account_welcome_visibility_and_text PASSED                                                              [ 16%]
tools/test_form_submission_unit.py::test_form_submission_fills_and_submits PASSED                                                             [ 33%]
tools/test_login_unit.py::test_login_calls_and_redirect PASSED                                                                                [ 50%]
tools/test_login_unit.py::test_login_negative_error_visible PASSED                                                                            [ 66%]
tools/test_search_product_unit.py::test_search_types_query_and_submits PASSED                                                                 [ 83%]
tools/test_search_product_unit.py::test_search_results_parsing PASSED                                                                         [100%]

================================================================= 6 passed in 0.01s =================================================================