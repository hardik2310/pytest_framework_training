from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click_by_locator(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def type_by_locator(self, locator, text):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def get_attribute_value(self, locator, attribute_name):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute_name)

    def get_text_from_locator(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

