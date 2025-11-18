

>There are two versions of this README.md, one in English, indicated by 🟦 at the top of this file and one in Spanish, indicated by 🟩, at the bottom, you can choose the one you want to use. 

>Se encuentran dos versiones de este README.md, una en Inglés, indicada por 🟦 en la parte superior de este archivo y otra en Español, indicada por 🟩 en la parte inferior, puedes escoger la que prefieras.



# Project C-QA-Automation-Framework
🟦 **English Version**
>This a Demo Project to create a simple Automation Framework for a web site UI (Magento) and as an educational project, not as a production ready code.



This project is an Automation Testing Framework developed with Python, Pytest and Selenium WebDriver, designed to ensure scalability, maintainability and structural clarity through the application of SOLID principles and software engineering best practices.

This code is recomended for beginners to understand the basic concepts of Automation Framework  using Python, Selenium WebDriver, Pytest, Faker, Allure Reports, and it is not a production ready code.

The C-QA named keeps a consecution of an educative web site [Compilidor QA](https://www.compiladorqa.tech/) (in English means Compiler QA), created to help QA professionals to learn and understand the basic concepts of technology, for that reason was the desicion to used `C-QA` as a short name for this project, of Automation Framework, related to the web site mentioned before.


## Very Important ⚠️  
🟦 I recommended you: 
- First remember that the base to create any program code is to abstract the problem from reality, what I mean to say by this, it is very imortant understand the bussiness logic in which you are working, the scope, the final user and the projects requeriments, also you must create a test plan and decide the test strategy to be used, for example, you can use a test strategy as `Smoke Testing`, `Regression Testing`, `API Testing`, `Mobile Testing`, `UI Testing`, etc.
- Try to understand the code and the structure of the framework, the program logic and the automation fundamentals by using Selenium WebDriver, Pytest and Python
- Not only copy and paste the code, because that is not the point of this project, the point is to understand the code and the structure of the framework.
- Once you understand the code and the structure of the framework, you will be able to create your own framework, and you will be able to automate your own web site UI.
- In addition you can add new features to the framework, such as mobile automation, API automation, CI/CD flow (Jenkins/GitHub Actions), unit tests, etc.
- Also in adition you can include more test modules, and more test cases and the needed libraries to make it work.

## 🟦 Scope
The specific scope of this project is Automation UI practice to explain Selenium Webdriver and Pytest using a simple e-commerce web site.
**Not included**
- Mobile Automation
- API Automation
- CI/CD flow (Jenkins/GitHub Actions)

But as a best practice it is strongly recommended consired this topics for a real and integral Automation Framework.

## 🟦 Objectives

- Automatize critical flows of an e-commerce web site Magento, validating functionalities as login, user registration, search, shopping cart and checkout, reliably and reutilizable.
- Create a simple Automation Framework for a web site UI (Magento) and as an educational project.
- Understand the basic concepts of Automation Framework  using Python, Selenium WebDriver, Pytest, Faker, Allure Reports, and it is not a production ready code.


## 🟦 Technologies used

- **Python 3.12+**
- **Selenium WebDriver**
- **Pytest**
- **Faker** (for dynamic data)
- **Allure Reports**
- **dotenv** (secure configuration management)
- **Jenkins** (for CI/CD)

## 🟦 Code Principles Design SOLID 

- **S: Single Responsibility**  
  
- **O: Open/Closed**  
  
- **L: Liskov Substitution**  
  
- **I: Interface Segregation**  
  
- **D: Dependency Inversion**  
  

## 🟦 Project Directory Structure

```
Automation-Framework-QA/
│
├── docs/                    # Documentation of the framework in markdown format and includes English and Spanish documentation
├── drivers/                 # Drivers for different browsers
├── pages/                   # Clase by page (modelo POM)
├── api/                     # API Module base calss for API tests
├── ci_cd/                   # CI/CD Module base calss for CI/CD tests, contains jenkinsfiles for different jobs (api, staging, smoke, ui), that are used to run the tests in different environments, for example staging job runs the ui tests in staging environment
├── features/                # Feature files for BDD (Behavior-Driven Development)
├── tests/                   # Test cases modules grouped by testing strategy as diffrent suite tests (smoke, regression, api, e2e, etc)
|
├── utils/                   # Configuration, logs, data and helpers, including api_helpers for API validation
├── tools/                   # Unit tests for page objects
├── .env                     # Environment variables and external locators
├── conftest.py              # Pytest global fixtures
├── requirements.txt         # Environment dependencies
└── README.md                # Framework documentation

```
Layered Testing Strategy

This framework supports **three layers** of testing, all reusing the same core logic:

```
┌─────────────────────────────────────────────┐
│   BDD Tests (Acceptance)                    │
│   features/ + tests/bdd_steps_definitions/  │
│   Purpose: Business behavior validation     │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────┴───────────────────────────┐
│   Integration Tests (Functional)            │
│   tests/api_test/ ,  tests/smoke_tests/     │
│   tests/regression_tests/, etc              │
│   Purpose: Detailed functional validation   │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────┴───────────────────────────┐
│   Unit Tests (Component)                    │
│   tools/src_unit/                           │
│   Purpose: Test POMs and API clients        │
└─────────────────────────────────────────────┘
```

**All three layers reuse:**
- `pages/` (Page Objects)
- `api/` (API Clients)
- `utils/` (Helpers and utilities)

----

## 📄 Testing Procedure

## 🟦 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Google Chrome or Firefox** - Latest version
- **Pip** - [Download Pip](https://pip.pypa.io/en/stable/installation/)


## 🟦 Execution Steps

#### 1️⃣ Clone the repository, or download the zip file, or fork the repository.

```
git clone https://github.com/LetyPG/Automation-Framework-QA.git

```

>After you clone the repo on the directory you want, you can run the tests inside of it, for this case is used the directory `Automation-Framework-QA`.

#### 2️⃣ Navigate to the project directory

```
cd Automation-Framework-QA
```

#### 3️⃣ Set Up Python Virtual Environment (Recommended)

Use a virtual environment to isolate project dependencies from your system Python. This is a good practice to keep the development environment clean and organized and avoid conflicts with other dependencies of your system, for example, in case you have a different version of Python installed in your system and the framework requires a different version, the virtual environment will allow you to keep both versions without conflicts.
By executing the following commands in the terminal, you can create and activate a virtual environment, both use the tool `venv` that comes by default with Python.

#### On Linux/macOS:

- Create virtual environment

```
python3 -m venv venv

```

- Activate virtual environment

```
source venv/bin/activate

```

#### On Windows:

- Create virtual environment

```
python -m venv venv

```

- Activate virtual environment

```
venv\Scripts\activate
```

- You should see `(venv)` in your terminal prompt when activated.

#### 4️⃣ Installation of Dependencies

- To run Selenium-based general tests:

```
pip install -r requiriments.txt

```
  
> Note: filename is `requiriments.txt` in this repo, by convention. 

- To run only the unit tests (tools/), no extra dependencies are required because the suite stubs Selenium and dotenv.

#### 5️⃣ Create a .env file and adapt it

- Create a .env file and adapt it to your needs, this is an explanatory framework, so you can adapt it to your needs.



#### 6️⃣ Run tests

Since you already are located in the project directory, on the root directory, you do not need to move to any other directory, you can run the tests from there, using the following commands:


#### Tests directory `tests/`
- General tests:

>This will run all the tests in the project, take care of the time it takes to run all the tests and the resources it uses.

```
pytest`  (or `pytest -v`)

```

- General tests in a specific directory <tests/test_directory_name>:

```
pytest tests/smoke_tests -v

```

- Specific test file <tests/test_directory_name/test_file_name.py>:

```
pytest tests/smoke_tests/test_account_user.py -v

```

- Specific test by name (this will execute any test function in any suite) with -k:

```
pytest -k test_login_success_if_credentials_present -v
```

- Markers (only if tests are marked accordingly):

```
pytest -m smoke -v
```

```
pytest -m regression -v
```

>Note: `-m` filters by marker name, not by test filename. To run a specific file, pass the file path; to match test names, use `-k`.

>Note: You can run tests using `-v` for verbose output or `-q` for quiet output, thats depends on your information needs.

#### 7️⃣ Allure reports (optional)

Allure is not forced via [pytest.ini](cci:7://file:///home/user/GuideProject/Automation-Framework-QA/pytest.ini:0:0-0:0) to keep the setup flexible. When you want to generate an Allure report, pass the argument via CLI:

- For general tests:

```
pytest tests --alluredir=reports/allure-results

```


#### Unit tests directory `tools/src_unit/`
- Unit tests :

```
pytest tools/src_unit -v
```
- Unit test file `<tools/test_unit_directory_name/unit_test_file_name.py>`:

```
pytest tools/src_unit/test_login_unit.py -v
```

#### API tests directory `api/`

- API tests :

```
pytest tests/api_test/ -v
```

- API test suite `<tests/api_test/test_directory_name/test_file_name.py>`:

```
pytest tests/api_test/test_user/ -v
```

- API test file `<tests/api_test/test_directory_name/test_file_name.py>`:

```
pytest tests/api_test/test_user/test_user_service.py
 -v
```

- Run by markers
```
pytest -m api -v
```

- Generate Allure reports
```
pytest tests/api_test/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

- Parallel execution
```
pytest tests/api_test/ -n 4
```

- With coverage
```
pytest tests/api_test/ --cov=api --cov-report=html
```

#### Run All BDD Tests
```bash
pytest features/ -v
```

#### Run Specific Feature (test feature)
```bash
pytest features/api/user_service.feature -v
pytest features/ui/login.feature -v
```

#### Run by Tags
```bash
# Smoke tests only
pytest features/ -m smoke

# API tests only
pytest features/ -m api

# Critical scenarios
pytest features/ -m critical

# Negative scenarios
pytest features/ -m negative
```

### Generate BDD Reports
```bash
# HTML report
pytest features/ --html=reports/bdd_report.html

# Allure report
pytest features/ --alluredir=reports/allure-results
allure serve reports/allure-results

```


## Recommended Testing Distribution

For a balanced QA framework:

| Test Type | % of Tests | Purpose |
|-----------|-----------|---------|
| **BDD (Acceptance)** | 15-20% | Critical user flows, acceptance criteria |
| **Integration/Functional** | 60-70% | Detailed API/UI testing, edge cases |
| **Unit Tests** | 10-15% | Test framework components (POMs, utils) |
| **E2E** | 5-10% | Full system integration |

**BDD Focus Areas:**
- Critical happy paths
- Key negative scenarios
- Business-critical workflows
- Acceptance criteria validation

**Standard Pytest Focus Areas:**
- Edge cases
- Boundary testing
- Performance tests
- Security tests
- Data validation
- Technical scenarios

### 🟦 Final Remarks

1. This Project will include on future updates as a release version:
- Mobile Automation
- API Automation
- CI/CD flow (Jenkins/GitHub Actions)
- Unit Tests modules
- More test modules

2. It is also going to include negative test cases for error handling and edge cases. 

3. It is going to include a more complete test coverage for the application.


## Contributing

This is an educational framework. Feel free to:
- Fork and experiment
- Suggest improvements
- Report issues
- Share with others learning QA automation


----
----


# 🟩 Proyecto Automation-Framework-QA

**Versión en Español** 🟩
>Este es un Demo Project para crear un  `Framework de Automatización`, base y simple, para un sitio web UI (Magento) y como un proyecto educativo, no como un código listo para producción.

Este es un proyecto de `Automation Testing Framework` desarrollado con **Python, Pytest y Selenium WebDriver**, diseñado para asegurar la escalabilidad, mantenibilidad y claridad estructural a través de la aplicación de los principios SOLID y las mejores prácticas de ingeniería de software.

Este código es recomendado para principiantes para entender los conceptos básicos de un Framework de Automatización utilizando Python, Selenium WebDriver, Pytest, Faker, Allure Reports, y no es un código listo para producción.
El nombre `C-QA` se mantiene como una consecución del sitio web educativo [Compilidor QA](https://www.compiladorqa.tech/), desarrollado para contribuir a la comunidad QA y ayudar a los profesionales de QA a aprender y entender los conceptos básicos de tecnología, por eso se decidió usar `C-QA` como un nombre corto para este proyecto de Framework de Automatización, alegorico al sitio web mencionado antes.


## Importante ⚠️

🟩 Le recomiendo que: 
- Intente entender el código y la estructura del framework, la lógica del programa y los fundamentos de la automatización utilizando Selenium WebDriver, Pytest y Python
- No solo copie y pegue el código, porque eso no es el punto de este proyecto, el punto es entender el código y la estructura del framework.
- Una vez que comprenda el código y la estructura del framework, podrá crear su propio framework, y podrá automatizar su propio sitio web UI.
- Además, puede agregar nuevas características al framework, como automatización móvil, automatización de API, flujo CI/CD (Jenkins/GitHub Actions), pruebas unitarias, etc.
- También puede incluir más módulos de pruebas, y más casos de pruebas y las bibliotecas necesarias para que funcione.

## 🟩 Alcance
El alcance específico de este proyecto es la práctica de Automation UI para explicar Selenium Webdriver y Pytest utilizando un sitio web de comercio electrónico simple.
**No incluido**
- Automatización móvil
- Automatización de API
- Flujo CI/CD (Jenkins/GitHub Actions)

Como una práctica recomendada, se recomienda considerar estos temas para un framework de automatización real e integral.

## 🟩 Objetivos

- Automatizar flujos críticos de un sitio web de comercio electrónico Magento, validando funcionalidades como inicio de sesión, registro de usuario, búsqueda, carrito de compras y checkout, de manera confiable y reutilizable.
- Crear un simple framework de automatización para un sitio web UI (Magento) y como un proyecto educativo.
- Entender los conceptos básicos de un Framework de Automatización utilizando Python, Selenium WebDriver, Pytest, Faker, Allure Reports, y no es un código listo para producción.


## 🟩 Tecnologías utilizadas

- **Python 3.12+**
- **Selenium WebDriver**
- **Pytest**
- **Faker** (for dynamic data)
- **Allure Reports**
- **dotenv** (secure configuration management)
- **Jenkins** (for CI/CD)

## 🟩 Principios de diseño SOLID 

- **S: Single Responsibility - Responsabilidad Unica**  
- **O: Open/Closed - Abierto/Cerrado**  
- **L: Liskov Substitution - Sustitución de Liskov**  
- **I: Interface Segregation - Segregación de Interfaces**  
- **D: Dependency Inversion - Inversión de Dependencias**  

## 🟩 Estructura del proyecto

```
Automation-Framework-QA/
├── docs/                    # Documentación (¡estás aquí!)
├── driver/                  # Drivers de navegador opcionales
├── pages/                   # Clases de Objeto de Página
├── api/                     # Clases de Objeto de API para automatización de test de API
├── ci_cd/                   # Contiene la logica para automatizar la ejecucion de test en un ciclo de intregracion y deployment, utiliza la herramienta Jenkins para diferentes jobs (api, staging, smoke, ui), que son usados para ejecutar los tests en distintos entornos
├── features/                # Archivos feature para ejecutar tests utilizando la metodologia BDD (Behavior-Driven Development)
├── tests/                   # Modulos de test cases agrupados por suites de pruebas, donde cada una contiene una estrategia de pruebas como smoke, regression, api, e2e, etc
├── tools/                   # Pruebas unitarias para objetos de página
|
├── utils/                   # Utilidades (config, data, browser, assertions, api_helpers para validacion de API)
├── .env                     # Variables de entorno (no en el repo)
├── conftest.py              # Fixtures globales de Pytest
├── pytest.ini               # Configuración de Pytest
└── requiriments.txt         # Dependencias de Python

```

Estrategia de Pruebas en Capas

Este framework soporta **tres capas** de pruebas, todas reutilizando la misma lógica central:


```
┌─────────────────────────────────────────────┐
│   Pruebas BDD (Aceptación)                  │
│   features/ + tests/bdd_steps_definitions/  │
│   Propósito: Validación de comportamiento   │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────┴───────────────────────────┐
│   Pruebas de Integración (Funcional)        │
│   tests/api_test/ + tests/smoke_tests/      │
│   tests/regression_tests/, etc              │
│   Propósito: Validación funcional detallada │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────┴───────────────────────────┐
│   Pruebas Unitarias (Componente)            │
│   tools/src_unit/                           │
│   Propósito: Probar POMs y clientes API     │
└─────────────────────────────────────────────┘

```

**Las tres capas reutilizan:**
- `pages/` (Page Objects)
- `api/` (Clientes API)
- `utils/` (Helpers y utilidades)

---

## 📄 Procedimiento de Testing 

## 🟩 Prerequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

### Software requerido
- **Python 3.12+** - [Descargar Python](https://www.python.org/downloads/)
- **Git** - [Descargar Git](https://git-scm.com/downloads)
- **Google Chrome o Firefox** - Latest version
- **Pip** - [Download Pip](https://pip.pypa.io/en/stable/installation/)


#### 1️⃣ Clonar el repositorio, descargar el archivo zip, o bifurcar (fork) el repositorio.

```
git clone https://github.com/LetyPG/Automation-Framework-QA.git

```

>Después de clonar el repositorio en el directorio que desees, puedes ejecutar los tests dentro de él, en este caso se usa el directorio `Automation-Framework-QA`.

#### 2️⃣ Navigate to the project directory

```
cd Automation-Framework-QA
```

#### 3️⃣ Configurar un entorno virtual de Python (Recomendado)

Utiliza un entorno virtual para aislar las dependencias del proyecto de tu sistema Python, esto es una buena práctica para mantener el entorno de desarrollo limpio y ordenado y evitar conflictos con otras dependencias de tu sistema, por ejemplo, en caso de que tengas instalado una versión diferente de Python en tu sistema y el framework requiera una versión diferente, el entorno virtual te permitirá mantener ambas versiones sin conflictos.
Ejecutando los siguientes comandos en la terminal, puedes crear y activar un entorno virtual, ambos utilizan la herramienta `venv` que viene por defecto con Python.

#### En Linux/macOS:

- Crear un entorno virtual

```
python3 -m venv venv

```

- Activar el entorno virtual

```
source venv/bin/activate

```

#### En Windows:

- Crear un entorno virtual

```
python -m venv venv

```

- Activar el entorno virtual

```
venv\Scripts\activate
```

- Deberías ver `(venv)` en tu terminal prompt cuando esté activado.

#### 4️⃣ Instalación de dependencias

- Para ejecutar los tests Selenium-based general tests:

```
pip install -r requiriments.txt

```
  
> Nota: el nombre del archivo es `requiriments.txt` en este repositorio, por convención. 

- Para ejecutar solo los tests unitarios (tools/), no se requieren dependencias adicionales porque la suite stubs Selenium y dotenv.

#### 5️⃣ Crear un archivo .env y adaptarlo

- Crear un archivo .env y adaptarlo a tus necesidades, este es un framework explicativo, por lo que puedes adaptarlo a tus necesidades.



#### 6️⃣ Ejecutar los tests

Teniendo en cuenta que ya te encuentras en el directorio raíz del proyecto, puedes ejecutar los tests desde ahí, sin necesidad de moverte a ningún otro directorio, usando los siguientes comandos:

##### Directorio raíz del proyecto `tests/`

- Tests generales Selenium-based :
>Nota: Si se decide ejecutar todos los test que existan en este framework, es importante tener en cuenta que el framework puede tardar mucho tiempo en ejecutarse, por lo que se recomienda ejecutar solo los test que se requieran, además que consumiria mucha memoria y tiempo de ejecución, lo que no es recomendable para el perfformance de un framework en producción.

```
pytest`  (or `pytest -v`)

```

- Ejecutar todos los tests en un directorio específico `<tests/test_directory_name>`: 

```
pytest tests/ui_tests -v

```

- Ejecutar un archivo de test específico `<tests/test_directory_name/test_file_name.py>`:

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


##### Directorio raíz del proyecto `tools/src_unit/` para tests unitarios

- Tests unitarios :

```
pytest tools/src_unit -v
```
- Para ejecutar un archivo de test específico `<tools/test_unit_directory_name/unit_test_file_name.py>`:

```
pytest tools/src_unit/test_login_unit.py -v
```

#### Directorio del proyecto `api/` para tests de API

- Tests de API :

```
pytest tests/api_test/ -v
```

- Ejecutar una suite de tests de API específica `<tests/api_test/test_directory_name/test_file_name.py>`:

```
pytest tests/api_test/test_user/ -v
```

- Ejecutar un archivo de test de API específico, que se encuentra dentrop de  una suite de tests `<tests/api_test/test_directory_name/test_file_name.py>`:

```
pytest tests/api_test/test_user/test_user_service.py
 -v
```

- Ejecutar tests por marker (solo si los tests están marcados de manera correspondiente):
```
pytest -m api -v
```

##### Directorio del proyecto `features/` para tests de BDD

- Run All BDD Tests
```bash
pytest features/ -v
```

- Run Specific Feature
```bash
pytest features/api/user_service.feature -v
pytest features/ui/login.feature -v
```

- Run by Tags
```bash
# Smoke tests only
pytest features/ -m smoke

# API tests only
pytest features/ -m api

# Critical scenarios
pytest features/ -m critical

# Negative scenarios
pytest features/ -m negative
```

- Generate BDD Reports
```bash
# HTML report
pytest features/ --html=reports/bdd_report.html

```

>Nota: `-m` filtra por nombre de marker, no por nombre de archivo de test. Para ejecutar un archivo específico, pasa la ruta del archivo; para coincidir con nombres de test, usa `-k`.

>Nota: Puedes ejecutar tests usando `-v` para salida detallada o `-q` para salida silenciosa, eso depende de tus necesidades de información.

#### 7️⃣ Allure reports (opcional)

Allure no está forzado via [pytest.ini](cci:7://file:///home/user/GuideProject/Automation-Framework-QA/pytest.ini:0:0-0:0) para mantener la configuración flexible. Cuando quieras generar un reporte de Allure, pasa el argumento via CLI:

- Para ejecuciones generales de **tests**- `tests/`:

```
pytest tests --alluredir=reports/allure-results
```

- Para ejecuciones de tests específicos `<tests/test_directory_name/test_file_name.py>`:

```
pytest tests/ui_tests/test_account_user.py --alluredir=reports/allure-results
```

- Para ejecuciones generales de **tests unitarios** -`tools/`:

```
pytest tools --alluredir=reports/allure-results

```

- Para ejecuciones generales de **tests de API** -`tests/api_test/`:

```
pytest tests/api_test/ -v
```

```
pytest tests/api_test/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

- Ejecutar tests en paralelo:
```
pytest tests/api_test/ -n 4
```

- Con cubrimiento de código:
```
pytest tests/api_test/ --cov=api --cov-report=html
```

```
pytest tests/api_test/ --alluredir=reports/allure-results

```
- Para ejecuciones generales de **tests de BDD** -`features/`:
```
pytest features/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Recommended Testing Distribution

For a balanced QA framework:

| Test Type | % of Tests | Purpose |
|-----------|-----------|---------|
| **BDD (Acceptance)** | 15-20% | Critical user flows, acceptance criteria |
| **Integration/Functional** | 60-70% | Detailed API/UI testing, edge cases |
| **Unit Tests** | 10-15% | Test framework components (POMs, utils) |
| **E2E** | 5-10% | Full system integration |

**BDD Focus Areas:**
- Critical happy paths
- Key negative scenarios
- Business-critical workflows
- Acceptance criteria validation

**Standard Pytest Focus Areas:**
- Edge cases
- Boundary testing
- Performance tests
- Security tests
- Data validation
- Technical scenarios


## 🟩 Notas Finales

1. Este proyecto incluirá en futuras actualizaciones como una versión de lanzamiento:
- Automatización de dispositivos móviles
- Automatización de API
- CI/CD flow (Jenkins/GitHub Actions)
- Otra versión de lanzamiento de Módulos de pruebas unitarias
- Módulos de pruebas adicionales

2. También incluirá en futuras actualizaciones pruebas negativas para manejo de errores y casos de borde. 

3. También incluirá en futuras actualizaciones una cobertura de pruebas más completa para la aplicación.



## Contribución

Este es un framework educativo. ¡Siéntase libre de:
- Hacer Fork y experimentar
- Sugerir mejoras
- Reportar problemas
- Compartir con otros aprendiendo QA automation



---

**Version**: 0.1.2  
**Last Updated**: 2025  
**Language**: English | [Español](../spanish/index.md)

