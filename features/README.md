>English Version: At the Top of this file you are going to see the English version indicated by this sy  mbol 🟦, and below you are going to see the Spanish version indicated by this symbol 🟩, you can choose the one you want to use.

>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.  

#  🟦 BDD Features Directory

## What is BDD (Behavior-Driven Development)?

**Behavior-Driven Development (BDD)** is a software development approach that extends Test-Driven Development (TDD) by writing test cases in natural language that non-programmers can read. BDD focuses on the **behavior** of the application from the user's perspective.

### Key Components:

1. **Gherkin Language**: Human-readable syntax using Given-When-Then
2. **Feature Files**: `.feature` files containing scenarios in plain English
3. **Step Definitions**: Python code that implements each Gherkin step
4. **Living Documentation**: Tests that serve as up-to-date documentation
5. **Extra QA Best Practices**: Using BDD is another layer of quality assurance, it helps to bridge the gap between QA and Development, and also keeps the bussiness close to real user scenarios and real user workflows, in this way it can be validate the real user experience and the real user journey.

---

## Why BDD is Important for QA Frameworks

### 1. Bridges Communication Gap
BDD enables collaboration between:
- QA Engineers
- Developers
- Business Analysts
- Product Owners
- Non-Technical Stakeholders

Everyone can read, understand, and contribute to test scenarios.

### 2. Living Documentation
Your `.feature` files are **executable documentation**:
- Always up-to-date (if it passes, the feature works)
- Self-documenting test coverage
- Easy to review what's being tested
- Business requirements in executable form

### 3. Clarity of Intent
Compare these approaches:

**Traditional Test:**
```python
def test_login_invalid_password():
    # What is being tested? Why?
    assert login("user", "wrong") == False
```

**BDD Test:**
```gherkin
Scenario: Login with invalid password shows error message
  Given I am on the login page
  When I enter username "user" and password "wrong"
  Then I should see error message "Invalid credentials"
  And I should remain on the login page
```

**Winner:** BDD clearly states the **context**, **action**, and **expected outcome**.

### 4. Requirement Traceability
Each scenario directly maps to business requirements:
- Easy to track which requirements are tested
- Product Owners can review test coverage
- Compliance and audit trails

### 5. Promotes Test Design Thinking
Writing scenarios in Gherkin forces you to:
- Think about user behavior
- Identify edge cases
- Focus on business value
- Avoid implementation details

---

## How BDD Integrates with This Framework

### Two-Layer Architecture

```
┌─────────────────────────────────────────────┐
│         BDD Layer (Story Layer)             │
│  features/*.feature + step_definitions/     │
│  "WHAT to test" - Business readable         │
└─────────────────┬───────────────────────────┘
                  │ Calls
                  ▼
┌─────────────────────────────────────────────┐
│       Engine Layer (Implementation)         │
│     pages/ (POM) + api/ (API Clients)       │
│  "HOW to test" - Technical implementation   │
└─────────────────────────────────────────────┘
```

### Integration Example:

**1. Gherkin (.feature file):**
```gherkin
When I enter "user@example.com" and "password123"
```

**2. Step Definition (step_defs/):**
```python
@when(parsers.parse('I enter "{username}" and "{password}"'))
def enter_credentials(username, password, login_page):
    login_page.perform_login(username, password)  # Calls Engine
```

**3. Engine (pages/):**
```python
def perform_login(self, username, password):
    self.actions.input_text(self.EMAIL_INPUT, username)
    self.actions.input_text(self.PASSWORD_INPUT, password)
    self.actions.click(self.LOGIN_BUTTON)
```

**Key Principle:** Step definitions are **glue code** with NO complex logic. All logic stays in the engine layer (pages/, api/).

---

## Framework Structure

```
|__features/
|   ├── README.md                    # This file
|   ├── api/                         # API BDD scenarios
|   |   ├── user_service.feature     # User API tests
|   |   ├── product_service.feature  # Product API tests
|   |   └── order_patyment.feature   # Payment API tests
|   └── ui/                          # UI BDD scenarios
|       ├── login.feature            # Login tests
|       ├── account.feature          # Account management tests
|       └── search_product.feature   # Product search tests

|__tests/
|   ├── bdd_steps_definitions/             # Step implementation
|       ├── conftest.py                  # BDD fixtures (scenario_context)
|       ├── test_api_user_steps_definition.py
|       └── test_ui_login_steps_definitions.py
|
|__tools/
|   |__ README.md                   # Extra tools for API and UI tests used for BDD practice
|   ├── api_helpers/                   # API client implementation
|   |        ├── user_schema.json             # Contains the schema for the user API response to validate the response across the API tests
|   └── __init__.py                    
|   └── schema_validator.py               # API utils implementation, contains the module logics that provides JSON schema validation capabilities for API responses.
|                                        # It supports BDD testing scenarios and follows the framework's architecture patterns.
```

---

## When to Use BDD

### Good Use Cases for BDD:

| Scenario | Why BDD? |
|----------|----------|
| **User workflows** | Describes user journey clearly |
| **Acceptance criteria** | Direct mapping to business requirements |
| **Critical business flows** | Stakeholder-readable validation |
| **E2E scenarios** | Natural description of end-to-end behavior |
| **Happy paths** | Primary user scenarios |
| **Critical negative paths** | Important error scenarios |

### Examples of Good BDD Scenarios:

**User Login**
```gherkin
Scenario: Successful login with valid credentials
  Given I am on the login page
  When I enter valid username and password
  Then I should be redirected to the dashboard
```

**E-commerce Purchase**
```gherkin
Scenario: Guest user completes purchase
  Given I am a guest user
  When I add a product to cart
  And I proceed to checkout
  And I enter shipping details
  And I complete payment
  Then I should receive an order confirmation
```

**API Contract Validation**
```gherkin
Scenario: API returns valid user data
  Given the user service is available
  When I request user with ID "2"
  Then the response status code should be 200
  And the response schema should be valid
```

---

## When NOT to Use BDD

### Poor Use Cases for BDD:

| Scenario | Why NOT BDD? | Use Instead |
|----------|--------------|-------------|
| **Unit tests** | Too granular | Pytest in `tools/` |
| **Technical edge cases** | Not business-facing | Pytest in `tests/api/` or `tests/ui/` |
| **Performance tests** | Technical metrics | Pytest with performance markers |
| **UI element validation** | Implementation details | Standard pytest tests |
| **Multiple field combinations** | Too many permutations | Parameterized pytest |

### Examples of Poor BDD Scenarios:

**Too Technical:**
```gherkin
Scenario: Verify CSS selector returns element
  Given the DOM is loaded
  When I query ".login-button"
  Then the element should have class "btn-primary"
```
**Better:** Regular pytest test

**Too Granular:**
```gherkin
Scenario: Password field accepts 8 characters
Scenario: Password field accepts 9 characters
Scenario: Password field accepts 10 characters
...
```
**Better:** Parameterized pytest with `@pytest.mark.parametrize`

**Implementation-Focused:**
```gherkin
Scenario: Verify HTTP response time under 2 seconds
  Given the API endpoint is "/users"
  When I measure the response time
  Then it should be less than 2000 milliseconds
```
**Better:** Pytest with performance assertions

---

## Scalability of BDD in This Framework

### 1. Step Reusability

Write once, use everywhere:

```gherkin
# Used in login.feature
Given I am on the login page

# Reused in account.feature
Given I am on the login page
And I login with valid credentials

# Reused in checkout.feature
Given I am on the login page
And I complete login
```

**Benefit:** One step definition, used in 50+ scenarios.

### 2. Centralized Logic (Maintainability)

**Scenario:** Login page changes - adds a "Remember Me" checkbox that's now mandatory.

**Without BDD approach:**
- Update 50+ test files manually
- Risk missing some tests
- Time-consuming and error-prone

**With BDD + POM approach:**
- Update **one** method: `login_page.perform_login()`
- All 50+ scenarios automatically fixed
- Fast and reliable

### 3. Parallel Execution

BDD scenarios can run in parallel:

```bash
# Run all BDD tests in parallel
pytest features/ -n 4

# Run specific tags in parallel
pytest -m "smoke" -n auto
pytest -m "api and critical" -n 4
```

### 4. Tag-Based Organization

Organize and filter tests using tags:

```gherkin
@smoke @api @user_service
Scenario: Retrieve user data

@critical @ui @payment
Scenario: Complete payment successfully

@negative @security
Scenario: Reject unauthorized access
```

**Run by tags:**
```bash
# Smoke tests only
pytest -m smoke

# API tests only
pytest -m api

# Critical scenarios
pytest -m critical

# Negative scenarios
pytest -m negative
```

### 5. Layered Testing Strategy

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
│   tests/api_test/ + tests/smoke_tests/      │
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

### 6. Growing the Test Suite

Adding new tests is scalable:

**Step 1:** Create `.feature` file
```gherkin
Feature: New Shopping Cart Feature
  Scenario: Add item to cart
    Given I am on the product page
    When I click "Add to Cart"
    Then the item should be in my cart
```

**Step 2:** Write step definitions (or reuse existing)
```python
@when('I click "Add to Cart"')
def click_add_to_cart(product_page):
    product_page.add_to_cart()  # Reuses existing POM
```

**Step 3:** Run the test
```bash
pytest features/ui/login.feature
```

**Scalable because:**
- Reuses existing POMs
- Reuses existing steps
- No duplicate code
- Easy to add, easy to maintain

---
---

## Running BDD Tests

**The Core Concept:**
In BDD with pytest-bdd, the 
.feature
 files ARE the tests, not the step definition files.

 ```
features/user_service.feature  ← This is the TEST (executable scenarios)
         │
         │ calls
         ▼
tests/bdd_steps_definitions/   ← This is the IMPLEMENTATION (glue code)

```
**How pytest-bdd Discovers Tests:**
Feature files define test cases: Each Scenario in a 
.feature
 file becomes a pytest test
Step definitions provide implementation: The Python code in tests/bdd_steps_definitions/ is glue code that gets called

**Execution Flow:**
When you run pytest features/user_service.feature:

```
1. pytest-bdd reads the .feature file
   └─> Finds: Scenario: Retrieve a specific user

2. For each Gherkin step, it looks for matching step definitions:
   └─> "Given the user service is available"
       → Searches for @given decorator with this text
       → Finds it in tests/bdd_steps_definitions/test_api_user_steps_definition.py
       → Executes the Python function
```

3. Reports pass/fail based on all steps in the scenario

### Run All BDD Tests
```bash
pytest features/ -v
```

### Run Specific Feature
```bash
pytest features/api/user_service.feature -v
pytest features/ui/login.feature -v
```

### Run by Tags
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

---

## BDD Best Practices

### 1. Write Declarative Steps (Not Imperative)

**Imperative (Too detailed):**
```gherkin
Given I navigate to "https://example.com/login"
When I type "user@example.com" in the field with id "email"
And I type "password123" in the field with id "password"
And I click the button with class "login-btn"
```

**Declarative (Focus on behavior):**
```gherkin
Given I am on the login page
When I login with valid credentials
Then I should be logged in
```

### 2. Scenarios Should Be Independent

Each scenario should:
- Set up its own preconditions
- Not depend on other scenarios
- Be runnable in any order
- Clean up after itself (use fixtures)

### 3. Use Background for Common Steps

```gherkin
Feature: Account Management

  Background:
    Given I am logged into my account
    And I am on the account page
  
  Scenario: Update email
    When I change my email to "new@example.com"
    Then my email should be updated
  
  Scenario: Update password
    When I change my password
    Then my password should be updated
```

### 4. Use Scenario Outline for Data Variations

```gherkin
Scenario Outline: Search for different products
  Given I am on the homepage
  When I search for "<product>"
  Then I should see results for "<product>"
  
  Examples:
    | product    |
    | shoes      |
    | shirts     |
    | jackets    |
```

### 5. Keep Scenarios Short and Focused

**Too long:**
```gherkin
Scenario: Complete entire shopping flow
  Given I register a new account
  When I search for products
  And I add 5 products to cart
  And I apply coupon
  And I checkout
  And I enter shipping
  And I enter billing
  And I complete payment
  ...
```

**Focused:**
```gherkin
Scenario: Add product to cart
  Given I am on a product page
  When I add the product to cart
  Then the product should be in my cart
```

---

## Learning Resources

- **Cucumber/Gherkin:** https://cucumber.io/docs/gherkin/
- **pytest-bdd Documentation:** https://pytest-bdd.readthedocs.io/
- **BDD Best Practices:** https://cucumber.io/docs/bdd/
- **Writing Good Gherkin:** https://cucumber.io/docs/gherkin/reference/

---

## Summary

### BDD in This Framework:

**Enables collaboration** between technical and non-technical team members  
**Provides living documentation** that's always up-to-date  
**Scales efficiently** through step reusability and centralized logic  
**Complements** traditional pytest tests (doesn't replace them)  
**Focuses on business behavior** rather than implementation details  
**Integrates seamlessly** with existing POMs and API clients  
**Supports parallel execution** and tag-based filtering  

### When to Use BDD:
- Critical user workflows
- Acceptance criteria
- Business-facing scenarios
- E2E validation

### When NOT to Use BDD:
- Unit tests
- Technical edge cases
- Performance tests
- Implementation details

---

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework 

----

# 🟩 Directorio de Features BDD

## ¿Qué es BDD (Desarrollo Dirigido por Comportamiento)?

**Behavior-Driven Development (BDD)** es un enfoque de desarrollo de software que extiende el Desarrollo Dirigido por Pruebas (TDD) escribiendo casos de prueba en lenguaje natural que los no programadores pueden leer. BDD se enfoca en el **comportamiento** de la aplicación desde la perspectiva del usuario.

### Componentes Clave:

1. **Lenguaje Gherkin**: Sintaxis legible por humanos usando Given-When-Then
2. **Archivos Feature**: Archivos `.feature` que contienen escenarios en lenguaje natural
3. **Definiciones de Pasos**: Código Python que implementa cada paso de Gherkin
4. **Documentación Viva**: Pruebas que sirven como documentación actualizada
5. **Mejores Prácticas Extra de QA**: Usar BDD es otra capa de aseguramiento de calidad, ayuda a cerrar la brecha entre QA y Desarrollo, y también mantiene al negocio cerca de escenarios y flujos de trabajo de usuarios reales, de esta manera se puede validar la experiencia real del usuario y el recorrido real del usuario.

---

## Por qué BDD es Importante para Frameworks QA

### 1. Cierra la Brecha de Comunicación
BDD habilita la colaboración entre:
- Ingenieros QA
- Desarrolladores
- Analistas de Negocio
- Product Owners
- Stakeholders No Técnicos

Todos pueden leer, entender y contribuir a los escenarios de prueba.

### 2. Documentación Viva
Tus archivos `.feature` son **documentación ejecutable**:
- Siempre actualizada (si pasa, la funcionalidad funciona)
- Cobertura de pruebas auto-documentada
- Fácil de revisar qué se está probando
- Requisitos de negocio en forma ejecutable

### 3. Claridad de Intención
Compara estos enfoques:

**Prueba Tradicional:**
```python
def test_login_invalid_password():
    # ¿Qué se está probando? ¿Por qué?
    assert login("user", "wrong") == False
```

**Prueba BDD:**
```gherkin
Scenario: Login con contraseña inválida muestra mensaje de error
  Given Estoy en la página de login
  When Ingreso username "user" y contraseña "wrong"
  Then Debería ver mensaje de error "Credenciales inválidas"
  And Debería permanecer en la página de login
```

**Ganador:** BDD claramente establece el **contexto**, **acción**, y **resultado esperado**.

### 4. Trazabilidad de Requisitos
Cada escenario mapea directamente a requisitos de negocio:
- Fácil rastrear qué requisitos están probados
- Product Owners pueden revisar cobertura de pruebas
- Cumplimiento y pistas de auditoría

### 5. Promueve Pensamiento de Diseño de Pruebas
Escribir escenarios en Gherkin te fuerza a:
- Pensar sobre el comportamiento del usuario
- Identificar casos extremos
- Enfocarte en valor de negocio
- Evitar detalles de implementación

---

## Cómo BDD se Integra con Este Framework

### Arquitectura de Dos Capas

```
┌─────────────────────────────────────────────┐
│         Capa BDD (Capa de Historia)         │
│  features/*.feature + step_definitions/     │
│  "QUÉ probar" - Legible por negocio         │
└─────────────────┬───────────────────────────┘
                  │ Llama
                  ▼
┌─────────────────────────────────────────────┐
│       Capa Motor (Implementación)           │
│     pages/ (POM) + api/ (Clientes API)      │
│  "CÓMO probar" - Implementación técnica     │
└─────────────────────────────────────────────┘
```

### Ejemplo de Integración:

**1. Gherkin (archivo .feature):**
```gherkin
When Ingreso "user@example.com" y "password123"
```

**2. Definición de Paso (step_defs/):**
```python
@when(parsers.parse('Ingreso "{username}" y "{password}"'))
def enter_credentials(username, password, login_page):
    login_page.perform_login(username, password)  # Llama al Motor
```

**3. Motor (pages/):**
```python
def perform_login(self, username, password):
    self.actions.input_text(self.EMAIL_INPUT, username)
    self.actions.input_text(self.PASSWORD_INPUT, password)
    self.actions.click(self.LOGIN_BUTTON)
```

**Principio Clave:** Las definiciones de pasos son **código de pegamento** SIN lógica compleja. Toda la lógica permanece en la capa motor (pages/, api/).

---

## Estructura del Framework

```
|__features/
|   ├── README.md                    # Este archivo
|   ├── api/                         # Escenarios BDD de API
|   |   ├── user_service.feature     # Pruebas de API de usuario
|   |   ├── product_service.feature  # Pruebas de API de producto
|   |   └── order_patyment.feature   # Pruebas de API de pago
|   └── ui/                          # Escenarios BDD de UI
|       ├── login.feature            # Pruebas de login
|       ├── account.feature          # Pruebas de gestión de cuenta
|       └── search_product.feature   # Pruebas de búsqueda de producto

|__tests/
|   ├── bdd_steps_definitions/             # Implementación de pasos
|       ├── conftest.py                  # Fixtures BDD (scenario_context)
|       ├── test_api_user_steps_definition.py
|       └── test_ui_login_steps_definitions.py
|
|__tools/
|   |__ README.md                   # Herramientas extra para pruebas API y UI usadas para práctica BDD
|   ├── api_helpers/                   # Implementación de cliente API
|   |        ├── user_schema.json             # Contiene el esquema para la respuesta API de usuario para validar la respuesta en las pruebas API
|   └── __init__.py                    
|   └── schema_validator.py               # Implementación de utilidades API, contiene la lógica del módulo que proporciona capacidades de validación de esquema JSON para respuestas API.
|                                        # Soporta escenarios de prueba BDD y sigue los patrones de arquitectura del framework.
```

---

## Cuándo Usar BDD

### Buenos Casos de Uso para BDD:

| Escenario | ¿Por qué BDD? |
|----------|----------|
| **Flujos de trabajo de usuario** | Describe claramente el recorrido del usuario |
| **Criterios de aceptación** | Mapeo directo a requisitos de negocio |
| **Flujos de negocio críticos** | Validación legible por stakeholders |
| **Escenarios E2E** | Descripción natural del comportamiento end-to-end |
| **Caminos felices** | Escenarios de usuario primarios |
| **Caminos negativos críticos** | Escenarios de error importantes |

### Ejemplos de Buenos Escenarios BDD:

**Login de Usuario**
```gherkin
Scenario: Login exitoso con credenciales válidas
  Given Estoy en la página de login
  When Ingreso username y contraseña válidos
  Then Debería ser redirigido al dashboard
```

**Compra E-commerce**
```gherkin
Scenario: Usuario invitado completa compra
  Given Soy un usuario invitado
  When Agrego un producto al carrito
  And Procedo al checkout
  And Ingreso detalles de envío
  And Completo el pago
  Then Debería recibir una confirmación de orden
```

**Validación de Contrato API**
```gherkin
Scenario: API retorna datos de usuario válidos
  Given El servicio de usuario está disponible
  When Solicito usuario con ID "2"
  Then El código de estado de respuesta debería ser 200
  And El esquema de respuesta debería ser válido
```

---

## Cuándo NO Usar BDD

### Casos de Uso Pobres para BDD:

| Escenario | ¿Por qué NO BDD? | Usar en su lugar |
|----------|--------------|-------------|
| **Pruebas unitarias** | Demasiado granular | Pytest en `tools/` |
| **Casos extremos técnicos** | No orientado a negocio | Pytest en `tests/api/` o `tests/ui/` |
| **Pruebas de rendimiento** | Métricas técnicas | Pytest con marcadores de rendimiento |
| **Validación de elementos UI** | Detalles de implementación | Pruebas pytest estándar |
| **Combinaciones múltiples de campos** | Demasiadas permutaciones | Pytest parametrizado |

### Ejemplos de Escenarios BDD Pobres:

**Demasiado Técnico:**
```gherkin
Scenario: Verificar que selector CSS retorna elemento
  Given El DOM está cargado
  When Consulto ".login-button"
  Then El elemento debería tener clase "btn-primary"
```
**Mejor:** Prueba pytest regular

**Demasiado Granular:**
```gherkin
Scenario: Campo de contraseña acepta 8 caracteres
Scenario: Campo de contraseña acepta 9 caracteres
Scenario: Campo de contraseña acepta 10 caracteres
...
```
**Mejor:** Pytest parametrizado con `@pytest.mark.parametrize`

**Enfocado en Implementación:**
```gherkin
Scenario: Verificar tiempo de respuesta HTTP bajo 2 segundos
  Given El endpoint de API es "/users"
  When Mido el tiempo de respuesta
  Then Debería ser menor a 2000 milisegundos
```
**Mejor:** Pytest con aserciones de rendimiento

---

## Escalabilidad de BDD en Este Framework

### 1. Reutilización de Pasos

Escribe una vez, usa en todas partes:

```gherkin
# Usado en login.feature
Given Estoy en la página de login

# Reutilizado en account.feature
Given Estoy en la página de login
And Me logueo con credenciales válidas

# Reutilizado en checkout.feature
Given Estoy en la página de login
And Completo el login
```

**Beneficio:** Una definición de paso, usada en más de 50 escenarios.

### 2. Lógica Centralizada (Mantenibilidad)

**Escenario:** La página de login cambia - agrega un checkbox "Recordarme" que ahora es obligatorio.

**Sin enfoque BDD:**
- Actualizar más de 50 archivos de prueba manualmente
- Riesgo de omitir algunas pruebas
- Consume tiempo y es propenso a errores

**Con enfoque BDD + POM:**
- Actualizar **un** método: `login_page.perform_login()`
- Todos los más de 50 escenarios arreglados automáticamente
- Rápido y confiable

### 3. Ejecución Paralela

Los escenarios BDD pueden ejecutarse en paralelo:

```bash
# Ejecutar todas las pruebas BDD en paralelo
pytest features/ -n 4

# Ejecutar tags específicos en paralelo
pytest -m "smoke" -n auto
pytest -m "api and critical" -n 4
```

### 4. Organización Basada en Tags

Organizar y filtrar pruebas usando tags:

```gherkin
@smoke @api @user_service
Scenario: Recuperar datos de usuario

@critical @ui @payment
Scenario: Completar pago exitosamente

@negative @security
Scenario: Rechazar acceso no autorizado
```

**Ejecutar por tags:**
```bash
# Solo pruebas smoke
pytest -m smoke

# Solo pruebas API
pytest -m api

# Escenarios críticos
pytest -m critical

# Escenarios negativos
pytest -m negative
```

### 5. Estrategia de Pruebas en Capas

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

### 6. Crecimiento de la Suite de Pruebas

Agregar nuevas pruebas es escalable:

**Paso 1:** Crear archivo `.feature`
```gherkin
Feature: Nueva Funcionalidad de Carrito de Compras
  Scenario: Agregar ítem al carrito
    Given Estoy en la página de producto
    When Hago click en "Agregar al Carrito"
    Then El ítem debería estar en mi carrito
```

**Paso 2:** Escribir definiciones de pasos (o reutilizar existentes)
```python
@when('Hago click en "Agregar al Carrito"')
def click_add_to_cart(product_page):
    product_page.add_to_cart()  # Reutiliza POM existente
```

**Paso 3:** Ejecutar la prueba
```bash
pytest features/ui/login.feature
```

**Escalable porque:**
- Reutiliza POMs existentes
- Reutiliza pasos existentes
- Sin código duplicado
- Fácil de agregar, fácil de mantener

---
---

## Ejecutar Pruebas BDD

**El Concepto Central:**
En BDD con pytest-bdd, los archivos `.feature` SON las pruebas, no los archivos de definición de pasos.

 ```
features/user_service.feature  ← Esta es la PRUEBA (escenarios ejecutables)
         │
         │ llama
         ▼
tests/bdd_steps_definitions/   ← Esta es la IMPLEMENTACIÓN (código de pegamento)

```
**Cómo pytest-bdd Descubre Pruebas:**
Los archivos feature definen casos de prueba: Cada Scenario en un archivo `.feature` se convierte en una prueba pytest
Las definiciones de pasos proporcionan implementación: El código Python en tests/bdd_steps_definitions/ es código de pegamento que se llama

**Flujo de Ejecución:**
Cuando ejecutas pytest features/user_service.feature:

```
1. pytest-bdd lee el archivo .feature
   └─> Encuentra: Scenario: Recuperar un usuario específico

2. Para cada paso Gherkin, busca definiciones de pasos coincidentes:
   └─> "Given el servicio de usuario está disponible"
       → Busca decorador @given con este texto
       → Lo encuentra en tests/bdd_steps_definitions/test_api_user_steps_definition.py
       → Ejecuta la función Python
```

3. Reporta pass/fail basado en todos los pasos del escenario

### Ejecutar Todas las Pruebas BDD
```bash
pytest features/ -v
```

### Ejecutar Feature Específico
```bash
pytest features/api/user_service.feature -v
pytest features/ui/login.feature -v
```

### Ejecutar por Tags
```bash
# Solo pruebas smoke
pytest features/ -m smoke

# Solo pruebas API
pytest features/ -m api

# Escenarios críticos
pytest features/ -m critical

# Escenarios negativos
pytest features/ -m negative
```

### Generar Reportes BDD
```bash
# Reporte HTML
pytest features/ --html=reports/bdd_report.html

# Reporte Allure
pytest features/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## Mejores Prácticas BDD

### 1. Escribir Pasos Declarativos (No Imperativos)

**Imperativo (Demasiado detallado):**
```gherkin
Given Navego a "https://example.com/login"
When Escribo "user@example.com" en el campo con id "email"
And Escribo "password123" en el campo con id "password"
And Hago click en el botón con clase "login-btn"
```

**Declarativo (Enfoque en comportamiento):**
```gherkin
Given Estoy en la página de login
When Me logueo con credenciales válidas
Then Debería estar logueado
```

### 2. Los Escenarios Deberían Ser Independientes

Cada escenario debería:
- Configurar sus propias precondiciones
- No depender de otros escenarios
- Ser ejecutable en cualquier orden
- Limpiarse después de sí mismo (usar fixtures)

### 3. Usar Background para Pasos Comunes

```gherkin
Feature: Gestión de Cuenta

  Background:
    Given Estoy logueado en mi cuenta
    And Estoy en la página de cuenta
  
  Scenario: Actualizar email
    When Cambio mi email a "new@example.com"
    Then Mi email debería estar actualizado
  
  Scenario: Actualizar contraseña
    When Cambio mi contraseña
    Then Mi contraseña debería estar actualizada
```

### 4. Usar Scenario Outline para Variaciones de Datos

```gherkin
Scenario Outline: Buscar diferentes productos
  Given Estoy en la página de inicio
  When Busco "<producto>"
  Then Debería ver resultados para "<producto>"
  
  Examples:
    | producto   |
    | zapatos    |
    | camisas    |
    | chaquetas  |
```

### 5. Mantener Escenarios Cortos y Enfocados

**Demasiado largo:**
```gherkin
Scenario: Completar flujo completo de compras
  Given Registro una nueva cuenta
  When Busco productos
  And Agrego 5 productos al carrito
  And Aplico cupón
  And Hago checkout
  And Ingreso envío
  And Ingreso facturación
  And Completo pago
  ...
```

**Enfocado:**
```gherkin
Scenario: Agregar producto al carrito
  Given Estoy en una página de producto
  When Agrego el producto al carrito
  Then El producto debería estar en mi carrito
```

---

## Recursos de Aprendizaje

- **Cucumber/Gherkin:** https://cucumber.io/docs/gherkin/
- **Documentación pytest-bdd:** https://pytest-bdd.readthedocs.io/
- **Mejores Prácticas BDD:** https://cucumber.io/docs/bdd/
- **Escribir Buen Gherkin:** https://cucumber.io/docs/gherkin/reference/

---

## Resumen

### BDD en Este Framework:

**Habilita colaboración** entre miembros técnicos y no técnicos del equipo  
**Proporciona documentación viva** que está siempre actualizada  
**Escala eficientemente** a través de reutilización de pasos y lógica centralizada  
**Complementa** pruebas pytest tradicionales (no las reemplaza)  
**Se enfoca en comportamiento de negocio** en lugar de detalles de implementación  
**Se integra perfectamente** con POMs y clientes API existentes  
**Soporta ejecución paralela** y filtrado basado en tags  

### Cuándo Usar BDD:
- Flujos de trabajo críticos de usuario
- Criterios de aceptación
- Escenarios orientados a negocio
- Validación E2E

### Cuándo NO Usar BDD:
- Pruebas unitarias
- Casos extremos técnicos
- Pruebas de rendimiento
- Detalles de implementación

---

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework
