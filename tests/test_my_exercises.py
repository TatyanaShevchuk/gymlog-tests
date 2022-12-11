from selenium.webdriver.common.by import By
from time import sleep
from pages.my_exercises_page import ExerPage
import pytest


@pytest.mark.my_exercises
def test_add_exercise_without_data(driver, user_logining):  # nothing should be on this page
    exer_page = ExerPage(driver)
    exer_page.add_exercise_without_data()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/profile/exercises/380/"]').click()
    assert exer_page.no_exercise()


@pytest.mark.my_exercises
def test_add_exercise_with_all_data(driver, user_logining):
    exer_page = ExerPage(driver)
    exer_page.add_exercise_with_all_data()
    sleep(3)
    assert exer_page.exercise_added()




