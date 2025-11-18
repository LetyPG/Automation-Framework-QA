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