from pages.search_product_page import SearchProductPage
from utils.config import Configuration


def test_search_types_query_and_submits(monkeypatch, dummy_driver):
    calls = {"send_keys": [], "click": []}
    page = SearchProductPage(dummy_driver)

    monkeypatch.setattr(page, "send_keys", lambda locator, text: calls["send_keys"].append((locator, text)))
    monkeypatch.setattr(page, "click", lambda locator: calls["click"].append(locator))

    page.search("jacket")

    assert calls["send_keys"] == [(Configuration.SEARCH_INPUT, "jacket")]
    assert calls["click"] == [Configuration.SEARCH_SUBMIT]


def test_search_results_parsing(monkeypatch, dummy_driver):
    page = SearchProductPage(dummy_driver)

    # Simulate that results are visible and provide sample titles
    monkeypatch.setattr(page, "is_visible", lambda locator: True)
    monkeypatch.setattr(page, "get_texts", lambda locator: ["Warm Jacket", "Hoodie", "Running Jacket"]) 

    assert page.results_visible() is True
    titles = page.get_results_titles()
    assert any("jacket" in t.lower() for t in titles)
