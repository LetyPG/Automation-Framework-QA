
# Unit test for FormSubmission page object
from pages.page_form_submission import FormSubmission
from utils.config import Configuration


def test_form_submission_fills_and_submits(monkeypatch, dummy_driver):
    calls = {"send_keys": [], "click": []}

    page = FormSubmission(dummy_driver)

    # Monkeypatch BaseActions methods on the instance
    monkeypatch.setattr(page, "send_keys", lambda locator, text: calls["send_keys"].append((locator, text)))
    monkeypatch.setattr(page, "click", lambda locator: calls["click"].append(locator))
    monkeypatch.setattr(page, "get_text", lambda locator: "Strong")
    monkeypatch.setattr(page, "is_visible", lambda locator: True)

    # Exercise
    page.fill_name("Alice")
    page.fill_last_name("Smith")
    page.fill_email("alice@example.com")
    page.fill_password("P@ssw0rd!")
    page.fill_confirm_password("P@ssw0rd!")
    page.submit_form()

    # Verify send_keys calls
    assert calls["send_keys"] == [
        (Configuration.FIRST_NAME_INPUT, "Alice"),
        (Configuration.LAST_NAME_INPUT, "Smith"),
        (Configuration.EMAIL_INPUT, "alice@example.com"),
        (Configuration.PASSWORD_INPUT, "P@ssw0rd!"),
        (Configuration.CONFIRM_PASSWORD_INPUT, "P@ssw0rd!"),
    ]

    # Verify click call
    assert calls["click"] == [Configuration.SUBMIT_BUTTON]

    # Extra behavior checks
    assert page.get_strength_label_text() == "Strong"
    assert page.is_success_message_displayed() is True
