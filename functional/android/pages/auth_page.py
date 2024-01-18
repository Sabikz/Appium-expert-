import time

from functional.android.PageFactory_android.find_accesibility_id import *

class AuthPage(Component):

    def __init__(self, value, valid_phone, valid_password):
        super().__init__(value)
        self.valid_phone = valid_phone
        self.valid_password = valid_password

    def authorize(self):
        self.find_acces_id('Logo')
        lang_kz = self.find_xpath("//*[@resource-id='logo_lang_button_kk']")
        lang_ru = self.find_xpath("//*[@resource-id='logo_lang_button_ru']")
        lang_kz.click()

        '''Check main page'''
        sign_in = self.find_xpath("//*[@resource-id='sign_in_button']")
        self.find_acces_id('image description')
        search = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]')
        qr = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[1]')
        depo = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                               '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[2]')
        account_open = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                  '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[3]')
        account = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                  'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[4]')
        depo_open = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                    'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[5]')
        transfer = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[6]')
        my_bank = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                  'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]')
        news = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                               'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]')
        main = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                               'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]')
        add_but = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]')


        '''Check page My bank'''
        my_bank.click()
        self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout')
        back_but = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                      '/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]')
        number_phone = self.find_xpath("//*[@resource-id='ui_input_phone']")
        mask = number_phone.get_attribute('text')
        if mask == '+7 7':
            pass
        else:
            print("Mask not +7 7")
        del_number = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                      'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText/android.view.View/android.view.View[1]')
        continue_but = self.find_xpath("//*[@resource-id='ui_button_primary_normal']")
        back_but.click()

        '''Check page additional'''
        add_but.click()
        branch = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                 'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]')
        atm = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                              'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]')
        questions = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                    'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]')
        settings = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]')
        connection_bank = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                          'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]')

        connection_bank.click()

        self.find_acces_id('Navigation back button')
        short_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')
        short_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']")
        driver.press_keycode(4)
        driver.press_keycode(4)
        mobile_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                       '.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]')
        mobile_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']")
        driver.press_keycode(4)
        driver.press_keycode(4)
        bussines_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                         'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]')
        bussines_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']")
        driver.press_keycode(4)
        driver.press_keycode(4)
        self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]').click()






















auth_page = AuthPage(value=None, valid_phone=None,valid_password=None)
