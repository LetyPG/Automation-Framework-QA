# English: BrowserManager centralizes WebDriver startup logic (single responsibility)
# Spanish: BrowserManager centraliza la lógica de arranque del WebDriver (responsabilidad única)

"""
English:
This module starts a Selenium WebDriver with good defaults. It favors Selenium Manager
(built into Selenium 4.6+) so you do NOT need to manually manage a local driver
binary. If you still want to provide a local driver, you can do so via environment
variables.

Spanish:
Este módulo inicia un WebDriver de Selenium con buenas configuraciones por defecto.
Privilegia Selenium Manager (incluido en Selenium 4.6+), por lo que NO necesitas
administrar manualmente un ejecutable de driver local. Si aún deseas proporcionar
un driver local, puedes hacerlo mediante variables de entorno.

Key points / Puntos clave:
- Chrome/Firefox supported with options (headless optional)
- Sensible defaults (maximize/size, timeouts)
- Optional local driver path if provided (otherwise Selenium Manager picks it)
- Designed to be simple for tests and clear for learning purposes

"""

from __future__ import annotations

import os
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserManager:
    """
    English:
    Small helper that encapsulates WebDriver creation. It reads environment variables
    for optional customization and applies sensible defaults.

    Spanish:
    Pequeño helper que encapsula la creación del WebDriver. Lee variables de entorno
    para personalización opcional y aplica valores por defecto razonables.

    Environment variables (opcionales):
    - BROWSER: chrome|firefox (default: chrome)
    - HEADLESS: true|false (default: false)
    - CHROME_BINARY: path to custom Chrome/Chromium binary
    - FIREFOX_BINARY: path to custom Firefox binary
    - CHROME_DRIVER_PATH: path to a chromedriver binary (if you insist on manual driver)
    - FIREFOX_DRIVER_PATH: path to a geckodriver binary (manual driver)
    - WINDOW_WIDTH / WINDOW_HEIGHT: window size when not headless (firefox); chrome is maximized by default
    - IMPLICIT_WAIT: seconds (default: 2)
    - PAGELOAD_TIMEOUT: seconds (default: 30)

    Note:
    - On Linux, a file like driver/chromedriver.exe is a Windows binary and will not be used.
      Prefer Selenium Manager or provide a Linux-compatible driver path.
    """

    def __init__(self, browser: Optional[str] = None, headless: Optional[bool] = None):
        self._browser = (browser or os.getenv("BROWSER") or "chrome").lower()
        self._headless = (
            (str(headless).lower() if headless is not None else os.getenv("HEADLESS", "false"))
            in ("1", "true", "yes")
        )
        self.driver: WebDriver = self._start_driver(self._browser)

    # English: Public accessor in case tests want to grab the driver
    # Spanish: Accesor público por si los tests necesitan obtener el driver
    @property
    def instance(self) -> WebDriver:
        return self.driver

    def _start_driver(self, browser: str) -> WebDriver:
        if browser == "chrome":
            options = self._build_chrome_options()
            # English: If CHROME_DRIVER_PATH is provided, use it; otherwise Selenium Manager picks a driver
            # Spanish: Si CHROME_DRIVER_PATH está definido, úsalo; de lo contrario Selenium Manager elige un driver
            chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
            service = ChromeService(executable_path=chrome_driver_path) if chrome_driver_path else ChromeService()
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            options = self._build_firefox_options()
            firefox_driver_path = os.getenv("FIREFOX_DRIVER_PATH")
            service = FirefoxService(executable_path=firefox_driver_path) if firefox_driver_path else FirefoxService()
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Navegador no soportado / Unsupported browser: {browser}")

        self._apply_timeouts_and_window(driver)
        return driver

    # --------------------------
    # Options builders / Constructores de opciones
    # --------------------------
    def _build_chrome_options(self) -> ChromeOptions:
        options = ChromeOptions()
        if self._headless:
            options.add_argument("--headless=new")  # modern headless
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        # Custom binary if provided
        chrome_binary = os.getenv("CHROME_BINARY")
        if chrome_binary:
            options.binary_location = chrome_binary

        # Common stability flags
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    def _build_firefox_options(self) -> FirefoxOptions:
        options = FirefoxOptions()
        if self._headless:
            options.add_argument("-headless")
        else:
            # For Firefox we set explicit size when not headless
            width = os.getenv("WINDOW_WIDTH", "1920")
            height = os.getenv("WINDOW_HEIGHT", "1080")
            options.set_preference("layout.css.devPixelsPerPx", "1.0")
            # Size will be applied after driver creation as well
            self._ff_size = (int(width), int(height))

        firefox_binary = os.getenv("FIREFOX_BINARY")
        if firefox_binary:
            options.binary_location = firefox_binary
        return options

    # --------------------------
    # Window and timeouts / Ventana y timeouts
    # --------------------------
    def _apply_timeouts_and_window(self, driver: WebDriver) -> None:
        # Timeouts
        implicit_wait = float(os.getenv("IMPLICIT_WAIT", "2"))
        page_load_timeout = float(os.getenv("PAGELOAD_TIMEOUT", "30"))
        driver.implicitly_wait(implicit_wait)
        driver.set_page_load_timeout(page_load_timeout)

        # Window sizing for Firefox when not headless
        if self._browser == "firefox" and not self._headless:
            width = int(os.getenv("WINDOW_WIDTH", "1920"))
            height = int(os.getenv("WINDOW_HEIGHT", "1080"))
            try:
                driver.set_window_size(width, height)
            except Exception:
                # Some drivers/platforms might not support it, fail softly
                pass

        # Note: Chrome is already maximized by option when not headless