from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import my_exercise_page_locators as epl


class ExerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_my_exercise(self):
        self.driver.get(self.my_exercise_url)

    def my_exercises_is_displayed(self):
        self.driver.find_element(epl.my_exercises_button)

    def save_button(self):
        self.find_element(epl.save)

    def add_exercise_is_displayed(self):
        return self.find_element(epl.add_exercise)

    def add_exercise_button(self):
        return self.find_element(epl.add_exercise).click()

    def all_field_for_add_exercise_is_displayed(self):
        return self.find_element(epl.all_field_for_add_exercise)

    def all_field_for_add_exercise(self):
        return self.find_element(epl.all_field_for_add_exercise).click()

    def find_exercise(self):
        return self.find_element(epl.find_exercise)

    def my_exercises_button(self):
        self.find_element(epl.my_exercises_button)

    def add_exercise_without_data(self):
        self.find_element(epl.my_exercises_button).click()
        self.find_element(epl.add_exercise).click()
        self.find_element(epl.save).click()

    def add_exercise_with_all_data(self):
        self.find_element(epl.my_exercises_button).click()
        self.add_exercise_button()
        cat_field = self.find_elements(epl.category)
        cat_field[1].click()
        self.find_element(epl.exericise_name).send_keys('Something with neck')
        select = Select(self.find_element(epl.select_value))
        select.select_by_value('347')
        select = Select(self.find_element(epl.mepa_1))
        select.select_by_value('7')
        select = Select(self.find_element(epl.mepa_2))
        select.select_by_value('3')
        self.find_element(epl.save).click()

    def no_exercise(self):
        alert_text = self.find_element(epl.info).text
        return 'Доступные упражнения отсутствуют' in alert_text

    def exercise_added(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.invisibility_of_element_located(epl.pop_up_massage_exercise)),
                   message='pop-up message "Данные успешно сохранены" appear')
        return True

    def delete_exercise(self):
        self.find_element(epl.delete_button).click()
