from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AbstractBasePage():
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver: object) -> None:
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver

    def click(self, by_locator: object) -> None:
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator: object, text: str) -> None:
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title