from pages.base_page import BasePage
import settings
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import my_settings_page_locators as spl


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_my_settings_page(self):
        self.driver.get(self.my_settings_url)

    def scroll_page_to_middle(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")

    def my_settings_button(self):
        return self.find_element(spl.my_settings_button).click()

    def my_settings_page_in_opened(self):
        return self.find_element(spl.data_field)

    def add_surname(self):
        self.find_element(spl.surname).send_keys(settings.surname)

    def add_name(self):
        self.find_element(spl.name).send_keys(settings.name)

    def add_patronymic(self):
        self.find_element(spl.patronymic).send_keys(settings.patronymic)

    def add_city(self):
        self.find_element(spl.city).send_keys(settings.city)

    def add_address(self):
        self.find_element(spl.address).send_keys(settings.address)

    def add_birthday(self):
        self.find_element(spl.birthday).send_keys(settings.birthday)

    def button_save(self):
        self.find_element(spl.save_button).click()

    def add_photo(self):
        self.find_element(spl.add_photo_field).send_keys('C:\\Users\\shevt\\test_photo.jpg')

    def add_profile_info(self):
        self.find_element(spl.profile_info).send_keys('test info')

    def add_contacts(self):
        self.find_element(spl.contacts).send_keys('123-123-123')

    def add_all_profile_data(self):
        self.my_settings_button()
        self.add_surname()
        self.add_name()
        self.add_patronymic()
        self.add_city()
        self.add_address()
        self.add_birthday()  # precondition: before add new date should be nothing in field
        self.scroll_page_to_middle()
        self.add_profile_info()
        self.add_contacts()
        sleep(3)
        self.button_save()

    def photo_added(self):
        self.find_element(spl.icon_after_adding_photo)

    def check_update_profile_info(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.invisibility_of_element_located(spl.pop_up_message)),
                   message='pop-up message "Данные успешно сохранены" appear')
        return True
