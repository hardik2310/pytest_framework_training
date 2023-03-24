import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework_demo.base.webdriver_listner import WebDriverWrapper
from framework_demo.utilities import data_source
from framework_demo.utilities.read_utils import get_excel_as_list


class TestEmployee(WebDriverWrapper):
    @pytest.mark.parametrize("username, password, first_name, middle_name, last_name, full_name, verify_f_name",
                             data_source.test_add_employee_data)
    def test_add_valid_employee(self, username, password, first_name, middle_name, last_name, full_name, verify_f_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.NAME, 'firstName').send_keys(first_name)
        self.driver.find_element(By.NAME, 'middleName').send_keys(middle_name)
        self.driver.find_element(By.NAME, 'lastName').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()

        wait = WebDriverWait(self.driver, 50)
        wait.until(
            expected_conditions.text_to_be_present_in_element_attribute((By.NAME, 'firstName'), 'value', first_name))
        employee_name = self.driver.find_element(By.XPATH,
                                                 '//h6[contains(normalize-space(),"' + first_name + '")]').text
        employee_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(employee_name).is_equal_to(full_name)
        assert_that(employee_first_name).is_equal_to(first_name)

    @pytest.mark.parametrize("username, password, first_name, middle_name, last_name, full_name, verify_f_name",
                             get_excel_as_list(io='../test_data/orange_test_data.xlsx',
                                               sheet_name='test_valid_login'))
    def test_add_valid_employee_with_excel(self, username, password, first_name, middle_name, last_name, full_name,
                                           verify_f_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.NAME, 'firstName').send_keys(first_name)
        self.driver.find_element(By.NAME, 'middleName').send_keys(middle_name)
        self.driver.find_element(By.NAME, 'lastName').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()

        wait = WebDriverWait(self.driver, 50)
        wait.until(
            expected_conditions.text_to_be_present_in_element_attribute((By.NAME, 'firstName'), 'value', first_name))
        employee_name = self.driver.find_element(By.XPATH,
                                                 '//h6[contains(normalize-space(),"' + first_name + '")]').text
        employee_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(employee_name).is_equal_to(full_name)
        assert_that(employee_first_name).is_equal_to(first_name)

    @pytest.mark.parametrize("username, password, file_error", data_source.test_invalid_file_data)
    def test_invalid_profile_upload(self, username, password, file_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            r'D:\python automation training\hybrid_framework\test_data\test_invalid_login_data.csv')
        actual_file_error = self.driver.find_element(By.XPATH,
                                                     '//span[contains(@class,"input-field-error-message")]').text
        assert_that(actual_file_error).is_equal_to(file_error)
