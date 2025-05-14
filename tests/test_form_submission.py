import pytest
from pages.page_form_submission import FormSubmission
from utils.config import Configuration
from utils.data_generator import generate_user


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

    assert page.is_redirected_to_account_page()
    assert page.is_success_message_displayed()

def test_password_strength_label(driver):
    user = generate_user()
    page= FormSubmission(driver)
    page.open(Configuration.SUBMISSION_URL)
    page.fill_name(user["first_name"])
    page.fill_last_name(user["last_name"])
    page.fill_email(user["email"])
    page.fill_password(user["password"])
    page.fill_confirm_password(user["confirm_password"])
    
    strength = page.get_strength_label_text()
    assert strength in ["Weak", "Moderate", "Strong", "Very Strong"]



