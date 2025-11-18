"""
English Version:
This file is used to run unit tests for page objects (no real browser).
It seeds a minimal env so utils.config.parse_locator does not raise.

Spanish Version:
Este archivo se utiliza para ejecutar pruebas unitarias para objetos de página (sin navegador real).
Se semilla un entorno mínimo para que utils.config.parse_locator no lance una excepción.

"""

import os
import importlib
import pytest
import sys
import types

"""
English Version:
Seed minimal env so utils.config.parse_locator does not raise

Spanish Version:
Utilliza un entorno mínimo para que utils.config.parse_locator no lance una excepción.
"""
DEFAULT_ENV = {
    # URLs
    "BASE_URL": "https://example.test/",
    "LOGIN_URL": "https://example.test/login",
    "SUBMISSION_URL": "https://example.test/register",
    "ACCOUNT_URL": "https://example.test/account",
    # Form Submission locators
    "FORM_NAME": "css,#firstname",
    "FORM_LAST_NAME": "css,#lastname",
    "FORM_EMAIL": "css,#email_address",
    "FORM_PASSWORD": "css,#password",
    "FORM_CONFIRMATION_PASSWORD": "css,#password-confirmation",
    "PASSWORD_STRENGTH_LABEL": "css,.password-strength-meter > .label",
    "SUCCESS_MESSAGE": "css,.message-success",
    "SUBMIT_BUTTON": "css,button.action.submit.primary",
    # Account locators
    "ACCOUNT_WELCOME_MESSAGE": "css,.page-title span",
    # Search locators
    "SEARCH_INPUT": "css,#search",
    "SEARCH_SUBMIT": "css,button.action.search",
    "SEARCH_RESULT_TITLES": "css,.product-item-name a",
    # Login locators
    "USER_NAME_INPUT": "css,#email",
    "PASSWORD_INPUT": "css,#pass",
    "LOGIN_BUTTON": "css,#send2",
}

# Code logic Explanation:

"""
English Version:
Set default environment variables
os.environ.setdefault(k, v) sets the environment variable k to v if it is not already set
If the environment variable is already set, it will not be changed

Spanish Version:
Establece variables de entorno por defecto
os.environ.setdefault(k, v) establece la variable de entorno k a v si no está ya establecida
Si la variable de entorno ya está establecida, no se cambiará
"""

for k, v in DEFAULT_ENV.items():
    os.environ.setdefault(k, v)

"""
English Version:
Provide a dummy 'dotenv' module if python-dotenv is not installed
so that 'from dotenv import load_dotenv' in utils.config works in unit tests.

Spanish Version:
Proporciona un módulo 'dotenv' dummy si python-dotenv no está instalado
para que 'from dotenv import load_dotenv' en utils.config funcione en pruebas unitarias.
"""
try:
    import dotenv  # type: ignore  # noqa: F401
except ModuleNotFoundError:
    dummy_dotenv = types.ModuleType("dotenv")
    def _noop(*args, **kwargs):
        return None
    dummy_dotenv.load_dotenv = _noop
    sys.modules["dotenv"] = dummy_dotenv

"""
English Version:
Provide a dummy 'selenium' package so imports in utils.config and pages.base_actions
work during unit tests without installing selenium.

Spanish Version:
Proporciona un paquete 'selenium' dummy para que las importaciones en utils.config y pages.base_actions
funcionen durante las pruebas unitarias sin instalar selenium.
"""
try:
    import selenium  # type: ignore  # noqa: F401
except ModuleNotFoundError:
    selenium_mod = types.ModuleType("selenium")
    sys.modules["selenium"] = selenium_mod

    # selenium.common.exceptions
    common_mod = types.ModuleType("selenium.common")
    exceptions_mod = types.ModuleType("selenium.common.exceptions")
    class TimeoutException(Exception):
        pass
    exceptions_mod.TimeoutException = TimeoutException
    sys.modules["selenium.common"] = common_mod
    sys.modules["selenium.common.exceptions"] = exceptions_mod

    # selenium.webdriver.common.by
    webdriver_mod = types.ModuleType("selenium.webdriver")
    webdriver_common_mod = types.ModuleType("selenium.webdriver.common")
    by_mod = types.ModuleType("selenium.webdriver.common.by")
    class By:
        ID = "id"
        NAME = "name"
        XPATH = "xpath"
        CSS_SELECTOR = "css"
        CLASS_NAME = "class"
        TAG_NAME = "tag"
        LINK_TEXT = "link"
        PARTIAL_LINK_TEXT = "plink"
    by_mod.By = By
    sys.modules["selenium.webdriver"] = webdriver_mod
    sys.modules["selenium.webdriver.common"] = webdriver_common_mod
    sys.modules["selenium.webdriver.common.by"] = by_mod

    # English: selenium.webdriver.remote.webdriver, this is a placeholder for typing WebDriver and allows to avoid import errors
    # Spanish: selenium.webdriver.remote.webdriver, esto es un placeholder para typing WebDriver y permite evitar errores de importación
    webdriver_remote_mod = types.ModuleType("selenium.webdriver.remote")
    webdriver_remote_webdriver_mod = types.ModuleType("selenium.webdriver.remote.webdriver")
    class WebDriver:  # placeholder for typing
        pass
    webdriver_remote_webdriver_mod.WebDriver = WebDriver
    sys.modules["selenium.webdriver.remote"] = webdriver_remote_mod
    sys.modules["selenium.webdriver.remote.webdriver"] = webdriver_remote_webdriver_mod

    # selenium.webdriver.support.ui.WebDriverWait
    support_mod = types.ModuleType("selenium.webdriver.support")
    support_ui_mod = types.ModuleType("selenium.webdriver.support.ui")
    class WebDriverWait:
        def __init__(self, driver, timeout):
            self.driver = driver
            self.timeout = timeout
        def until(self, method, message=None):
            # No-op for unit tests; monkeypatched page methods handle behavior
            return True
    support_ui_mod.WebDriverWait = WebDriverWait

    # selenium.webdriver.support.expected_conditions as EC
    support_ec_mod = types.ModuleType("selenium.webdriver.support.expected_conditions")
    def _return_arg(arg):
        # Our dummy WebDriverWait.until just returns True; conditions are placeholders
        return arg
    support_ec_mod.presence_of_element_located = _return_arg
    support_ec_mod.element_to_be_clickable = _return_arg
    support_ec_mod.visibility_of_element_located = _return_arg

    sys.modules["selenium.webdriver.support"] = support_mod
    sys.modules["selenium.webdriver.support.ui"] = support_ui_mod
    sys.modules["selenium.webdriver.support.expected_conditions"] = support_ec_mod

# Reload utils.config to re-evaluate Configuration with seeded env
import utils.config as cfg
importlib.reload(cfg)

# Monkeypatch BaseActions wait creation to avoid constructing Selenium WebDriverWait
import pages.base_actions as base_actions
base_actions.BaseActions._set_wait = lambda self, timeout=10: object()


class DummyDriver:
    def __init__(self, current_url: str = "https://example.test/"):
        self.current_url = current_url


@pytest.fixture
def dummy_driver():
    return DummyDriver()
