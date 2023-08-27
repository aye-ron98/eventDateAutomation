from selenium import webdriver
from Pages.InteractPage import InteractPage
from Drivers.Drivers import Drivers
from Resources.WebSiteLocators import WebSiteLocators
from Resources.HomePageLocators import HomePageLocators

from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
svc = webdriver.ChromeService(executable_path=Drivers.win_chrome_64)
driver = webdriver.Chrome(service=svc)


def main():
    # Define driver
    automater = InteractPage(driver)

    # Navigate to login
    automater.navigate_to(HomePageLocators.login_button)

    # Send Login Info
    automater.send_text((HomePageLocators.login_name, os.getenv('USER_NAME')),
                        (HomePageLocators.login_password, os.getenv('PASSWORD')))

    # enter website
    automater.navigate_to(HomePageLocators.login_submit,
                          HomePageLocators.website_enter)

    # navigate to calendar
    driver.get('https://devweb.squarespace.com/config/website/pages/5cd5ecbb1905f492b038a788')

    automater.navigate_to(WebSiteLocators.add_element)

    sleep(60)
    print('complete')


if __name__ == '__main__':
    main()
