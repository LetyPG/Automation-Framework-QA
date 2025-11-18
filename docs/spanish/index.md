# Marco de Automatización QA - Índice de Documentación

Bienvenido a la documentación completa de este Marco de Automatización QA educativo. Este framework demuestra las mejores prácticas para la automatización de pruebas UI usando Python, Selenium WebDriver y Pytest.

---

## 📚 Estructura de la Documentación

### Primeros Pasos
- **[Guía de Inicio](getting_started.md)** - Configuración paso a paso y primera ejecución de pruebas
- **[Resumen del Proyecto](project_overview.md)** - Estructura completa del proyecto y aplicación de principios SOLID
- **[Configuración del Entorno](.env_example.txt)** - Archivo .env de ejemplo con todas las variables requeridas

### Conceptos Fundamentales
- **[Estrategia de Automatización](automation_strategy.md)** - Por qué Page Object Model, fixtures y decisiones arquitectónicas
- **[Estándares de Código](coding_repository_standards.md)** - Principios SOLID y patrones de diseño aplicados
- **[Mejores Prácticas](best_practices.md)** - Guías y recomendaciones de automatización QA

### Tecnologías Utilizadas
- **[Python](technologies/python.md)** - Fundamentos del lenguaje y entornos virtuales
- **[Selenium WebDriver](technologies/selenium.md)** - Automatización de navegadores y conceptos de WebDriver
- **[Pytest](technologies/pytest.md)** - Framework de pruebas, fixtures y markers
- **[Faker](technologies/faker.md)** - Generación dinámica de datos de prueba
- **[Reportes Allure](technologies/allure.md)** - Reportes y visualización de pruebas

### Componentes del Framework
- **[Modelo de Objeto de Página](page_object_model.md)** - Implementación del patrón POM
- **[Acciones Base](base_actions.md)** - Operaciones Selenium reutilizables
- **[Gestión de Configuración](configuration.md)** - Variables de entorno y localizadores
- **[Pruebas Unitarias](../tools/README.md)** - Pruebas de objetos de página sin navegador

---

## Enlaces Rápidos

### Para Principiantes
1. Comienza con la [Guía de Inicio](getting_started.md)
2. Comprende el [Resumen del Proyecto](project_overview.md)
3. Aprende sobre el [Modelo de Objeto de Página](page_object_model.md)
4. Revisa las [Mejores Prácticas](best_practices.md)

### Para Ingenieros QA Experimentados
1. Revisa la [Estrategia de Automatización](automation_strategy.md)
2. Examina los [Estándares de Código](coding_repository_standards.md)
3. Explora las [Pruebas Unitarias](../tools/README.md)

---

## 🌐 Enlaces a Documentación Oficial

- **Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Selenium**: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- **Pytest**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **Faker**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)
- **Allure**: [https://docs.qameta.io/allure/](https://docs.qameta.io/allure/)

---

## Acerca de Este Framework

Este es un **proyecto educativo** diseñado para demostrar:
- Principios SOLID en automatización de pruebas
- Patrón de diseño Page Object Model (POM)
- Fixtures y markers de Pytest
- Gestión de configuración con .env
- Pruebas unitarias para objetos de página
- Gestión de drivers de navegador con Selenium Manager
- Datos de prueba dinámicos con Faker
- Reportes completos con Allure

**Audiencia Objetivo**: Ingenieros QA, principiantes en automatización de pruebas y cualquier persona aprendiendo automatización UI basada en Python.

**Nota**: Este es un proyecto demo con fines educativos, no código listo para producción.

---

## Estructura del Repositorio

```
Automation-Framework-QA/
├── docs/                    # Documentación (¡estás aquí!)
├── driver/                  # Drivers de navegador opcionales
├── src/                     # Código fuente del proyecto
|   ├── pages/               # Clases de Objeto de Página
|   ├── api/                 # Clases de API
|
|__ ci-cd/                   # Directorio para el CI/CD
|__ features/                # Directorio para los features permite aplicar el modelo BDD (Behavior Driven Development/Desarrollo Guiado por Comportamiento)
├── tests/                   # Modulos de test cases agrupados por suites de pruebas, donde cada una contiene una estrategia de pruebas como smoke, regression, api, e2e, etc
├── tools/                   # Pruebas unitarias para objetos de página
├── utils/                   # Utilidades (config, data, browser, assertions)
├── .env                     # Variables de entorno (no en el repo)
├── conftest.py              # Fixtures globales de Pytest
├── pytest.ini               # Configuración de Pytest
└── requiriments.txt         # Dependencias de Python
```

---

## Contribuciones

Este es un framework educativo. Siéntete libre de:
- Hacer fork y experimentar
- Sugerir mejoras
- Reportar problemas
- Compartir con otros que estén aprendiendo automatización QA

---

**Versión**: 0.1.2  
**Última Actualización**: 2025  
**Idioma**: [English](../english/index.md) | Español
