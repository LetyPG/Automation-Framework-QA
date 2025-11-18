# Pytest fixtures: such as driver, setup, teardown, log information, the fixtures for pytest is an object that is passed to the test function and is reused  in all the tests
# Fixtures de Pytest: navegador, setup, teardown, log information, 'fixtures' para pyest son objetos que se pasan a la funcion de test y se reutilizan en todos los tests
import pytest
from utils.logger import logger


@pytest.fixture(scope="function")
def driver(request):
    """Fixture de WebDriver para pruebas de integración (usa Selenium).
    La importación de BrowserManager es perezosa para evitar requerir Selenium
    cuando se ejecutan únicamente pruebas unitarias en tools/.
    """
    try:
        # Importación perezosa: evita fallar al cargar si Selenium no está instalado
        from utils.browser_manager import BrowserManager  # type: ignore
    except ModuleNotFoundError as e:
        pytest.skip(
            "Selenium no está instalado. Esta fixture 'driver' es solo para pruebas de integración. "
            "Ejecute 'pip install -r requirements.txt' o ejecute únicamente pruebas unitarias en tools/."
        )
        raise e  # no debería alcanzarse por el skip, pero mantiene el flujo de tipos

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