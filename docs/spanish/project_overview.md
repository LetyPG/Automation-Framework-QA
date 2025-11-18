
## Estructura del Directorio del Proyecto

```
Automation-Framework-QA/
│
├── docs/                    # Documentación del framework en formato markdown y incluye documentación en inglés y español
├── drivers/                 # Drivers para diferentes navegadores
├── pages/                   # Clase por página (modelo POM)
├── tests/                   # Modulos de test cases
├── utils/                   # Configuración, logs, datos y helpers
├── tools/                   # Pruebas unitarias para objetos de página
├── .env                     # Variables de entorno y selectores externos
├── conftest.py              # Pytest fixtures globales
├── requirements.txt         # Dependencias del entorno
└── README.md                # Framework documentation

```
----

## Amplified Structure Details

Todos los directorios que se crearon para este framework se basan en los principios SOLID. Así que el objetivo era hacer el framework fácil de mantener y escalar. 
De aquí se estructuraron los directorios como sigue (Puedes ver las iniciales `L, S, O, I, D` como el inicio de la explicación del directorio)

### 1. Principio `L` 

```
│
├── drivers/

```

<details>
<summary>Directorio `drivers/` <br>- Principio  de Sustitución de Liskov (soporte para diferentes navegadores)</summary>


```
├── drivers/                      
│   └── chromedriver.exe           #El código puede ser utilizado en diferentes implementaciones del driver (Webdriver) en diferentes navegadores 
│                                  (Chrome, Firefox, Zafari) sin romper los tests.
│                                  #Si una clase hija (LoginPage) extiende y usa la clase padre (Basepage),entonces no modifica el flujo de los tests.


```

</details>


----

### 2. Principio `S` 


```
│
├── pages/

```


<details><summary>Directorio `pages/` <br>-  Principio de Responsabilidad Unica (cada clase modela una sola página) <br>- Principio de Segregación de Interfaces (cada clase consume solo los métodos necesarios de cada clase)</summary>


- Cada clase representa una sola responsabilidad, utilizando el Page Object Model, representando una sola página del sitio.
- El primer Object "Page"  inicializando el modelo POM (Page Object Model)   
- Soporta el principio DRY (Don’t Repeat Yourself)   

- Cada clase Page modela una sola página web.
- Las páginas instanciadas son relativas como la forma en que el software maneja sus servicios, generalmente una página maneja un solo servicio para centralizar la lógica de la página y las solicitudes del usuario, para este alcance se consideraron separados estos servicios, también cada servicio corresponde con una URL única (como inicio de sesión, registro, búsqueda, carrito de compras, checkout, etc.)


```

├── pages/                        
│   ├── __init__.py
│   ├── base_page.py         # Definición de la clase base (BasePage), con métodos reutilizables para encapsular la lógica de interacción, con el navegador y los elementos (click, write, wait)
│   ├──                      # Son creados instanciados al driver, donde los métodos generales de la clase base son heredados (herencia) 
│   ├──                      # Son creados nuevas clase para cada interface, con métodos específicos de cada interface se agregan, por lo que se crea un nuevo Object Page para cada interface
│   ├── login_page.py               # Login (LoginPage)
│   ├── page_form_submission.py     # Formulario de autenticación o registro (SubmissionForm)
│   ├── page_account_user.py        # Cuenta de usuario (UserAccount)
|
|   # Estos son otros páginas del sitio que no se usan en este proyecto pero se crean para el POM (Page Object Model)
│   ├── search_product_page.py      # Buscar productos (SearchProducts)
│   ├── product_page.py             # Agregar al carrito, favoritos, etc. (ProductActions)
│   ├── cart_page.py                # Carrito de compras (ShopingPage)
│   ├── payment_page.py             # Pago (PurchasePage)
│   ├── page_favorites.py           # Favoritos (Favorites)


```



</details>

----

### 4. `O` Principle

```
│
├── tests/

```

<details>
<summary>Directorio `tests/` <br>- Abierto para extensión, cerrado para modificación</summary>

- Abierto para extensión, cerrado para modificación significa que podemos agregar nuevos tests o páginas sin modificar el código existente.
- Se puede agregar nuevos tests o páginas sin modificar el código existente.
- Se puede agregar nuevas validaciones o assertions sin modificar el código existente.
- Cada test es independiente de los demás y incluye sus propias validaciones y assertions.

>También se creó una clase aislada que contiene las assertions y validations, en lugar de agregarlas a cada test, esta clase se utiliza para centralizar las assertions y validations, y se encuentra en el directorio utils.


```
├── tests/    
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_page_form_submission.py
│   ├── test_account_user.py
│   ├── test_search_product.py
# Estos son otros tests del sitio que no se usan en este proyecto pero se crean para el POM (Page Object Model)
│   ├── test_add_to_cart.py
│   ├── test_favorites.py
│   ├── test_checkout.py
│   └── test_order_history.py

```

</details>


### Justification

- Para este proyecto se creó un solo módulo de pruebas, pero se puede crear más módulos para probar diferentes características del sitio, como una sugerencia se podrían crear estos diferentes directorios como módulos independientes: smoke, regression, e2e, etc.
- También es una buena práctica crear un módulo de pruebas con pruebas negativas, para validar los mensajes de error y las páginas de error, pero para este proyecto no se creó. La realidad es que con esta aislación es mejor separar la validación de la funcionalidad de la gestión de errores.
- Adicionalmente a los argumentos explicados anteriormente es importante mencionar que en el archivo `test_loging. py` si se incluyó una prueba negativa para validar el manejo de errores en caso de credenciales incorrectas.


### 5. `D`: Principle

```
│
├── utils/

```

<details>
<summary>Directorio `utils/`  <br> Principio de Inversión de Dependencias (los tests no dependen directamente del webdriver, los detalles como selectores, los datos, la configuración del navegador) </summary>

- El directorio `utils/` contiene las assertions, generador de datos, administrador de navegador, configuración y logger.
- Al aplicar este principio, se mantiene la lógica que indica que los módulos de alto nivel no deben depender de los módulos de bajo nivel, sino que ambos deben depender de abstracciones. 
- El directorio `utils/` proporciona abstracciones a los tests, por lo que los tests no dependen del webdriver, los detalles como selectores y la configuración del navegador se abstractan en capas (`utils`, `.env`, fixtures).
- Esto mantiene los tests independientes de los detalles de la implementación, utilizando abstracciones para ocultar los detalles de la implementación.


```
├── utils/  
│   ├── __init__.py
│   ├── assertions.py       # Asersiones 'Soft' y 'Hard', comparaciones personalizadas (assert equal) para validaciones de confirmaciones como si fuera un assert
│   ├──                     recibe text(actual) y luego compara (==) con text(expected)
│   ├──                     
│   ├── data_generator.py   # Generador de datos con Faker (usuarios, correos electrónicos, direcciones, etc.), para que los tests no dependan de detalles fijos como datos
│   ├── browser_manger.py   # Este abstracts webdriver para diferentes navegadores y asegura en la configuración de pytest (conftest.py) que los tests se ejecuten 
│   ├──                      sin depender de detalles fijos como datos (driver= Chromedriver vs driver=BrowseManger) y puede ser cambiado a otros sin tocar los tests
│   ├──                     
│   ├── config.py           # Centraliza valores como urls, selectores, timeout y evita hardcodearlos (datos fijos dentro del código) en los tests, esto significa que,
│   ├──                      si un locator con un atributo CSS único (By.Id, "email") cambia, debe buscarse dentro del test para cambiarlo, 
│   ├──                      por lo que Config se utiliza como una abstracción para hacer los tests independientes de datos fijos
│   ├──                     
│   └── logger.py          # Centraliza logging con formato, timestamp y niveles (info, error, debug)
│


```

</details>


### 6. `D`: Repeatability Principle

```
│
├── .env

```

<details>
<summary>Archivo `.env` (contiene variables de entorno para configuración: `selectores, urls, locators, timeout`, etc.) <br> Inversión de Dependencia (el código no depende de los detalles de la implementación)</summary>

- El archivo `.env` contiene variables de entorno para configuración: `selectores, urls, locators, timeout`, etc.
- Evita hardcode fixed islotes the variables values. 
- Por ejemplo, si un locator con un atributo CSS único (By.Id, "email") cambia, debe buscarse dentro del test para cambiarlo.
- Por lo que Config se utiliza como una abstracción para hacer los tests independientes de datos fijos
- Este archivo debe agregarse a .gitignore, porque contiene datos sensibles, por lo que no debe ser comprometido al repositorio, por razones de seguridad, por el mismo motivo puedes ver el archivo .env incluido en el archivo .gitignore, y no se muestra en este repositorio

>Para los locators complejos con XPATH, se recomienda usar un archivo locators.py o un archivo .ymal para evitar hardcode fixed islotes the variables values, such as locators.yml


```

├── .env   
├──     
# Other posible files to manage the locators variables values.                        
├── locators.py
├── locators.yml


```

**Ejemplo de .env file para ser usado como plantilla para crear .env file**

Para un mejor guia de esta práctica se puede ver el archivo .env_example en este mismo directorio (`docs/english/.env_example`).
Se recomienda crear un nuevo `.env` file y agregar las variables de entorno para configuración y `selectores, urls, locators, timeout`, etc.

**Nota:** El archivo original `.env` no se incluye en este repositorio, por razones de seguridad y privacidad, por lo que solo es para fines de ejemplo


</details>


----

### Otros archivos importantes de Configuración


<details>
<summary>Archivo `conftest.py` (Contiene las `fixtures` de Pytest: browser, setup, teardown,log info, manager)</summary>

- Este archivo contiene las fixtures de Pytest, que son usadas para setup y teardown del browser, log info, manager y browser.
- Las fixtures son funciones especiales que pytest proporciona para compartir setup y teardown code across tests, in other words, it is a way to share code across tests, for example:
   - Si un test usa un browser, se comparte en todos los tests, por lo que no es necesario crear un nuevo browser para cada test.
   - Si un test usa un teardown method, se comparte en todos los tests, por lo que no es necesario crear un nuevo teardown para cada test.

- Este archivo, es una convención de pytest para aplicar una configuración centralizada para compartir utilidades across tests.

```
├── conftest.py     
├──                     

```

</details>

<details>

<details>

<summary>Archivo `requirements.txt` (Contiene las dependencias del proyecto,librerías, versiones fijas para mayor control y reproducibilidad)</summary>

**Dependencias del proyecto,librerías, versiones fijas para mayor control y reproducibilidad**

- These files allow to install the project dependencies in this case using `pip install -r requirements.txt`

```
├── requirements.txt       
|

```

</details>

<details>

<summary>`pytest.ini` File (configurations of Pytest) </summary> 

**Pytest configurations: report of Allure, testpath for define "test" as the root directory of the tests, marker for tag the test as: smoke,regression,integration**

- Este archivo contiene las configuraciones generales de Pytest, como:
   - Reporte de Allure
   - `testpath` para indicar a Pytest la ubicacion del codigo de los test para que pueda ejecutar el codigo, en este caso se define `tests/` que se encuentra en la raiz del directorio, si los test estan en otra ubicacion, se debe cambiar la ruta, por ejemplo: `ejecuciones_test/` 
   - marker para etiquetar el test como: smoke,regression,integration


```
├── pytest.ini             
├──                      

```

**Los `markers` usados en este archivo pueden ser adaptados a las necesidades del proyecto, por ejemplo:**
- `smoke`: tests que validan la funcionalidad más importante de la aplicación
- `regression`: tests que validan que la funcionalidad previa de la aplicación sigue funcionando después de los cambios
- `n+1`: tests que validan que la funcionalidad previa de la aplicación sigue funcionando después de las correcciones
- `end_to_end`: tests que validan un flujo específico de la aplicación

>Los `markers` son útiles para etiquetar los tests y comandos de ejecución, con un tag específico, por ejemplo:

```
pytest -m smoke
pytest -m regression
pytest -m integration
pytest -m end_to_end
pytest -m performance

```

</details>

----

### Unit Tests for page objects

Como QA estamos creando un framework de automatización con robustez en mente y calidad en mente,  mejores prácticas de código, necesitamos validar que los objetos de página están funcionando como se espera, por lo que necesitamos validar que los métodos llamen a los helpers esperados y que los valores de retorno y el flujo de control funcionen como se pretende.

<details>
<summary>Directorio `tools/` - Pruebas Unitarias para Page Objects: </summary>

- El directorio tools contiene pruebas unitarias para objetos de página bajo `pages/` que no requieren iniciar un navegador real. Utilizan `pytest` y monkeypatching para validar que:
- Los métodos llamen a los helpers esperados (e.g., `send_keys`, `click`).
- Los valores de retorno y el flujo de control funcionen como se pretende.
- La extracción de texto y las verificaciones de visibilidad están conectadas a los selectores configurados.

```
├── tools/                   # Pruebas unitarias para objetos de página
│   ├── __init__.py
│   ├── conftest.py          # Fixtures globales de pytest para pruebas unitarias
|   |__README.md             # Explicación de las pruebas unitarias y cómo ejecutarlas
│   ├── test_account_user_unit.py
│   ├── test_login_unit.py
│   ├── test_page_form_submission_unit.py
│   ├── test_search_product_unit.py
│   └── test_login_unit.py


```

</details>





















