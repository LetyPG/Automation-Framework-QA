
# English: Test to validate the form submission
# Spanish: Test para validar la envio del formulario
import pytest
from src.pages.page_form_submission import FormSubmission
from src.pages.page_account_user import AccountUser
from utils.config import Configuration
from utils.data_generator import generate_user
from utils.assertions import assert_element_visible
from utils.logger import setup_logger

# English: Setup logger for this test module
# Spanish: Configurar logger para este módulo de test
logger = setup_logger(__name__)

# English: First validates the registration process and then validates the account page
# Spanish: Primero valida el proceso de registro y luego valida la página de cuenta

@pytest.mark.usefixtures("driver")
def test_valid_submission(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_valid_submission")
    
    logger.debug("Generating test user data")
    user = generate_user()
    logger.info(f"Generated user: {user['email']}")

    page = FormSubmission(driver)
    logger.debug(f"Opening submission form at: {Configuration.SUBMISSION_URL}")
    page.open(Configuration.SUBMISSION_URL)

    logger.info("Filling out registration form")
    page.fill_name(user["first_name"])
    page.fill_last_name(user["last_name"])
    page.fill_email(user["email"])
    page.fill_password(user["password"])
    page.fill_confirm_password(user["confirm_password"])
    
    logger.debug("Submitting form")
    page.submit_form()

    # English: Validates that the user is redirected to the account page and that the success message is displayed
    # Spanish: Valida que el usuario sea redirigido a la página de cuenta y que se muestre el mensaje de éxito
    logger.info("Validating redirection to account page")
    assert page.is_redirected_to_account_page(), "No se redirigió a la página de cuenta de usuario"
    
    logger.info("Validating success message is displayed")
    assert page.is_success_message_displayed(), "No se mostró el mensaje de éxito"

    # English: Validates that the welcome message is visible in the account page
    # Spanish: Valida que el mensaje de bienvenida sea visible en la página de cuenta
    logger.info("Validating welcome message on account page")
    account = AccountUser(driver)
    assert account.is_welcome_message_visible(), "El mensaje de bienvenida no es visible en la cuenta"
    assert_element_visible(driver, Configuration.ACCOUNT_WELCOME_MESSAGE)
    
    logger.info("✓ Test passed: User registration successful with all validations")
    logger.info("=" * 80)


# English: Validates that the password strength label is displayed and has the expected value
# Spanish: Valida que el mensaje de fortaleza sea visible en la página de cuenta
def test_password_strength_label(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_password_strength_label")
    
    logger.debug("Generating test user data")
    user = generate_user()
    logger.info(f"Generated user: {user['email']}")
    
    page = FormSubmission(driver)
    logger.debug(f"Opening submission form at: {Configuration.SUBMISSION_URL}")
    page.open(Configuration.SUBMISSION_URL)
    
    logger.info("Filling form fields to trigger password strength indicator")
    page.fill_name(user["first_name"])
    page.fill_last_name(user["last_name"])
    page.fill_email(user["email"])
    page.fill_password(user["password"])
    page.fill_confirm_password(user["confirm_password"])

    # English: Validates that the password strength label is displayed and has the expected value
    # Spanish: Valida que el mensaje de fortaleza sea visible en la página de cuenta    
    logger.info("Retrieving password strength label")
    strength = page.get_strength_label_text()
    logger.info(f"Password strength displayed: '{strength}'")
    
    assert strength in ["Weak", "Moderate", "Strong", "Very Strong"], f"Etiqueta de fortaleza inesperada: {strength}"
    
    logger.info("✓ Test passed: Password strength label displayed correctly")
    logger.info("=" * 80)
