from pages.home_page import HomePage
from pages.login_page import LoginPage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_registration_form_by_scroll(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.scroll_page_to_bottom()
    assert home_page.registration_form_is_displayed()


def test_go_to_registration_by_touch_registr(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.registration_button_is_displayed().click()
    assert home_page.registration_form_is_displayed()


def test_go_to_login_page(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_login_page()
    registr_page = LoginPage(driver)
    assert registr_page.login_email_field_is_displayed()
    assert registr_page.password_field_is_displayed()
    assert registr_page.entrance_button_is_displayed()
    assert registr_page.vk_is_displayed()
    assert registr_page.twitter_is_displayed()
    assert registr_page.ok_is_displayed()
    assert registr_page.instagram_is_displayed()
    assert registr_page.facebook_is_displayed()


def test_open_block_exercises(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_exercises_page()
    return home_page.check_exercises_page_opened()


def test_open_block_programs(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_programs_page()
    return home_page.check_programs_page_opened()


def test_contacts_form(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_contacts_form()
    return home_page.check_contacts_form()

