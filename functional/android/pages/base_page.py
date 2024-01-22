import time
from functional.android.PageFactory_android.find_accesibility_id import *

class BasePage(Component):

    def __init__(self, value=None, lng=None):
        self.lng = lng
        super().__init__(value)

    def main_page(self, driver, lng):
        self.find_acces_id('Logo', driver)
        if lng == 'kz':
            lang_kz = self.find_xpath("//*[@resource-id='logo_lang_button_kk']", driver)
            lang_kz.click()
        else:
            lang_ru = self.find_xpath("//*[@resource-id='logo_lang_button_ru']", driver)
            lang_ru.click()

        '''Check main page'''
        sign_in = self.find_xpath("//*[@resource-id='sign_in_button']", driver)
        self.find_acces_id('image description', driver)
        search = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]', driver)
        qr = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[1]', driver)
        depo = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                               '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[2]', driver)
        account_open = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                  '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[3]', driver)
        account = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                  'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[4]', driver)
        depo_open = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                    'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[5]', driver)
        transfer = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View[6]', driver)
        my_bank = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                  'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]', driver)
        news = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                               'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]', driver)
        main = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                               'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]', driver)
        add_but = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]', driver)


        '''Check page My bank'''
        my_bank.click()
        self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout', driver)
        back_but = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                      '/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]', driver)
        number_phone = self.find_xpath("//*[@resource-id='ui_input_phone']", driver)
        mask = number_phone.get_attribute('text')
        if mask == '+7 7':
            pass
        else:
            print("Mask not +7 7")
        del_number = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                      'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText/android.view.View/android.view.View[1]', driver)
        continue_but = self.find_xpath("//*[@resource-id='ui_button_primary_normal']", driver)
        back_but.click()

        '''Check page additional'''
        add_but.click()
        branch = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                 'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]', driver)
        atm = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                              'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]', driver)
        questions = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                    'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]', driver)
        settings = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]', driver)
        connection_bank = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                          'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]', driver)

        connection_bank.click()

        self.find_acces_id('Navigation back button', driver)
        short_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                   'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]', driver)
        short_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']", driver)
        driver.press_keycode(4)
        driver.press_keycode(4)
        mobile_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                       '.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]', driver)
        mobile_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']", driver)
        driver.press_keycode(4)
        driver.press_keycode(4)
        bussines_phone = self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                         'FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]', driver)
        bussines_phone.click()
        self.find_xpath("//*[@resource-id='com.samsung.android.dialer:id/digits']", driver)
        driver.press_keycode(4)
        driver.press_keycode(4)
        self.find_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]', driver).click()

base_page = BasePage()




















