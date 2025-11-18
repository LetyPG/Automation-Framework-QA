# English: Test to validate the search product
# Spanish: Test para validar la búsqueda de productos

import pytest
from src.pages.search_product_page import SearchProductPage
from utils.config import Configuration
from utils.logger import setup_logger

# English: Setup logger for this test module
# Spanish: Configurar logger para este módulo de test
logger = setup_logger(__name__)

# English: The test first opens the base URL and then searches for the product, asserts that the results are visible and that the search term is present in the results
# Spanish: El test primero abre la URL base y luego busca el producto, asertando que los resultados son visibles y que el término de búsqueda está presente en los resultados


@pytest.mark.usefixtures("driver")
def test_search_products_shows_results(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_search_products_shows_results")
    
    page = SearchProductPage(driver)
    logger.debug(f"Opening base URL: {Configuration.BASE_URL}")
    page.open(Configuration.BASE_URL)

    query = "jacket"
    logger.info(f"Performing search with query: '{query}'")
    page.search(query)

    logger.info("Validating search results are visible")
    assert page.results_visible(), "No se visualizaron resultados de búsqueda"

    logger.debug("Retrieving search result titles")
    titles = [t.lower() for t in page.get_results_titles() if t]
    logger.info(f"Found {len(titles)} results")
    logger.debug(f"First 5 titles: {titles[:5]}")
    
    assert any(query in t for t in titles), (
        f"Ningún resultado parece contener el término '{query}'. Títulos: {titles[:5]}"
    )
    
    logger.info(f"✓ Test passed: Search results contain the term '{query}'")
    logger.info("=" * 80)

@pytest.mark.usefixtures("driver")
def test_search_specific_product(driver):
    logger.info("=" * 80)
    logger.info("Starting test: test_search_specific_product")
    
    page = SearchProductPage(driver)
    logger.debug(f"Opening base URL: {Configuration.BASE_URL}")
    page.open(Configuration.BASE_URL)

    query = "jacket"
    logger.info(f"Performing search with query: '{query}'")
    page.search(query)

    logger.info("Validating search results are visible")
    assert page.results_visible(), "No se visualizaron resultados de búsqueda"

    logger.debug("Retrieving and analyzing search result titles")
    titles = [t.lower() for t in page.get_results_titles() if t]
    logger.info(f"Found {len(titles)} results")
    logger.debug(f"First 5 titles: {titles[:5]}")
    
    try:
        assert any(query in t for t in titles), (
            f"Ningún resultado parece contener el término '{query}'. Títulos: {titles[:5]}"
        )
        logger.info(f"✓ Test passed: Specific product search successful for '{query}'")
    except AssertionError as e:
        logger.error(f"✗ Test failed: {str(e)}")
        pytest.fail(str(e))
    
    logger.info("=" * 80)