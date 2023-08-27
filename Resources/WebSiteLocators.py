from selenium.webdriver.common.by import By


class WebSiteLocators:
    website_button = (
        By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/nav/div[1]/div[2]/div[1]/a')
    website_pages = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/a')
    website_calendar = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_8141"]')
    add_element = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div/button')
