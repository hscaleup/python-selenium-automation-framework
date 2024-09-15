
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.LoginPage import LoginPage
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginNegative:

    
    def test_negative_login_scenario(self):
    
        login_page= LoginPage(self.driver)
        login_page.enter_username("student")
        time.sleep(5)
        login_page.enter_password("Test")
        time.sleep(5)
        login_page.click_on_submit_button()
        time.sleep(5)
       # assert login_page.error_message_is_displayed, "Error message is not diaplyaed, but it should be"
        #assert login_page.error_message_text == "Your password is invalid!", "Error message is not expected"

        error_message_locator = self.driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed, "Error message is not diaplyaed, but it should be"
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
       
        