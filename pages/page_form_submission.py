

# English: Define the form submission page controller with the specifics methods to interact with the form submission page
# Spanish: Define el controlador de la página de envío de formularios con los métodos específicos para interactuar con la página de envío de formularios
from utils.config import Configuration
from pages.base_actions import BaseActions  


# English: Class that represents the Create Account page in Magento
# Spanish: Clase que representa la página Create Account en Magento

class FormSubmission(BaseActions):
    
# English: Fill the name
# Spanish: Llenar el nombre
    def fill_name(self, name):
        self.send_keys(Configuration.FIRST_NAME_INPUT, name)

# English: Fill the last name
# Spanish: Llenar el apellido
    def fill_last_name(self, name):
        self.send_keys(Configuration.LAST_NAME_INPUT, name)

# English: Fill the email
# Spanish: Llenar el email
    def fill_email(self, email):
        self.send_keys(Configuration.EMAIL_INPUT, email)

# English: Fill the password
# Spanish: Llenar la contraseña
    def fill_password(self, password):
        self.send_keys(Configuration.PASSWORD_INPUT, password)

# English: Fill the confirm password
# Spanish: Llenar la confirmación de la contraseña
    def fill_confirm_password(self, confirm_password):
        self.send_keys(Configuration.CONFIRM_PASSWORD_INPUT, confirm_password)
    
# English: Get the strength label text
# Spanish: Obtener el texto de la etiqueta de la contraseña
    def get_strength_label_text(self):
        return self.get_text(Configuration.PASSWORD_STRENGTH_LABEL)
    
# English: Check if the user is redirected to the account page
# Spanish: Verificar si el usuario es redirigido a la página de cuenta
    def is_redirected_to_account_page(self):
        return Configuration.ACCOUNT_URL in self.driver.current_url

# English: Check if the success message is displayed
# Spanish: Verificar si el mensaje de éxito es mostrado
    def is_success_message_displayed(self):
        return self.is_visible(Configuration.SUCCESS_MESSAGE)
    
# English: Check if the user is redirected to the dashboard
# Spanish: Verificar si el usuario es redirigido a la página de dashboard
    def is_redirected_to_dashboard(self):
        return self.is_visible(Config.DASHBOARD_HEADER)

 
# English: Submit the form
# Spanish: Enviar el formulario
    def submit_form(self):
        self.click(Configuration.SUBMIT_BUTTON)


  


        