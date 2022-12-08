from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep
import settings


def test_enter_correct_login_data(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.enter_login_data(email=settings.email, password=settings.password)
    assert login_page.user_login_email_is_displayed()


def test_logining_with_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.login_email_field().send_keys('shevtanya2022@gmail.com')
    login_page.password_field().send_keys('11111')
    login_page.entrance_button_is_displayed().click()
    sleep(5)
    assert login_page.allert_message_is_displayed()


def test_logining_without_email(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.password_field().send_keys('kaDbaa')
    login_page.entrance_button_is_displayed().click()
    sleep(5)
    assert login_page.allert_message_is_displayed()


def test_logining_with_login(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.login_email_field().send_keys('User380')
    login_page.password_field().send_keys('kaDbaa')
    login_page.entrance_button_is_displayed().click()
    assert login_page.user_login_email_is_displayed()


def test_logining_without_password_and_login(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.entrance_button_is_displayed().click()
    assert login_page.allert_message_is_displayed()


def test_login_vk(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.vk_is_displayed().click()
    assert driver.find_element(By.XPATH, '/html/body/pre')
    print('bug')


def test_login_twitter(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.twitter_is_displayed().click()
    assert driver.find_element(By.ID, 'debug')
    print('Bug, Возникла внутренняя ошибка сервера.')


def test_login_ok(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.ok_is_displayed().click()
    assert driver.find_element(By.ID, 'hook_Block_OAuth2Login')


def test_login_facebook(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.facebook_is_displayed().click()
    assert driver.find_element(By.ID, 'debug')


def test_forget_password(driver):
    login_page = LoginPage(driver)
    login_page.open_logining()
    login_page.forget_password_is_displayed().click()
    assert login_page.recovery_button_is_displayed()
