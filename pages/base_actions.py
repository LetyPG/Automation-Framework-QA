# English: Base class with generic operations for all pages
"""
Define methods that are reusable to encapsulate interaction logic 
with the browser and elements 
(click, write, wait, etc.). 
Supports the DRY (Don’t Repeat Yourself)
 and Single Responsibility (SRP) principles.

"""

# Spanish: Clase base con operaciones genéricas para todas las páginas
"""
Define métodos reutilizables que encapsulan lógica de interacción 
con el navegador y los elementos 
(hacer clic, escribir, esperar, etc.). 
Apoya el principio DRY (Don’t Repeat Yourself)
 y Responsabilidad Única (SRP).
 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = self._set_wait()

    def _set_wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def _as_by_locator(self, locator):
        """
        English: Normalizes the locator for Selenium.
        Spanish: Normaliza el locator para Selenium.
        - Si es una tupla (By, value) la retorna tal cual.
        - Si es un string, se asume como un CSS selector.
        """
        if isinstance(locator, tuple) and len(locator) == 2:
            return locator
        return (By.CSS_SELECTOR, locator)

    # English: Navigates to the URL
    # Spanish: Navega hasta la URL
    def open(self, url):
        self.driver.get(url)
    
    # English: Waits and finds an element
    # Spanish: Espera y encuentra un elemento
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(self._as_by_locator(locator)))

    # English: Clicks on an element, safe click waiting for it to be clickable
    # Spanish: Hace clic en un elemento, click seguro esperando que sea clickable
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self._as_by_locator(locator)))
            element.click()
        except TimeoutException:
            raise Exception(f"Elemento no clickeable: {locator}")

    # English: Types into an input field
    # Spanish: Escribe en un input
    def send_keys(self, locator, text):
        input_field = self.find(locator)
        input_field.clear()
        input_field.send_keys(text)

    # English: Obtains the visible text of an element
    # Spanish: Obtiene el texto visible de un elemento
    def get_text(self, locator):
        return self.find(locator).text

    # English: Verifies if an element is visible
    # Spanish: Verifica si un elemento es visible
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(self._as_by_locator(locator)))
        except TimeoutException:
            return False

    # English: Finds multiple elements
    # Spanish: Encontrar múltiples elementos
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(self._as_by_locator(locator)))

    # English: Obtains the list of texts of multiple elements
    # Spanish: Obtener lista de textos de múltiples elementos
    def get_texts(self, locator):
        elements = self.find_all(locator)
        return [el.text for el in elements]

    # English: Scrolls to an element
    # Spanish: Hacer scroll hacia un elemento visible
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

   # English: Uploads a file from a local path
   # Spanish: Subir un archivo desde una ruta local
    def upload_file(self, locator, file_path):
        file_input = self.find(locator)
        file_input.send_keys(file_path)

    # English: Refreshes the page
    # Spanish: Actualizar la página
    def refresh_page(self):
        self.driver.refresh()

    # English: Goes back to the previous page
    # Spanish: Regresar a la página anterior
    def go_back(self):
        self.driver.back()

    # English: Goes forward to the next page
    # Spanish: Avanzar a la página siguiente
    def go_forward(self):
        self.driver.forward()

    # English: Handles a window alert
    # Spanish: Maneja una alerta de ventana
    def handle_window_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
    
    # English: Handles a window switch
    # Spanish: Maneja el cambio de ventana
    def handle_switch_to_window(self, window_title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == window_title:
                break
    
    # English: Closes the driver
    # Spanish: Cierra el driver
    def close(self):
        self.driver.quit()
