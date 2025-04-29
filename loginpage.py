from selenium.webdriver.common.by import By
from BasePage import BasePage

class LoginPage(BasePage):
    email_field = (By.ID, "input-4")
    password_field = (By.ID, "input-6")
    sign_in_button = (By.XPATH, "//span[normalize-space()='Sign In']")

    def login(self, email, password):
        self.send_keys(self.email_field, email)
        self.send_keys(self.password_field, password)
        self.click(self.sign_in_button)
