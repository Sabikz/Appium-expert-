from functional.android.PageFactory_android.find_accesibility_id import *

class AuthPage(Component):

    def __init__(self, value, valid_phone, valid_password):
        super().__init__(value)
        self.driver = None
        self.valid_phone = valid_phone
        self.valid_password = valid_password

    def authorize(self):
        self.find_acces_id('Logo')
        self.is_clickable('logo_lang_button_kk')
        self.is_clickable('logo_lang_button_ru')




auth_page = AuthPage(value=None, valid_phone=None,valid_password=None)
