"""
English: 
This logic was intended to create a configuration class to centralize the configuration of the tests, 
This is an abstraction to make the tests independent of fixed data
So on the test files are imported the Configuration class and the locators are parsed using the parse_locator function
And the variables are parsed using the parse_locator function
This class handles the variables and the charges form the .env file, so the test files only keeps the logic on main goal which is to validate the functionality of the site.

Spanish: 
Esta lógica fue diseñada para crear una clase de configuración para centralizar la configuración de los tests, 
Esta es una abstracción para hacer los tests independientes de datos fijos
Entonces en los archivos de test se importa la clase Configuration y los locators se parsean usando la función parse_locator
Las varables son cargadas usando la funcion 'parse_locator'
Las variables y los valores se cargan desde el archivo .env, por lo que los test archivos solo mantienen la lógica del objetivo principal que es validar la funcionalidad del sitio.

"""



import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


def parse_locator(env_value, var_name=None):
    """Convierte 'css,#id' en (By.CSS_SELECTOR, '#id')"""
    if not env_value:
        raise ValueError(f"El valor del locator para '{var_name or 'UNKNOWN'}' está vacío o no definido en el archivo .env")
    by_map = {
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "class": By.CLASS_NAME,
        "tag": By.TAG_NAME,
        "link": By.LINK_TEXT,
        "plink": By.PARTIAL_LINK_TEXT,
    }
    tipo, valor = env_value.split(",", 1)
    return (by_map[tipo.strip().lower()], valor.strip())


class Configuration:
    BASE_URL = os.getenv('BASE_URL')
    LOGIN_URL = os.getenv('LOGIN_URL')
    SUBMISSION_URL = os.getenv('SUBMISSION_URL')
    ACCOUNT_URL = os.getenv('ACCOUNT_URL')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    # Locators Page Submission
    FIRST_NAME_INPUT = parse_locator(os.getenv('FORM_NAME'), 'FORM_NAME')
    LAST_NAME_INPUT = parse_locator(os.getenv('FORM_LAST_NAME'), 'FORM_LAST_NAME')
    EMAIL_INPUT = parse_locator(os.getenv('FORM_EMAIL'), 'FORM_EMAIL')
    PASSWORD_INPUT = parse_locator(os.getenv('FORM_PASSWORD'), 'FORM_PASSWORD')
    CONFIRM_PASSWORD_INPUT = parse_locator(os.getenv('FORM_CONFIRMATION_PASSWORD'), 'FORM_CONFIRMATION_PASSWORD')
    PASSWORD_STRENGTH_LABEL = parse_locator(os.getenv('PASSWORD_STRENGTH_LABEL'), 'PASSWORD_STRENGTH_LABEL')
    SUCCESS_MESSAGE = parse_locator(os.getenv('SUCCESS_MESSAGE'), 'SUCCESS_MESSAGE')
    SUBMIT_BUTTON = parse_locator(os.getenv('SUBMIT_BUTTON'), 'SUBMIT_BUTTON')

    # Locators Account Page
    ACCOUNT_WELCOME_MESSAGE = parse_locator(os.getenv('ACCOUNT_WELCOME_MESSAGE'), 'ACCOUNT_WELCOME_MESSAGE')

    # Buscador de productos
    SEARCH_URL = os.getenv('SEARCH_URL') or BASE_URL  # opcional
    SEARCH_INPUT = parse_locator(os.getenv('SEARCH_INPUT'), 'SEARCH_INPUT')
    SEARCH_SUBMIT = parse_locator(os.getenv('SEARCH_SUBMIT'), 'SEARCH_SUBMIT')
    SEARCH_RESULT_TITLES = parse_locator(os.getenv('SEARCH_RESULT_TITLES'), 'SEARCH_RESULT_TITLES')

    # Locators Login Page
    USER_NAME_INPUT = parse_locator(os.getenv('USER_NAME_INPUT'), 'USER_NAME_INPUT')
    PASSWORD_INPUT_LOGIN = parse_locator(os.getenv('PASSWORD_INPUT'), 'PASSWORD_INPUT')
    LOGIN_BUTTON = parse_locator(os.getenv('LOGIN_BUTTON'), 'LOGIN_BUTTON')
    LOGIN_ERROR_MESSAGE = (
        parse_locator(os.getenv('LOGIN_ERROR_MESSAGE'), 'LOGIN_ERROR_MESSAGE')
        if os.getenv('LOGIN_ERROR_MESSAGE') else None
    )