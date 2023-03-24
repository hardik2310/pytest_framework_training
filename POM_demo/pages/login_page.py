from selenium.webdriver.common.by import By

from POM_demo.base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__username_locator = (By.NAME, "username")
        self.__password_locator = (By.NAME, "password")
        self.__login_locator = (By.XPATH, "//button[normalize-space()='Login']")
        self.__creds_error = (By.XPATH, "//p[contains(normalize-space(),'Invalid')]")

    def enter_username_input(self, username):
        self.type_by_locator(self.__username_locator, username)

    def enter_password_input(self, password):
        self.type_by_locator(self.__password_locator, password)

    def click_on_login_button(self):
        self.click_by_locator(self.__login_locator)

    @property
    def get_invalid_error_message(self):
        return self.get_text_from_locator(self.__creds_error)

    @property
    def get_username_placeholder(self):
        return self.get_attribute_value(self.__username_locator, 'placeholder')

    @property
    def get_password_placeholder(self):
        return self.get_attribute_value(self.__password_locator, 'placeholder')
