from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import settings
from selenium.webdriver.common.keys import Keys
from time import sleep

login_email_button = (By.ID, 'email')
password_button = (By.ID, 'password')
entrance_button = (By.XPATH, '//*[@id="login-form"]/div[1]/div[4]/button')
remember_me = (By.XPATH, '//*[@id="login-form"]/div[1]/div[4]/label)')
vk = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[1]')
twitter = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[2]')
ok = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[3]')
instagram = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[4]')
facebook = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[5]')
user_login_email = (By.XPATH, '//*[@id="header"]/ul/li[1]/a')
allert_message = (By.XPATH, '//*[@id="login-form"]/div[1]/div[3]/div/div')
foget_password = (By.XPATH, '//*[@id="login-form"]/div[2]/div[2]/a[2]')
recovery_button = (By.XPATH, '//*[@id="recovery-form"]/div[1]/div[3]/button')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_logining(self):
        self.driver.get(self.login_url)

    def enter_login_data(self, email, password):
        self.find_element(login_email_button).send_keys(settings.email)
        self.find_element(password_button).send_keys(settings.password)
        sleep(5)
        self.find_element(entrance_button).click()

    def enter_incorrect_password(self, email, password):
        self.find_element(login_email_button).send_keys(settings.email)
        self.find_element(password_button).send_keys(settings.incorrect_password)
        sleep(5)
        self.find_element(entrance_button).click()

    def allert_message_is_displayed(self):
        return self.find_element(allert_message)

    def login_email_field_is_displayed(self):
        return self.find_element(login_email_button)

    def login_email_field(self):
        return self.find_element(login_email_button)

    def password_field_is_displayed(self):
        return self.find_element(password_button)

    def password_field(self):
        return self.find_element(password_button)

    def entrance_button_is_displayed(self):
        return self.find_element(entrance_button)

    def vk_is_displayed(self):
        return self.find_element(vk)

    def twitter_is_displayed(self):
        return self.find_element(twitter)

    def ok_is_displayed(self):
        return self.find_element(ok)

    def instagram_is_displayed(self):
        return self.find_element(instagram)

    def facebook_is_displayed(self):
        return self.find_element(facebook)

    def user_login_email_is_displayed(self):
        return self.find_element(user_login_email)

    def forget_password_is_displayed(self):
        return self.find_element(foget_password)

    def recovery_button_is_displayed(self):
        return self.find_element(recovery_button)
