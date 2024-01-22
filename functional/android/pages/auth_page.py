from functional.android.PageFactory_android.find_accesibility_id import *

class AuthPage(Component):
    def __init__(self, value=None, number=None, password=None):
        self.number = number
        self.password = password
        super().__init__(value)

    def sign_up(self,driver):
        pass
