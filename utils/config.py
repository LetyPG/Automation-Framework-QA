## Configuraciones generales y carga de variables desde .env
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


def parse_locator(env_value,var_name=None):
    """Convierte 'css,#id' en (By.CSS_SELECTOR, '#id')"""
    print(f"[DEBUG] var_name: {var_name}, env_value: {env_value}")

    if not env_value:
        raise ValueError("El valor del locator está vacío o no definido en el archivo .env")
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

    #Locators Page Submission
    FIRST_NAME_INPUT = parse_locator(os.getenv('FORM_NAME'))
    LAST_NAME_INPUT = parse_locator(os.getenv('FORM_LAST_NAME'))
    EMAIL_INPUT = parse_locator(os.getenv('FORM_EMAIL'))
    PASSWORD_INPUT = parse_locator(os.getenv('FORM_PASSWORD'))
    CONFIRM_PASSWORD_INPUT = parse_locator(os.getenv('FORM_CONFIRMATION_PASSWORD'))
    PASSWORD_STRENGTH_LABEL = parse_locator(os.getenv("PASSWORD_STRENGTH_LABEL"))
    SUCCESS_MESSAGE = parse_locator(os.getenv('SUCCESS_MESSAGE'))
    SUBMIT_BUTTON = parse_locator(os.getenv('SUBMIT_BUTTON'))
    
    # Locators Login Page n
    """
    USER_NAME_INPUT = parse_locator(os.getenv('USER_NAME_INPUT'))
    PASSWORD_INPUT = parse_locator(os.getenv('PASSWORD_INPUT'))
    LOGIN_BUTTON = parse_locator(os.getenv('LOGIN_BUTTON'))
    """
    