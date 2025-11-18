
# English: Test to validate the form submission
# Spanish: Test para validar la envio del formulario
import pytest
from pages.page_form_submission import FormSubmission
from pages.page_account_user import AccountUser
from utils.config import Configuration
from utils.data_generator import generate_user
from utils.assertions import assert_element_visible


# English: First validates the registration process and then validates the account page
# Spanish: Primero valida el proceso de registro y luego valida la página de cuenta

@pytest.mark.usefixtures("driver")
def test_valid_submission(driver):
    user = generate_user()

    page = FormSubmission(driver)
    page.open(Configuration.SUBMISSION_URL)

    page.fill_name(user["first_name"])
    page.fill_last_name(user["last_name"])
    page.fill_email(user["email"])
    page.fill_password(user["password"])
    page.fill_confirm_password(user["confirm_password"])
    page.submit_form()

    # English: Validates that the user is redirected to the account page and that the success message is displayed
    # Spanish: Valida que el usuario sea redirigido a la página de cuenta y que se muestre el mensaje de éxito
    assert page.is_redirected_to_account_page(), "No se redirigió a la página de cuenta de usuario"
    assert page.is_success_message_displayed(), "No se mostró el mensaje de éxito"

    # English: Validates that the welcome message is visible in the account page
    # Spanish: Valida que el mensaje de bienvenida sea visible en la página de cuenta
    account = AccountUser(driver)
    assert account.is_welcome_message_visible(), "El mensaje de bienvenida no es visible en la cuenta"
    assert_element_visible(driver, Configuration.ACCOUNT_WELCOME_MESSAGE)


# English: Validates that the password strength label is displayed and has the expected value
# Spanish: Valida que el mensaje de fortaleza sea visible en la página de cuenta
def test_password_strength_label(driver):
    user = generate_user()
    page = FormSubmission(driver)
    page.open(Configuration.SUBMISSION_URL)
    page.fill_name(user["first_name"])
    page.fill_last_name(user["last_name"])
    page.fill_email(user["email"])
    page.fill_password(user["password"])
    page.fill_confirm_password(user["confirm_password"])

    # English: Validates that the password strength label is displayed and has the expected value
    # Spanish: Valida que el mensaje de fortaleza sea visible en la página de cuenta    
    strength = page.get_strength_label_text()
    assert strength in ["Weak", "Moderate", "Strong", "Very Strong"], f"Etiqueta de fortaleza inesperada: {strength}"
