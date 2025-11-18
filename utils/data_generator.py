"""
English: 
- Data generator with Faker Python library(users, emails, addresses, etc.)
- This generator is used to create random data for the tests, to validate the functionality of the site.
- So it is not need to create manual data for the tests, each time you need to iterate the tests, it will create random data.

Spanish: 
- Generador de datos con la librería Faker de Python (usuarios, emails, direcciones, etc.)
- Este generador se utiliza para crear datos aleatorios para los tests, para validar la funcionalidad del sitio.
- Así que no es necesario crear datos manualmente para los tests, cada vez que necesites iterar los tests, creará datos aleatorios.

"""

from faker import Faker
import random

fake = Faker()

def generate_user():
    generated_password = fake.password(
    length=12, special_chars=True, 
    digits=True, upper_case=True, lower_case=True
    )
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": generated_password,
        "confirm_password": generated_password
    }

def generate_invalid_email_user():
    user = generate_user()
    user["email"] = "not-an-email"
    return user

def generate_short_password():
    user = generate_user()
    user["password"] = "123"
    user["confirm_password"] = "123"
    return user

def generate_user_with_mismatched_passwords():
    user = generate_user()
    user["confirm_password"] = user["password"] + "xyz"
    return user

def generate_user_with_empty_passwords():
    user = generate_user()
    user["password"] = ""
    user["confirm_password"] = ""
    return user