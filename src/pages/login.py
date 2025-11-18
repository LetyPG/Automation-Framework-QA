# English: Define the login page controller with the specifics methods to interact with the login page
# Spanish: Define el controlador de la página de login con los métodos específicos para interactuar con la página de login


from src.pages.base_actions import BaseActions
from utils.config import Configuration

"""
    English: Magento Login Page Controller
    
    Spanish: Controlador de la página de login de Magento
   
"""

class LoginPage(BaseActions):
    
# English: Open the login page
# Spanish: Abrir la página de login
    def open_login(self):
        self.open(Configuration.LOGIN_URL)

# English: Fill the username
# Spanish: Llenar el nombre de usuario
    def fill_username(self, username: str):
        self.send_keys(Configuration.USER_NAME_INPUT, username)

# English: Fill the password
# Spanish: Llenar la contraseña
    def fill_password(self, password: str):
        self.send_keys(Configuration.PASSWORD_INPUT_LOGIN, password)

# English: Submit the login form
# Spanish: Enviar el formulario de login
    def submit(self):
        self.click(Configuration.LOGIN_BUTTON)

# English: Login with the given username and password
# Spanish: Iniciar sesión con el nombre de usuario y contraseña dados
    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

# English: Check if the user is redirected to the account page
# Spanish: Verificar si el usuario es redirigido a la página de cuenta
    def is_redirected_to_account(self) -> bool:
        return Configuration.ACCOUNT_URL in self.driver.current_url

# English: Check if the error message is visible
# Spanish: Verificar si el mensaje de error es visible
    def is_error_visible(self) -> bool:
        if Configuration.LOGIN_ERROR_MESSAGE:
            return bool(self.is_visible(Configuration.LOGIN_ERROR_MESSAGE))
        return False

# English: Get the error message text
# Spanish: Obtener el texto del mensaje de error
    def get_error_text(self) -> str:
        if Configuration.LOGIN_ERROR_MESSAGE:
            return self.get_text(Configuration.LOGIN_ERROR_MESSAGE)
        return ""