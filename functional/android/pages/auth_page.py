from functional.android.PageFactory_android.find_accesibility_id import TestFindByAccessibilityID


class AuthPage(TestFindByAccessibilityID):

    def __init__(self, value, valid_phone, valid_password):
        super().__init__()
        self.valid_phone = valid_phone
        self.valid_password = valid_password
        self.value = value

    def authorize(self, valid_phone, valid_password, value):
        self.find_id(value)
