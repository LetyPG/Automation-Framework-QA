
# English: Test to validate the login
# Spanish: Test para validar el login


import pytest
from src.pages.login import LoginPage
from utils.config import Configuration
from utils.logger import setup_logger

# English: Setup logger for this test module
# Spanish: Configurar logger para este módulo de test
logger = setup_logger(__name__)

"""
English: The test validates the success login if the credentials are present
Spanish: El test valida el login exitoso si las credenciales están presentes
Si no hay credenciales, se salta la prueba.

"""

@pytest.mark.usefixtures("driver")
def test_login_success_if_credentials_present(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_login_success_if_credentials_present")
    
    username = Configuration.USERNAME
    password = Configuration.PASSWORD
    if not username or not password:
        logger.warning("USERNAME/PASSWORD not configured in .env - Skipping successful login test")
        pytest.skip("USERNAME/PASSWORD no configurados en .env; se omite login exitoso")

    logger.info(f"Attempting login with username: {username}")
    page = LoginPage(driver)
    
    logger.debug("Opening login page")
    page.open_login()
    
    logger.debug("Performing login action")
    page.login(username, password)

    logger.info("Validating redirection to account page")
    assert page.is_redirected_to_account(), "No se redirigió a la página de cuenta tras iniciar sesión"
    
    logger.info("✓ Test passed: User successfully logged in and redirected to account page")
    logger.info("=" * 80)

# English: The test validates the negative login if the credentials are not present
# Spanish: El test valida el login negativo si las credenciales no están presentes

@pytest.mark.usefixtures("driver")
def test_login_negative_shows_error_if_configured(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_login_negative_shows_error_if_configured")
    
    if not Configuration.LOGIN_ERROR_MESSAGE:
        logger.warning("LOGIN_ERROR_MESSAGE not configured in .env - Skipping negative login test")
        pytest.skip("LOGIN_ERROR_MESSAGE no configurado en .env; se omite prueba negativa de login")

    logger.info("Testing negative login scenario with invalid credentials")
    page = LoginPage(driver)
    
    logger.debug("Opening login page")
    page.open_login()
    
    logger.debug("Attempting login with invalid credentials")
    page.login("invalid_user@example.com", "wrong_password")

    logger.info("Validating error message is visible")
    assert page.is_error_visible(), "No se visualizó el mensaje de error de login"
    
    error_text = page.get_error_text()
    logger.info(f"Error message displayed: '{error_text}'")
    
    logger.info("✓ Test passed: Error message correctly displayed for invalid credentials")
    logger.info("=" * 80)