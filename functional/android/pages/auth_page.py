from functional.android.PageFactory_android.find_accesibility_id import *

class AuthPage(Component):

    def __init__(self, value, valid_phone, valid_password):
        super().__init__(value)
        self.valid_phone = valid_phone
        self.valid_password = valid_password

    def authorize(self):
        self.find_acces_id('Logo')
        self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]').click()








auth_page = AuthPage(value=None, valid_phone=None,valid_password=None)
