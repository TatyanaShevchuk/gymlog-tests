from pages.home_page import HomePage
from pages.stretching_page import StretchingPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.mark.stretching
def test_logining_going_to_stretching(driver, user_logining):
    login_page = LoginPage(driver)
    sleep(5)
    stretching_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/a[4]')
    stretching_button.click()
    exercise_button = driver.find_element(By.XPATH, '//*[@id="top-menu"]/a[4]')
    exercise_button.click()
    assert login_page.user_login_email_is_displayed()
    assert driver.find_element(By.CLASS_NAME, 'last')
    assert driver.find_element(By.ID, 'top-menu')
    assert driver.find_element(By.CLASS_NAME, 'catalog-filters')
    assert driver.find_element(By.XPATH, '//*[@id="solar"]/div[2]/aside/section')
    assert driver.find_element(By.CLASS_NAME, 'h1')
