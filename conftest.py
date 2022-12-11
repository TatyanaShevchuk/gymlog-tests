import pytest
import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def user_logining(driver):
    driver.get('https://gymlog.ru/')
    login_button = driver.find_element(By.CLASS_NAME, 'login-button')
    login_button.click()
    login_email = driver.find_element(By.ID, 'email')
    login_email.send_keys(settings.email)
    login_password = driver.find_element(By.ID, 'password')
    login_password.send_keys(settings.password)
    login_password.send_keys(Keys.ENTER)


