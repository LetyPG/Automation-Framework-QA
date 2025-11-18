# English: Define the search product page controller with the specifics methods to interact with the search product page
# Spanish: Define el controlador de la página de búsqueda de productos con los métodos específicos para interactuar con la página de búsqueda de productos

from src.pages.base_actions import BaseActions
from utils.config import Configuration

"""
    English: Search product page controller with the specifics methods to interact with the search product page
    Spanish: Controlador de la página de búsqueda de productos con los métodos específicos para interactuar con la página de búsqueda de productos
    
"""

class SearchProductPage(BaseActions):
   
# English: Open the search page
# Spanish: Abrir la página de búsqueda
    def open_search(self):
        self.open(Configuration.SEARCH_URL or Configuration.BASE_URL)

# English: Type the query
# Spanish: Escribir la consulta
    def type_query(self, query: str):
        self.send_keys(Configuration.SEARCH_INPUT, query)

# English: Submit the search
# Spanish: Enviar la búsqueda
    def submit_search(self):
        self.click(Configuration.SEARCH_SUBMIT)

# English: Search for a product
# Spanish: Buscar un producto
    def search(self, query: str):
        self.type_query(query)
        self.submit_search()

# English: Check if the results are visible
# Spanish: Verificar si los resultados son visibles
    def results_visible(self) -> bool:
        return bool(self.is_visible(Configuration.SEARCH_RESULT_TITLES))

# English: Get the results titles
# Spanish: Obtener los títulos de los resultados
    def get_results_titles(self):
        return self.get_texts(Configuration.SEARCH_RESULT_TITLES)
