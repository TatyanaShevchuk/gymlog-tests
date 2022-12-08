from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import settings
from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.home_page import HomePage
from pages.login_page import LoginPage


add_exercise = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div/div/div[1]/a')
all_field_for_add_exercise = (By.XPATH, '//*[@id="object-form"]/div/div[2]/div[1]')
my_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/aside/section/ul/li[5]')


class ExerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_my_exercise(self):
        self.driver.get(self.my_exercise_url)

    def my_exercises_is_displayed(self):
        self.driver.find_element(my_exercises)

    def my_exercises_button(self):
        self.driver.find_element(my_exercises).click()

    def add_exercise_is_displayed(self):
        return self.find_element(add_exercise)

    def add_exercise(self):
        return self.find_element(add_exercise).click()

    def all_field_for_add_exercise_is_displayed(self):
        return self.find_element(all_field_for_add_exercise)

    def all_field_for_add_exercise(self):
        return self.find_element(all_field_for_add_exercise).click()

