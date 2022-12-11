from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://gymlog.ru/'
        self.login_url = 'https://gymlog.ru/profile/login/'
        self.my_exercise_url = 'https://gymlog.ru/profile/380/'
        self.my_settings_url = 'https://gymlog.ru/profile/settings/'

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_page_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_page_to_middle(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")