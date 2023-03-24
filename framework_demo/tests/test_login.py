import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from framework_demo.base.webdriver_listner import WebDriverWrapper
from framework_demo.utilities import data_source
from framework_demo.utilities.read_utils import get_csv_as_list

"""Login related test cases """


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize("username, password", data_source.test_valid_login_data)
    def test_valid_login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    """Invalid Login Test - Data Driven Using .csv file"""

    @pytest.mark.parametrize("username, password, cred_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, cred_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH,
                                                "//p[text()='Invalid credentials']").text
        assert_that(cred_error).is_equal_to(actual_error)

    @pytest.mark.parametrize("username, password, cred_error",
                             get_csv_as_list('../test_data/test_invalid_login_data.csv'))
    def test_invalid_login_with_csv(self, username, password, cred_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH,
                                                "//p[text()='Invalid credentials']").text
        assert_that(cred_error).is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert actual_title == 'OrangeHRM'
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, '//h5').text
        assert_that(actual_header).is_equal_to('Login')

    def test_login_placeholders(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)
