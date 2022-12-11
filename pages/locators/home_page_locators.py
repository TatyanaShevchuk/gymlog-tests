from selenium.webdriver.common.by import By


login_button = (By.XPATH, '//*[@id="header"]/a[1]')
user_email_after_enter = (By.LINK_TEXT, 'User380 [shevtanya2022@gmail.com]')
registration_form = (By.ID, 'registration-form')
registr_button = (By.XPATH, '//*[@id="header"]/a[2]')
exercises_button = (By.XPATH, '//*[@id="top-menu"]/a[4]')
programs_button = (By.XPATH, '//*[@id="top-menu"]/a[5]')
contacts_button = (By.XPATH, '//*[@id="top-menu"]/a[1]')
filters_exercises1 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[1]/label')
filters_exercises2 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[2]/label')
groups_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[1]')
groups_mini_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]')
filters_programs = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]')
contacts = (By.ID, 'contacts')