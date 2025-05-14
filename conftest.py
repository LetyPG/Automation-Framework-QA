## Fixtures de Pytest: navegador, setup, teardown, log information
import pytest
from utils.browser_manager import BrowserManager
from utils.logger import logger

@pytest.fixture(scope="function")
def driver(request):
    #browser = request.config.getoption("--browser")  # parámetro desde CLI (opcional)
    # Si no se pasa --browser, usa "chrome"
    browser = request.config.getoption("--browser") or "chrome"

    logger.info(f"Iniciando navegador: {browser}")
    
    manager = BrowserManager(browser)
    driver = manager.driver
    yield driver
    
    logger.info("Cerrando navegador...")
    driver.quit()

# Para permitir pasar --browser desde CLI (Ejemplo browser=firefox)
#pytest tests/test_login.py --browser=firefox
#Si no pasas nada, usará "chrome" por defecto (como se define en BrowserManager).
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador a usar: chrome o firefox"
    )