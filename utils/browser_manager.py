#SRP (Single Responsibility Principle): BrowserManager gestiona el navegador; 
# BaseActions interactúa con la página.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

class BrowserManager:
    def __init__(self, browser="chrome"):
        self.driver: WebDriver = self._start_driver(browser)

    def _start_driver(self, browser: str) -> WebDriver:
        if browser.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(service=ChromeService(), options=options)
        elif browser.lower() == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            return webdriver.Firefox(service=FirefoxService(), options=options)
        else:
            raise ValueError(f"Navegador no soportado: {browser}")