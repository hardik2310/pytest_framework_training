from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def get_dashboard_text(self):
        return self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
