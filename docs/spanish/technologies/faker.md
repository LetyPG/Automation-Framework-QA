# Faker - Generación Dinámica de Datos de Prueba

## ¿Qué es Faker?

**Faker** es una biblioteca de Python que genera datos falsos (pero realistas) para propósitos de prueba. Puede crear nombres, correos electrónicos, direcciones, números de teléfono y mucho más.

**Documentación Oficial**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)

---

## ¿Por qué Faker para Automatización de Pruebas?

### Ventajas

1. **Datos de Prueba Realistas**
   - Genera datos que parecen reales
   - Evita valores de prueba codificados
   - Mejor cobertura de pruebas

2. **Aleatorización**
   - Datos diferentes en cada ejecución de prueba
   - Detecta casos límite
   - Previene contaminación de datos de prueba

3. **Soporte de Localización**
   - Generar datos en múltiples idiomas
   - Probar internacionalización
   - Formatos específicos de región

4. **Amplia Gama de Tipos de Datos**
   - Información personal (nombres, correos, teléfonos)
   - Direcciones y ubicaciones
   - Datos de internet (URLs, IPs, user agents)
   - Fechas, números, texto

5. **Fácil de Usar**
   - API simple
   - Métodos encadenables
   - Extensible con proveedores personalizados

---

## Instalación

```bash
pip install faker
```

---

## Uso Básico

```python
from faker import Faker

# Crear instancia de Faker
fake = Faker()

# Generar datos
name = fake.name()                    # "John Smith"
email = fake.email()                  # "john.smith@example.com"
address = fake.address()              # "123 Main St, City, State 12345"
phone = fake.phone_number()           # "+1-555-123-4567"
```

---

## Cómo Este Framework Usa Faker

### Generador de Datos (`utils/data_generator.py`)

Generación centralizada de datos de prueba:

```python
from faker import Faker
import random

class DataGenerator:
    """Genera datos de prueba dinámicos usando Faker."""
    
    def __init__(self, locale='en_US'):
        self.fake = Faker(locale)
    
    def generate_user(self):
        """Generar datos completos de usuario."""
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.generate_password(),
            "phone": self.fake.phone_number(),
            "address": self.fake.address()
        }
    
    def generate_password(self, length=12):
        """Generar contraseña segura."""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
        return ''.join(random.choice(chars) for _ in range(length))
    
    def generate_email(self, domain="example.com"):
        """Generar correo con dominio específico."""
        username = self.fake.user_name()
        return f"{username}@{domain}"
```

### Uso en Pruebas

```python
from utils.data_generator import DataGenerator

def test_user_registration(browser):
    # Generar datos de prueba
    generator = DataGenerator()
    user_data = generator.generate_user()
    
    # Usar en prueba
    page = RegistrationPage(browser)
    page.fill_form(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
        password=user_data["password"]
    )
    page.submit()
    
    assert page.is_success_message_visible()
```

**Beneficios**:
- Datos frescos en cada ejecución de prueba
- Sin valores codificados
- Escenarios de prueba realistas
- Evitar problemas de datos duplicados

---

## Proveedores Comunes de Faker

### Información Personal

```python
fake.name()                    # "Jane Doe"
fake.first_name()              # "Jane"
fake.last_name()               # "Doe"
fake.name_male()               # "John Smith"
fake.name_female()             # "Mary Johnson"
fake.prefix()                  # "Dr."
fake.suffix()                  # "Jr."
```

### Datos de Internet

```python
fake.email()                   # "user@example.com"
fake.safe_email()              # "user@example.org" (dominios seguros)
fake.free_email()              # "user@gmail.com"
fake.company_email()           # "user@company.com"
fake.user_name()               # "john_smith"
fake.password()                # "aB3$xY9#kL2@"
fake.url()                     # "https://example.com"
fake.ipv4()                    # "192.168.1.1"
fake.mac_address()             # "00:1B:63:84:45:E6"
```

### Dirección y Ubicación

```python
fake.address()                 # "123 Main St\nCity, State 12345"
fake.street_address()          # "123 Main St"
fake.city()                    # "New York"
fake.state()                   # "California"
fake.state_abbr()              # "CA"
fake.zipcode()                 # "12345"
fake.country()                 # "United States"
fake.latitude()                # "40.7128"
fake.longitude()               # "-74.0060"
```

### Números de Teléfono

```python
fake.phone_number()            # "+1-555-123-4567"
fake.msisdn()                  # "1234567890" (móvil)
```

### Fechas y Horas

```python
fake.date()                    # "2023-05-15"
fake.date_of_birth()           # "1990-03-20"
fake.date_between(start_date='-30d', end_date='today')  # Fecha reciente
fake.future_date()             # Fecha futura
fake.past_date()               # Fecha pasada
fake.time()                    # "14:30:00"
fake.iso8601()                 # "2023-05-15T14:30:00"
```

### Texto y Lorem Ipsum

```python
fake.text()                    # Párrafo de texto
fake.sentence()                # "Lorem ipsum dolor sit amet."
fake.word()                    # "lorem"
fake.words(5)                  # ["lorem", "ipsum", "dolor", "sit", "amet"]
fake.paragraph()               # Párrafo completo
```

### Números

```python
fake.random_int(min=1, max=100)        # 42
fake.random_digit()                    # 7
fake.random_number(digits=5)           # 12345
fake.pyfloat(left_digits=2, right_digits=2)  # 12.34
```

### Empresa y Trabajo

```python
fake.company()                 # "Acme Corporation"
fake.job()                     # "Software Engineer"
fake.bs()                      # "synergize innovative solutions"
```

### Tarjetas de Crédito (¡Solo Datos de Prueba!)

```python
fake.credit_card_number()      # "4532123456789012"
fake.credit_card_provider()    # "Visa"
fake.credit_card_expire()      # "12/25"
fake.credit_card_security_code()  # "123"
```

---

## Características Avanzadas

### Localización

Generar datos en diferentes idiomas:

```python
# Inglés (US)
fake_us = Faker('en_US')
print(fake_us.address())  # Formato US

# Español
fake_es = Faker('es_ES')
print(fake_es.name())     # Nombre español

# Francés
fake_fr = Faker('fr_FR')
print(fake_fr.address())  # Dirección francesa

# Múltiples locales
fake_multi = Faker(['en_US', 'es_ES', 'fr_FR'])
print(fake_multi.name())  # Aleatorio de cualquier local
```

### Semilla para Reproducibilidad

Generar los mismos datos entre ejecuciones:

```python
# Establecer semilla para datos reproducibles
Faker.seed(12345)

fake1 = Faker()
print(fake1.name())  # Siempre el mismo nombre

# Reiniciar y usar la misma semilla
Faker.seed(12345)
fake2 = Faker()
print(fake2.name())  # Mismo nombre que fake1
```

**Caso de Uso**: Depurar fallos específicos de pruebas

### Proveedores Personalizados

Crear tus propios generadores de datos:

```python
from faker.providers import BaseProvider

class CustomProvider(BaseProvider):
    def product_name(self):
        products = ["Laptop", "Phone", "Tablet", "Monitor"]
        return self.random_element(products)
    
    def product_price(self):
        return f"${self.random_int(100, 2000)}.99"

# Agregar a Faker
fake = Faker()
fake.add_provider(CustomProvider)

print(fake.product_name())  # "Laptop"
print(fake.product_price())  # "$599.99"
```

### Valores Únicos

Asegurar que no haya duplicados:

```python
fake = Faker()

# Generar correos únicos
for _ in range(10):
    email = fake.unique.email()
    print(email)  # Todos diferentes

# Reiniciar rastreador de únicos
fake.unique.clear()
```

---

## Ejemplos Prácticos para Este Framework

### 1. Prueba de Registro de Usuario

```python
def test_user_registration(browser):
    generator = DataGenerator()
    
    # Generar usuario único
    user = generator.generate_user()
    
    page = RegistrationPage(browser)
    page.open(Configuration.SUBMISSION_URL)
    page.fill_registration_form(
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"],
        password=user["password"]
    )
    page.submit()
    
    assert page.is_success_message_visible()
```

### 2. Creación de Múltiples Usuarios

```python
def test_create_multiple_users(browser):
    generator = DataGenerator()
    
    for _ in range(5):
        user = generator.generate_user()
        create_user(browser, user)
        verify_user_created(browser, user["email"])
```

### 3. Validación de Formulario con Casos Límite

```python
def test_email_validation(browser):
    generator = DataGenerator()
    
    # Probar con varios formatos de correo
    emails = [
        generator.fake.email(),           # Estándar
        generator.fake.free_email(),      # Proveedor gratuito
        generator.fake.company_email(),   # Empresa
        "invalid-email",                  # Inválido
        "",                               # Vacío
    ]
    
    for email in emails:
        test_email_input(browser, email)
```

### 4. Búsqueda con Consultas Aleatorias

```python
def test_product_search(browser):
    generator = DataGenerator()
    
    # Generar términos de búsqueda
    search_terms = [
        generator.fake.word(),
        generator.fake.sentence(nb_words=3),
        "jacket",  # Producto conocido
    ]
    
    for term in search_terms:
        page = SearchPage(browser)
        page.search(term)
        results = page.get_results()
        # Verificar resultados
```

---

## Mejores Prácticas

### 1. Centralizar Generación de Datos

```python
# Bueno - Centralizado en DataGenerator
generator = DataGenerator()
user = generator.generate_user()

# Evitar - Disperso en las pruebas
fake = Faker()
name = fake.name()  # En prueba 1
email = fake.email()  # En prueba 2
```

### 2. Usar Datos Significativos

```python
# Bueno - Datos realistas
email = fake.email()  # "john.smith@example.com"

# Evitar - Datos obviamente falsos
email = "test@test.com"  # Menos realista
```

### 3. Combinar con Datos Reales

```python
# Mezclar Faker con datos de prueba reales
user = {
    "first_name": fake.first_name(),  # Aleatorio
    "last_name": fake.last_name(),    # Aleatorio
    "email": fake.email(),            # Aleatorio
    "country": "United States",       # Fijo para prueba
    "role": "customer"                # Fijo para prueba
}
```

### 4. Manejar Restricciones Únicas

```python
# Para campos que deben ser únicos
def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    username = fake.user_name()
    return f"{username}_{timestamp}@example.com"
```

---

## Faker vs Datos de Prueba Manuales

| Enfoque | Pros | Contras |
|----------|------|---------|
| **Faker** | Realista, aleatorizado, sin duplicados | Más difícil depurar fallos específicos |
| **Codificado** | Predecible, fácil de depurar | Poco realista, duplicados, mantenimiento |
| **Híbrido** | Lo mejor de ambos mundos | Requiere planificación |

**Este framework usa Faker** para datos de prueba realistas y dinámicos.

---

## Solución de Problemas

### Problema: Mismos Datos en Cada Ejecución

**Solución**: No establecer semilla (o usar semillas diferentes)
```python
# Evitar para datos aleatorios
Faker.seed(12345)

# O usar timestamp como semilla
import time
Faker.seed(int(time.time()))
```

### Problema: Necesita Formato Específico

**Solución**: Personalizar con Python
```python
# Formato de correo personalizado
username = fake.user_name()
email = f"{username}@mycompany.com"

# Formato de teléfono personalizado
area_code = fake.random_int(200, 999)
number = fake.random_int(1000000, 9999999)
phone = f"({area_code}) {number}"
```

### Problema: Locale No Funciona

**Solución**: Instalar datos específicos de locale
```python
# Algunos locales necesitan paquetes extra
pip install faker[locales]
```

---

## Recursos de Aprendizaje

### Documentación Oficial
- **Documentación Faker**: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)
- **Lista de Proveedores**: [https://faker.readthedocs.io/en/master/providers.html](https://faker.readthedocs.io/en/master/providers.html)

### Tutoriales
- **Real Python - Guía Faker**: [https://realpython.com/](https://realpython.com/)
- **Ejemplos GitHub**: [https://github.com/joke2k/faker](https://github.com/joke2k/faker)

---

## Resumen

Faker mejora este framework con datos de prueba dinámicos:
- **Datos realistas** - Nombres, correos, direcciones que parecen reales
- **Aleatorización** - Datos diferentes en cada ejecución
- **Localización** - Soporte para múltiples idiomas/regiones
- **Fácil de usar** - API simple, proveedores extensos
- **Cobertura de pruebas** - Mejor detección de casos límite

**Próximos Pasos**:
- Revisa `utils/data_generator.py` para la implementación
- Experimenta con diferentes proveedores de Faker
- Agrega proveedores personalizados para datos específicos del dominio
- Consulta [Mejores Prácticas](../best_practices.md) para consejos de generación de datos
