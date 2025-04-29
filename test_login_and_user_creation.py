import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loginpage import LoginPage
from user_creation_page import UserCreationPage

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_and_create_user(driver):
    driver.get("https://app.yourwebsite/auth/sign-in")

    login_page = LoginPage(driver)
    login_page.login("test@test.com", "****")

    assert driver.current_url == "https://app..yourwebsite/app/dms/"

    user_creation_page = UserCreationPage(driver)
    user_creation_page.create_user(
        name="Test User",
        email="newuser@test.com",
        phone="01700000000",
        password="Test@1234"
    )
