from selenium.webdriver.common.by import By


class HomePageLocators:
    login_button = (By.XPATH, '//*[@id="www-navigation-container"]/div[2]/div[1]/div[3]/div[1]/div[1]')
    login_name = (By.NAME, 'email')
    login_password = (By.NAME, 'password')
    login_submit = (By.ID, 'login-button')
    website_enter = (By.XPATH, '//*[@id="renderTarget"]/div/main/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[1]/a')
