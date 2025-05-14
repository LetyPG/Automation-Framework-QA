Docuemtacion del framework
# Automation-Framework-QA

Este proyecto es un framework de Automatización de Pruebas desarrollado con Python, Pytest y Selenium WebDriver, diseñado para garantizar **escalabilidad**, **mantenibilidad** y **claridad estructural** mediante la aplicación de principios SOLID y buenas prácticas de ingeniería de software.

## 💡 Objetivo

Automatizar flujos críticos de una tienda e-commerce Magento, validando funcionalidades como login, registro de usuario, búsqueda, carrito de compras y checkout, de forma confiable y reutilizable.

## ⚙️ Tecnologías utilizadas

- **Python 3.12+**
- **Selenium WebDriver**
- **Pytest**
- **Faker** (para datos dinámicos)
- **Allure Reports**
- **dotenv** (manejo seguro de configuraciones)

## 📐 Arquitectura basada en principios SOLID

- **S: Single Responsibility**  
  Cada clase representa una sola página del sitio (Page Object Model).
  
- **O: Open/Closed**  
  El framework está abierto a nuevas funcionalidades sin modificar el código existente.
  
- **L: Liskov Substitution**  
  Soporta múltiples navegadores con una estructura intercambiable en el manejo del driver.
  
- **I: Interface Segregation**  
  Las pruebas consumen sólo lo necesario de cada clase, sin depender de implementaciones innecesarias.
  
- **D: Dependency Inversion**  
  Las pruebas no dependen directamente de Selenium: los detalles como selectores y configuración del browser se abstraen en capas (`utils`, `.env`, fixtures).

## 📁 Estructura del proyecto

```plaintext
Automation-Framework-QA/
│
├── pages/                 # Clases por página (modelo POM)
├── tests/                 # Casos de prueba modulares
├── utils/                 # Configuración, logs, datos y helpers
├── .env                   # Variables de entorno y locators externos
├── conftest.py            # Fixtures globales de Pytest
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación del framework

