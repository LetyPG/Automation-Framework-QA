#  # Soft/hard assertions, comparaciones personalizadas
from selenium.common.exceptions import NoSuchElementException
class AssertionError(Exception):
    pass

def assert_element_displayed(element, message="Elemento no visible"):
    assert element.is_displayed(), message
from selenium.common.exceptions import NoSuchElementException

def assert_text_equals(actual, expected, message=None):
    assert actual == expected, message or f"Texto esperado: '{expected}', pero fue: '{actual}'"

def assert_element_visible(driver, locator, message=None):
    try:
        element = driver.find_element(*locator)
        assert element.is_displayed(), message or f"El elemento {locator} no está visible."
    except NoSuchElementException:
        raise AssertionError(message or f"Elemento no encontrado: {locator}")

def assert_element_contains_text(driver, locator, expected_text, message=None):
    try:
        element = driver.find_element(*locator)
        actual = element.text.strip()
        assert expected_text in actual, message or f"'{expected_text}' no está en el texto del elemento: '{actual}'"
    except NoSuchElementException:
        raise AssertionError(message or f"Elemento no encontrado: {locator}")

def assert_element_not_visible(driver, locator, message=None):
    try:
        element = driver.find_element(*locator)
        assert not element.is_displayed(), message or f"El elemento {locator} debería estar oculto, pero está visible."
    except NoSuchElementException:
        # Si no existe, también está oculto → pasa la validación
        pass

def assert_element_exists(driver, locator, message=None):
    try:
        driver.find_element(*locator)
    except NoSuchElementException:
        raise AssertionError(message or f"Elemento esperado no existe: {locator}")
