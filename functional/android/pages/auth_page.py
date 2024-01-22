from functional.android.PageFactory_android.find_accesibility_id import *

class AuthPage(Component):
    def __init__(self, number=None, password=None):
        self.number = number
        self.password = password