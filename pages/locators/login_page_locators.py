from selenium.webdriver.common.by import By

login_email_button = (By.ID, 'email')
password_button = (By.ID, 'password')
entrance_button = (By.XPATH, '//*[@id="login-form"]/div[1]/div[4]/button')
remember_me = (By.XPATH, '//*[@id="login-form"]/div[1]/div[4]/label)')
vk = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[1]')
twitter = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[2]')
ok = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[3]')
instagram = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[4]')
facebook = (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/a[5]')
user_login_email = (By.XPATH, '//*[@id="header"]/ul/li[1]/a')
allert_message = (By.XPATH, '//*[@id="login-form"]/div[1]/div[3]/div/div')
foget_password = (By.XPATH, '//*[@id="login-form"]/div[2]/div[2]/a[2]')
recovery_button = (By.XPATH, '//*[@id="recovery-form"]/div[1]/div[3]/button')
logout_button = (By.CSS_SELECTOR, 'a[href="/profile/logout/"]')
login_button_icon = (By.CLASS_NAME, 'login-button')
