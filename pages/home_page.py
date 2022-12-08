from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#from pages.locators import home_page_locators as hpl
#import settings
from pages.base_page import BasePage
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from time import sleep

login_button = (By.XPATH, '//*[@id="header"]/a[1]')
user_email_after_enter = (By.LINK_TEXT, 'User380 [shevtanya2022@gmail.com]')
registration_form = (By.ID, 'registration-form')
registr_button = (By.XPATH, '//*[@id="header"]/a[2]')
exercises_button = (By.XPATH, '//*[@id="top-menu"]/a[4]')
programs_button = (By.XPATH, '//*[@id="top-menu"]/a[5]')
contacts_button = (By.XPATH, '//*[@id="top-menu"]/a[1]')
filters_exercises1 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[1]/label')
filters_exercises2 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[2]/label')
groups_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[1]')
groups_mini_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]')
filters_programs = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]')
contacts = (By.ID, 'contacts')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def check_username_and_email_displ_on_home_page(self):
        return self.find_element(user_email_after_enter).is_displayed()

    def registration_form_is_displayed(self):
        return self.find_element(registration_form).is_displayed()

    def registration_button_is_displayed(self):
        return self.find_element(registr_button)

    def go_to_login_page(self):
        return self.find_element(login_button).click()

    def go_to_exercises_page(self):
        return self.find_element(exercises_button).click()

    def check_exercises_page_opened(self):
        assert self.find_element(filters_exercises1).is_displayed()
        assert self.find_element(filters_exercises1).is_displayed()
        assert self.find_element(groups_exercises).is_displayed()
        assert self.find_element(groups_mini_exercises).is_displayed()

    def go_to_programs_page(self):
        return self.find_element(programs_button).click()

    def check_programs_page_opened(self):
        assert self.find_element(filters_programs).is_displayed()

    def go_contacts_form(self):
        return self.find_element(contacts_button).click()

    def check_contacts_form(self):
        assert self.find_element(contacts).is_displayed()
