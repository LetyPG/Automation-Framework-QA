from utils.config import Configuration
from pages.base_actions import BaseActions  


#Clase que representa la página Create Account en Magento

class FormSubmission(BaseActions):
    
    def fill_name(self, name):
        self.send_keys(Configuration.FIRST_NAME_INPUT, name)

    def fill_last_name(self, name):
        self.send_keys(Configuration.LAST_NAME_INPUT, name)

    def fill_email(self, email):
        self.send_keys(Configuration.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.send_keys(Configuration.PASSWORD_INPUT, password)
    def fill_confirm_password(self, confirm_password):
        self.send_keys(Configuration.CONFIRM_PASSWORD_INPUT, confirm_password)
    
    def get_strength_label_text(self):
        return self.get_text(Configuration.PASSWORD_STRENGTH_LABEL)
    
    def is_redirected_to_account_page(self):
        return Configuration.ACCOUNT_URL in self.driver.current_url

    def is_success_message_displayed(self):
        return self.is_visible(Configuration.SUCCESS_MESSAGE)
    
    #def is_redirected_to_dashboard(self):
        #return self.is_visible(Config.DASHBOARD_HEADER)

 

    def submit_form(self):
        self.click(Configuration.SUBMIT_BUTTON)


  


        