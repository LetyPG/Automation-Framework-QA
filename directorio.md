/mi_framework_QA/Magento_APP
│
├── drivers/        <> L: Sustituibilidad de Liskov (soporte para distintos navegadores)
│   └── chromedriver.exe     #El código puede usarse en distintas implementaciones del manejador 
│                               (Webdriver) en sobre distintos navegadores 
│                               (Chrome, Firefox, Zafari) sin romper los test.
│                              #Si una clase hija (LoginPage) extiende y utiliza la clase padre 
│                                (Basepage),entonces no modifica el flujo de la prueba.
├── pages/          <> S: Responsabilidad única (cada clase modela una sola página)
│   ├── __init__.py
│   ├── base_page.py                # Clase base (BasePage)donde se instancia el manejador (driver)  │    ├──                           para el Sistema de Automatización  con operaciones genéricas 
│   ├──                            para todas las  páginas, así se crea el primero Objeto "Page"     
│   ├──                            iniciando el modelo POM (Page Object Model)                          
│   ├──                            - Define métodos reutilizables que encapsulan lógica de interacción 
│   ├──                              con el navegador y los elementos (hacer clic, escribir, esperar)
│   ├──                            - Apoya el principio DRY (Don’t Repeat Yourself)               
│   ├──             <> I: Principio de Segregación de Interfaces
Cada clase Page modela una sola pagina web
│   ├──                              # Se crea una nueva clase para instanciar al driver, donde
│   ├──                             se heredan (herencia) los métodos genericos de la clase base  
│   ├──                             (BasePage) y se agregan metodos específicos de cada interface,  
│   ├──                             se crea asi una nueva Objeto Page por cada interfaz
│   ├── login_page.py               # Login (LoginPage)
│   ├── page_form_submission.py     # Formulario de autenticación (registro) (SubmissionForm)
│   ├── page_account_user.py        # Cuenta de Usuario (UserAccount)
├   ├── search_product_page.py      # Búsqueda de productos (SearchProducts)
│   ├── product_page.py             # Agregar al carrito, favoritos, etc. (ProductActions)
│   ├── cart_page.py                # Carrito de compras (ShopingPage)
│   └── payment_page.py             # Página de pago (PurchasePage)
│
├── tests/         <> O: Abierto a extensión, cerrado a modificación
│                                     #se pueden agregar nuevas pruebas o pages
│                                      sin modificar las anteriores
│                                     # Se pueden agregar las comprobaciones o validaciones (Assertions)
│                                      o usar una clase que contenga los metodos para las validaciones
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_page_form_submission.py
│   ├── test_account_user.py
│   ├── test_search_product.py
│   ├── test_add_to_cart.py
│   ├── test_favorites.py
│   ├── test_checkout.py
│   └── test_order_history.py
│
├── utils/  # D: Inversión de dependencias (test no depende  directo del webdriver)
│   ├── __init__.py
│   ├── assertions.py       # Soft/hard assertions, comparaciones personalizadas (assert equal)
│   ├──                     Se crea una clase con métodos para validaciones de confirmaciones como si un 
│   ├──                     texto recibido(actual) es igual(==) al esperado (expected)
│   ├── data_generator.py   # Generador de datos con Faker (usuarios, emails, direcciones, etc.)
│   ├──                       las abstracciones como los test no deben depender de detalles fijos 
│   ├──                       como los datos
│   ├── browser_manger.py   # Abstrae webdriver para distintos navegadores y asegura en la
│   ├──                       configuración de pytest (conftest.py) que se puedan ejecutar los test 
│   ├──                       sin depender de detalles específicos (driver= Chromedriver vs 
│   ├──                       driver=BrowseManger) y se pueda cambiar a otros sin tocar las pruebas
│   ├── config.py          # Configuraciones generales y carga de variables desde .env
│   ├──                      Centraliza valores como urls, locators,timeout y evita harcodearlos (datos │   ├──                       fijos dentro del código fuente) en los test, esto significa que,
│   ├──                       si se coloca un locator con un atributo CSS con un valor unico 
│   ├──                      (By.Id, "email") y este cambia, hay que buscar dentro del test para 
│   ├──                      cambiarlo, así como una url que tambien puede cambiar, en lugar de esto
│   ├──                      se usa Config como una abstracción para que los test 
│   ├──                      no dependan de datos fijos
│   └── logger.py          # Logging centralizado con formato, timestamp y niveles (info, error, debug)
│
├── .env                    # Archivo con Variables de entorno para configuración  y selectores 
│   ├──                      (URL, locators por cada page, en el caso de locators con XPATH recomiedo un │   ├──                      archivo locators.py  o un archivo .ymal si se quiere mantener el principio │   ├──                      de no hardcode: datos fijos en el código fuente)
├── conftest.py             # Fixtures de Pytest: navegador, setup, teardown,log info, manager
├── requirements.txt        # Dependencias del proyecto,librerias, fija versiones para mayor control 
├                            y reproducibilidad:(pip install -r requirements.txt)
├── pytest.ini              # Configuraciones generales de Pytest (reporte de Allure,
├                            testpath para definir "test" como el directorio raíz de los tests,
├                            marker para etiquetar los test como: smoke,regression,integration)
└── README.md               # Documentación del framework 
