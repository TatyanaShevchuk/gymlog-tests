from pages.locators import home_page_locators as hpl
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def check_username_and_email_displ_on_home_page(self):
        return self.find_element(hpl.user_email_after_enter).is_displayed()

    def registration_form_is_displayed(self):
        return self.find_element(hpl.registration_form).is_displayed()

    def registration_button_is_displayed(self):
        return self.find_element(hpl.registr_button)

    def go_to_login_page(self):
        return self.find_element(hpl.login_button).click()

    def go_to_exercises_page(self):
        return self.find_element(hpl.exercises_button).click()

    def check_exercises_page_opened(self):
        assert self.find_element(hpl.filters_exercises1).is_displayed()
        assert self.find_element(hpl.filters_exercises1).is_displayed()
        assert self.find_element(hpl.groups_exercises).is_displayed()
        assert self.find_element(hpl.groups_mini_exercises).is_displayed()

    def go_to_programs_page(self):
        return self.find_element(hpl.programs_button).click()

    def check_programs_page_opened(self):
        assert self.find_element(hpl.filters_programs).is_displayed()

    def go_contacts_form(self):
        return self.find_element(hpl.contacts_button).click()

    def check_contacts_form(self):
        assert self.find_element(hpl.contacts).is_displayed()
