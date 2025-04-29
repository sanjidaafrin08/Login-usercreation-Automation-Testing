from selenium.webdriver.common.by import By
from BasePage import BasePage

class UserCreationPage(BasePage):
    account_module = (By.XPATH, "//i[@class='v-icon notranslate v-theme--light v-icon--size-default text-secondary']//*[name()='svg']")
    user_settings = (By.XPATH, "//div[contains(text(),'User Settings')]")
    add_member = (By.XPATH, "//button[contains(@class, 'v-btn') and contains(text(), 'Add Member')]")
    user_type_dropdown = (By.XPATH, "//div[@class='v-select__selections']")
    user_type_option = (By.XPATH, "//div[contains(text(),'User')]")
    member_name_field = (By.XPATH, "//input[@placeholder='Enter Member Name']")
    email_field = (By.XPATH, "//input[@placeholder='Enter Email Address']")
    role_dropdown = (By.XPATH, "(//div[@role='combobox'])[4]")
    line_manager_dropdown = (By.XPATH, "(//div[@role='combobox'])[5]")
    phone_number_field = (By.XPATH, "//input[@aria-describedby='input-77-messages']")
    password_field = (By.XPATH, "//input[@placeholder='Enter Password']")
    invite_button = (By.XPATH, "//button[normalize-space()='Invite']")

    def create_user(self, name, email, phone, password):
        self.click(self.account_module)
        self.click(self.user_settings)
        self.click(self.add_member)
        self.click(self.user_type_dropdown)
        self.click(self.user_type_option)
        self.send_keys(self.member_name_field, name)
        self.send_keys(self.email_field, email)
        self.select_dropdown_option(self.role_dropdown, "Intern 2")
        self.select_dropdown_option(self.line_manager_dropdown, "Test")
        self.send_keys(self.phone_number_field, phone)
        self.send_keys(self.password_field, password)
        self.click(self.invite_button)

    def select_dropdown_option(self, dropdown, option_text):
        self.click(dropdown)
        option = (By.XPATH, f"//div[contains(text(),'{option_text}')]")
        self.click(option)
