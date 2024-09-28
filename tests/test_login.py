import time;
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.LoginPage import LoginPage
import pytest

#@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.skip
class TestLoginPositive:

  
    def test_positive_login(self):

        login_page= LoginPage(self.driver)

        login_page.enter_username("student")

        time.sleep(5)
        login_page.enter_password("Password123")
       
        time.sleep(5)
        login_page.click_on_submit_button()

        time.sleep(2)
        actual_url= self.driver.current_url
        print( actual_url)
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        time.sleep(3)

        text_locator=self.driver.find_element(By.XPATH, "//div//h1[@class='post-title']")
        actual_text= text_locator.text
        assert actual_text == "Logged In Successfully"

        logout_button_locator=self.driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed
        
