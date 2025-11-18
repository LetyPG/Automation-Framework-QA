# English: Test to validate the account page after registration
# Spanish: Test para validar la página de cuenta después de la registro

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

# English: Register a user and validate that the account page loads correctly
# Spanish: Registrar un usuario y validar que la página de cuenta cargue correctamente

@pytest.mark.usefixtures("driver")
def test_account_page_after_registration(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_account_page_after_registration")
    
    logger.debug("Generating test user data")
    user = generate_user()
    logger.info(f"Generated user: {user['email']}")

    # Register (Registro)
    logger.info("Starting user registration process")
    form = FormSubmission(driver)
    logger.debug(f"Opening submission form at: {Configuration.SUBMISSION_URL}")
    form.open(Configuration.SUBMISSION_URL)
    
    logger.debug("Filling registration form")
    form.fill_name(user["first_name"])
    form.fill_last_name(user["last_name"])
    form.fill_email(user["email"])
    form.fill_password(user["password"])
    form.fill_confirm_password(user["confirm_password"])
    
    logger.debug("Submitting registration form")
    form.submit_form()

    # Validations (Validaciones)
    logger.info("Validating redirection to account page after registration")
    assert form.is_redirected_to_account_page(), "No se redirigió a Account tras registrar usuario"

    logger.info("Validating account page elements")
    account = AccountUser(driver)
    assert account.is_welcome_message_visible(), "No se visualiza el mensaje de bienvenida en la cuenta"
    assert_element_visible(driver, Configuration.ACCOUNT_WELCOME_MESSAGE)

    # Welcome message (Mensaje de bienvenida que suele contener el nombre o 'My Account')
    logger.info("Retrieving and validating welcome message text")
    welcome_text = account.get_welcome_message_text()
    logger.info(f"Welcome message text: '{welcome_text}'")
    
    assert any(keyword in welcome_text for keyword in ["My Account", "Mi cuenta", user["first_name"]]), (
        f"Unexpected welcome message: '{welcome_text}'"
    )
    
    logger.info("✓ Test passed: Account page loaded successfully after registration")
    logger.info("=" * 80)