
# English: Test to validate the login
# Spanish: Test para validar el login

import os
import pytest
from pages.login import LoginPage
from utils.config import Configuration

"""
English: The test validates the success login if the credentials are present
Spanish: El test valida el login exitoso si las credenciales están presentes
Si no hay credenciales, se salta la prueba.

"""

@pytest.mark.usefixtures("driver")
def test_login_success_if_credentials_present(driver):

    username = Configuration.USERNAME
    password = Configuration.PASSWORD
    if not username or not password:
        pytest.skip("USERNAME/PASSWORD no configurados en .env; se omite login exitoso")

    page = LoginPage(driver)
    page.open_login()
    page.login(username, password)

    assert page.is_redirected_to_account(), "No se redirigió a la página de cuenta tras iniciar sesión"

# English: The test validates the negative login if the credentials are not present
# Spanish: El test valida el login negativo si las credenciales no están presentes

@pytest.mark.usefixtures("driver")
def test_login_negative_shows_error_if_configured(driver):
    if not Configuration.LOGIN_ERROR_MESSAGE:
        pytest.skip("LOGIN_ERROR_MESSAGE no configurado en .env; se omite prueba negativa de login")

    page = LoginPage(driver)
    page.open_login()
    page.login("invalid_user@example.com", "wrong_password")

    assert page.is_error_visible(), "No se visualizó el mensaje de error de login"
    error_text = page.get_error_text()

    assert error_text is not None and error_text != "", "El texto de error de login está vacío"