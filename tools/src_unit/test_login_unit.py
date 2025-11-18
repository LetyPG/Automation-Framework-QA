import pytest
from pages.login import LoginPage
from utils.config import Configuration


def test_login_calls_and_redirect(monkeypatch, dummy_driver):
    calls = {"send_keys": [], "click": []}
    page = LoginPage(dummy_driver)

    # Monkeypatch BaseActions methods on the instance
    monkeypatch.setattr(page, "send_keys", lambda locator, text: calls["send_keys"].append((locator, text)))
    def fake_click(locator):
        calls["click"].append(locator)
        # Simulate redirect after clicking login
        dummy_driver.current_url = Configuration.ACCOUNT_URL
    monkeypatch.setattr(page, "click", fake_click)

    # Exercise
    page.login("foo@example.com", "secret")

    # Verify interactions
    assert calls["send_keys"] == [
        (Configuration.USER_NAME_INPUT, "foo@example.com"),
        (Configuration.PASSWORD_INPUT_LOGIN, "secret"),
    ]
    assert calls["click"] == [Configuration.LOGIN_BUTTON]

    # Verify redirect check
    assert page.is_redirected_to_account() is True


def test_login_negative_error_visible(monkeypatch, dummy_driver):
    page = LoginPage(dummy_driver)

    # Ensure error locator is present for unit test; if not, inject a default one
    if not getattr(Configuration, "LOGIN_ERROR_MESSAGE", None):
        monkeypatch.setattr(Configuration, "LOGIN_ERROR_MESSAGE", ("css", ".message-error"), raising=False)

    # Force error visible/text
    monkeypatch.setattr(page, "is_visible", lambda locator: True)
    monkeypatch.setattr(page, "get_text", lambda locator: "Invalid login or password.")

    assert page.is_error_visible() is True
    assert page.get_error_text() == "Invalid login or password."
