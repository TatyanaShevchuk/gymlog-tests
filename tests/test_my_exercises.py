from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep
import settings
from pages.my_exercises_page import ExerPage


def test_add_exercise(driver, user_logining):
    exer_page = ExerPage(driver)
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="solar"]/div[2]/aside/section/ul/li[5]').click()
    exer_page.add_exercise()
    assert exer_page.all_field_for_add_exercise_is_displayed()

