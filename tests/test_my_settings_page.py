from pages.my_settings_page import SettingsPage
from time import sleep
import pytest


@pytest.mark.my_settings
def test_open_my_settings_page(driver, user_logining):
    set_page = SettingsPage(driver)
    sleep(5)
    set_page.open_my_settings_page()
    assert set_page.my_settings_page_in_opened()


@pytest.mark.my_settings
def test_add_all_data_in_profile(driver, user_logining):  # precondition nothing in profile before
    set_page = SettingsPage(driver)
    set_page.my_settings_button()
    set_page.add_surname()
    set_page.add_name()
    set_page.add_patronymic()
    set_page.add_city()
    set_page.add_address()
    set_page.add_birthday()
    set_page.scroll_page_to_middle()
    set_page.add_profile_info()
    set_page.add_contacts()
    sleep(3)
    set_page.button_save()
    assert set_page.check_update_profile_info()

