# English: Test to validate the account page after registration
# Spanish: Test para validar la página de cuenta después de la registro

import pytest
from pages.page_form_submission import FormSubmission
from pages.page_account_user import AccountUser
from utils.config import Configuration
from utils.data_generator import generate_user
from utils.assertions import assert_element_visible


# English: Register a user and validate that the account page loads correctly
# Spanish: Registrar un usuario y validar que la página de cuenta cargue correctamente

@pytest.mark.usefixtures("driver")
def test_account_page_after_registration(driver):
    user = generate_user()

    # Register (Registro)
    form = FormSubmission(driver)
    form.open(Configuration.SUBMISSION_URL)
    form.fill_name(user["first_name"])
    form.fill_last_name(user["last_name"])
    form.fill_email(user["email"])
    form.fill_password(user["password"])
    form.fill_confirm_password(user["confirm_password"])
    form.submit_form()

    # Validations (Validaciones)
    assert form.is_redirected_to_account_page(), "No se redirigió a Account tras registrar usuario"

    account = AccountUser(driver)
    assert account.is_welcome_message_visible(), "No se visualiza el mensaje de bienvenida en la cuenta"
    assert_element_visible(driver, Configuration.ACCOUNT_WELCOME_MESSAGE)

    # Welcome message (Mensaje de bienvenida que suele contener el nombre o 'My Account')
    welcome_text = account.get_welcome_message_text()
    assert any(keyword in welcome_text for keyword in ["My Account", "Mi cuenta", user["first_name"]]), (
        f"Unexpected welcome message: '{welcome_text}'"
    )