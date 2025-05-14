# # Clase base con operaciones genéricas para todas las páginas
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
    """
    Controlador base para la interacción con el navegador web utilizando Selenium.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = self._set_wait()

    def _set_wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    #Navega hasta la URL
    def open(self, url):
        self.driver.get(url)
    
    #Espera y encuentra un elemento
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    #Hace clic en un elemento, click seguro esperando que sea clickable
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            element.click()
        except TimeoutException:
            raise Exception(f"Elemento no clickeable: {locator}")

    #Escribe en un input
    def send_keys(self, locator, text):
        input_field = self.find(locator)
        input_field.clear()
        input_field.send_keys(text)

    #Obtener texto visible de un elemento
    def get_text(self, locator):
        return self.find(locator).text

    #Verificar si un elemento es visible
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            return False

    #Hacer scroll hacia un elemento visible
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

   #Subir un archivo desde una ruta local
    def upload_file(self, locator, file_path):
        file_input = self.find(locator)
        file_input.send_keys(file_path)

    #actualizar la página
    def refresh_page(self):
        self.driver.refresh()

    #regresar a la página anterior
    def go_back(self):
        self.driver.back()

   #avanzar a la página siguiente
    def go_forward(self):
        self.driver.forward()

    def handle_window_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
    def handle_switch_to_window(self, window_title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == window_title:
                break
    def close(self):
        self.driver.quit()



   
  


    


    

