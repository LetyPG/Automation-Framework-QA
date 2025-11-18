# Unit test for AccountUser page object

from pages.page_account_user import AccountUser


def test_account_welcome_visibility_and_text(monkeypatch, dummy_driver):
    page = AccountUser(dummy_driver)

    # Simulate visibility and text
    monkeypatch.setattr(page, "is_visible", lambda locator: True)
    monkeypatch.setattr(page, "get_text", lambda locator: "My Account - Welcome Alice")

    assert page.is_welcome_message_visible() is True
    text = page.get_welcome_message_text()
    assert any(keyword in text for keyword in ["My Account", "Mi cuenta"])  # language agnostic
