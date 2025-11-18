
# English: Define the account user page controller with the specifics methods to interact with the account user page
# Spanish: Define el controlador de la página de cuenta de usuario con los métodos específicos para interactuar con la página de cuenta de usuario

from pages.base_actions import BaseActions
from utils.config import Configuration

"""
    English: Account user page controller with the specifics methods to interact with the account user page
    Spanish: Controlador de la página de cuenta de usuario con los métodos específicos para interactuar con la página de cuenta de usuario
    
"""

class AccountUser(BaseActions):
 
# English: Check if the welcome message is visible
# Spanish: Verificar si el mensaje de bienvenida es visible
    def is_welcome_message_visible(self) -> bool:
        return bool(self.is_visible(Configuration.ACCOUNT_WELCOME_MESSAGE))

# English: Get the welcome message text
# Spanish: Obtener el texto del mensaje de bienvenida
    def get_welcome_message_text(self) -> str:
        return self.get_text(Configuration.ACCOUNT_WELCOME_MESSAGE)
