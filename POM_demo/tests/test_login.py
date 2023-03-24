import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from POM_demo.pages.dashboard_page import DashboardPage
from POM_demo.pages.login_page import LoginPage
from framework_demo.base.webdriver_listner import WebDriverWrapper
from framework_demo.utilities import data_source
from framework_demo.utilities.read_utils import get_csv_as_list

"""Login related test cases """


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize("username, password", data_source.test_valid_login_data)
    def test_valid_login(self, username, password):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.enter_username_input(username)
        login_page.enter_password_input(password)
        login_page.click_on_login_button()
        assert_that("Dashboard").is_equal_to(dashboard_page.get_dashboard_text)

    """Invalid Login Test - Data Driven Using .csv file"""

    @pytest.mark.parametrize("username, password, cred_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, cred_error):
        login_page = LoginPage(self.driver)

        login_page.enter_username_input(username)
        login_page.enter_password_input(password)
        login_page.click_on_login_button()

        assert_that(cred_error).is_equal_to(login_page.get_invalid_error_message)

    @pytest.mark.parametrize("username, password, cred_error",
                             get_csv_as_list('../test_data/test_invalid_login_data.csv'))
    def test_invalid_login_with_csv(self, username, password, cred_error):
        login_page = LoginPage(self.driver)

        login_page.enter_username_input(username)
        login_page.enter_password_input(password)
        login_page.click_on_login_button()

        assert_that(cred_error).is_equal_to(login_page.get_invalid_error_message)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        assert_that('OrangeHRM').is_equal_to(self.driver.title)

    def test_header(self):
        assert_that(self.driver.find_element(By.XPATH, '//h5').text).is_equal_to('Login')

    def test_login_placeholders(self):
        login_page = LoginPage(self.driver)

        assert_that("Username").is_equal_to(login_page.get_username_placeholder)
        assert_that("Password").is_equal_to(login_page.get_password_placeholder)
