from Pages.AbstractBasePage import AbstractBasePage as BasePage


class InteractPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.squarespace.com/')

    def send_text(self, *args: object) -> None:
        try:
            for locator, text in args:
                self.enter_text(locator, text)
        except:
            print('sorry there was an error sending text')

    def navigate_to(self, *locators: object) -> None:
        # try:
            for arg in locators:
                self.click(arg)
        # except:
        #     print('sorry there was an error in navigating to')
