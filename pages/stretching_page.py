from pages.base_page import BasePage
from pages.locators import stretching_page_locators as strpl


class StretchingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_stretching(self):
        self.driver.get('https://gymlog.ru/exercises/stretching/')

    def level_beginner_button(self):
        return self.find_element(strpl.level_beginner)

    def level_advanced_button(self):
        return self.find_element(strpl.level_advanced)

    def level_professional_button(self):
        return self.find_element(strpl.level_professional)

    def scroll_page_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def tabs(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
