

# English: Test to validate the search product
# Spanish: Test para validar la búsqueda de productos

import pytest
from pages.search_product_page import SearchProductPage
from utils.config import Configuration

# English: The test first opens the base URL and then searches for the product, asserts that the results are visible and that the search term is present in the results
# Spanish: El test primero abre la URL base y luego busca el producto, asertando que los resultados son visibles y que el término de búsqueda está presente en los resultados


@pytest.mark.usefixtures("driver")
def test_search_products_shows_results(driver):
    page = SearchProductPage(driver)
    page.open(Configuration.BASE_URL)

    query = "jacket"
    page.search(query)

    assert page.results_visible(), "No se visualizaron resultados de búsqueda"

    titles = [t.lower() for t in page.get_results_titles() if t]
    assert any(query in t for t in titles), (
        f"Ningún resultado parece contener el término '{query}'. Títulos: {titles[:5]}"
    )

@pytest.mark.usefixtures("driver")
def test_search_specific_product(driver):
    page = SearchProductPage(driver)
    page.open(Configuration.BASE_URL)

    query = "jacket"
    page.search(query)

    assert page.results_visible(), "No se visualizaron resultados de búsqueda"

    titles = [t.lower() for t in page.get_results_titles() if t]
    assert any(query in t for t in titles), (
        f"Ningún resultado parece contener el término '{query}'. Títulos: {titles[:5]}"
    )
    try:
        assert any(query in t for t in titles), (
            f"Ningún resultado parece contener el término '{query}'. Títulos: {titles[:5]}"
        )
    except AssertionError as e:
        pytest.fail(str(e))