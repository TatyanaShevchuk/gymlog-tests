from pages.locators import login_page_locators as lpl
from pages.base_page import BasePage
import settings
from time import sleep


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_logining(self):
        self.driver.get(self.login_url)

    def enter_login_data(self, email, password):
        self.find_element(lpl.login_email_button).send_keys(settings.email)
        self.find_element(lpl.password_button).send_keys(settings.password)
        sleep(5)
        self.find_element(lpl.entrance_button).click()

    def enter_incorrect_data(self, email, password):
        self.find_element(lpl.login_email_button).send_keys(settings.email)
        self.find_element(lpl.password_button).send_keys(settings.incorrect_password)
        sleep(5)
        self.find_element(lpl.entrance_button).click()

    def enter_incorrect_password(self, email, password):
        self.find_element(lpl.login_email_button).send_keys(settings.email)
        self.find_element(lpl.password_button).send_keys(settings.incorrect_password)
        sleep(5)
        self.find_element(lpl.entrance_button).click()

    def allert_message_is_displayed(self):
        return self.find_element(lpl.allert_message)

    def login_email_field_is_displayed(self):
        return self.find_element(lpl.login_email_button)

    def login_email_field(self):
        return self.find_element(lpl.login_email_button)

    def password_field_is_displayed(self):
        return self.find_element(lpl.password_button)

    def password_field(self):
        return self.find_element(lpl.password_button)

    def entrance_button_is_displayed(self):
        return self.find_element(lpl.entrance_button)

    def vk_is_displayed(self):
        return self.find_element(lpl.vk)

    def twitter_is_displayed(self):
        return self.find_element(lpl.twitter)

    def ok_is_displayed(self):
        return self.find_element(lpl.ok)

    def instagram_is_displayed(self):
        return self.find_element(lpl.instagram)

    def facebook_is_displayed(self):
        return self.find_element(lpl.facebook)

    def user_login_email_is_displayed(self):
        return self.find_element(lpl.user_login_email)

    def forget_password_is_displayed(self):
        return self.find_element(lpl.foget_password)

    def recovery_button_is_displayed(self):
        return self.find_element(lpl.recovery_button)

    def logout(self):
        return self.find_element(lpl.logout_button).click()

    def after_logout(self):
        return self.find_element(lpl.login_button_icon)
