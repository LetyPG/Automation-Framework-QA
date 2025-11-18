# Principios de diseño SOLID 

Los principios SOLID son una guía para diseñar software que sea mantenible, escalable y fácil de entender, originalmente propuestos por Robert C. Martin (también conocido como Uncle Bob) y en inglés son conocidos como SOLID Principles. Para este proyecto educativo se van mencionando con la traducción al español, pero se mantiene el nombre en ingles para promover el reconocimiento de los mismos tanto en su uso habitual como por mantener su terminología internacional, ademas porque en otros contextos es vinculado a otros conceptos y aparecen en Ingles como 'Clean Code', que es una guía para escribir código que sea mantenible, escalable y fácil de entender.

- **S: Single Responsibility - Responsabilidad Unica**  

  Cada clase representa una sola responsabilidad, utilizando el Page Object Model, representando una sola página del sitio.
  
- **O: Open/Closed - Abierto/Cerrado**  

  El framework es abierto a nuevas funcionalidades sin modificar el código existente.
  
- **L: Liskov Substitution - Sustitución de Liskov**  
  Soporta múltiples navegadores con una estructura intercambiable en la gestión del driver.
  
- **I: Interface Segregation - Segregación de Interfaces**  
  Los tests consumen solo lo que es necesario de cada clase, sin depender de implementaciones innecesarias.
  Este principio originalemnte se usa para centralizar metodos comunes, que sean los mas generales, sin que haya modificaciones en el codigo existente, sin necesidad de crear una clase base como una interface abstracta y que pueda ser reutilizado en diferentes interfaces.
     - En el caso de este framework se trato de mantener un poco la misma logica, creando una interface abstracta que tenga los metodos mas genericos y luego en cada interface se implementan los metodos especificos de la pagina web y se importan los mas genericos.
  

- **D: Dependency Inversion - Inversión de Dependencias**  
  Los tests no dependen directamente de Selenium: los detalles como selectores y configuración del navegador se abstractan en capas (`utils`, `.env`, fixtures).

  ## DRY (Don't Repeat Yourself/ No Repetirte)
  Se crearon una clase base para operaciones reutilizables, y una clase base para operaciones API reutilizables:
  - `BaseActions` para operaciones reutilizables
  - `BaseAPIClient` define la estructura de los metodos HTTP
  
  Para escalar el framework, el paradigma utilizado es el Page Object Model (POM), que es un patrón de diseño que crea un repositorio de objetos para los elementos de la interfaz de usuario web. Cada página web se representa como una clase, y los elementos web se definen como variables dentro de esa clase.
  Esta arquitectura permite una fácil mantenimiento y escalabilidad del framework.
  
  ### Como usar el Page Object Model y el principio DRY?
  
  Para usar el Page Object Model y el principio DRY, los siguientes pasos deben seguidos:
  
  1. Crear una nueva clase de objeto de página para la página que deseas probar.
  2. Definir los elementos web como variables dentro de la clase.
  3. Usar la clase de objeto de página en tus pruebas.
  4. Usar el principio DRY para evitar la duplicación de código.
  
  
  ### Estructura del Framework y Convenciones de Directorios
  
  El framework está estructurado de la siguiente manera:
  
  - `README.md` archivo: Contiene el README para entender el framework y propósitos educativos en inglés y español.
  - `src/` directorio: Contiene los objetos de página para el sitio web, se usa `src` como nombre de la carpeta para seguir la convencion de nombres de carpetas en inglés, que indican que contiene el código fuente del proyecto, por lo que `src` es la abreviatura de `source` que en español se traduce como `fuente`.
  - `ci-cd/` directorio: Contiene los archivos de ci-cd para el sitio web.
  - `docs/` directorio: Contiene la documentación para entender el framework y propósitos educativos.
  - `features/` directorio: Contiene las funcionalidades para aplicar BDD (Behavior Driven Development).
  - `tests/` directorio: Contiene todas las suites de pruebas.
  - `tools/` directorio: Contiene las herramientas para el sitio web, en este momento, contiene una herramienta para ejecutar pruebas unitarias sobre las funciones de las páginas.
  - `utils/` directorio: Contiene las utils para el sitio web.
  - `config.py` archivo: Contiene la configuración para el sitio web.
  - `.env` archivo: Contiene las variables de entorno para el sitio web.
  
  
  
  
    ## Next Steps
    
    - Review [Page Object Model](programming_standards.md) para ejemplos detallados de POM
    - Check [Coding Standards](coding_repository_standards.md) para principios SOLID
    - Check [Coding Standards](programming_paradigm.md) para principios SOLID
    - Explore [Best Practices](selenium.md) para QA guidelines
    - Explore [Best Practices](pytest.md) para QA guidelines
    - Read [Getting Started](getting_started.md) para ejecutar el framework
  
  **Version**: 0.1.2  
  **Framework**: C-QA Automation Framework  
    