from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.LoginPage import LoginPage
import pytest
from utilities import ReadConfigurations
from ddt import ddt,data,unpack
import unittest


@pytest.mark.usefixtures("setup_and_teardown")
@ddt
class TestLoginMultiple:

    #@data(*ReadConfigurations.read_data_from_csv("C:\\Users\\44745\\workspace\\python-selenium-automation-framework\\testdata\\input.csv"))
    
    @data(("student","test"))
    @unpack
    def test_login_scenario(self, user, pwd):
        login_page= LoginPage(self.driver)
        login_page.enter_username("student")
        time.sleep(5)
        login_page.enter_password("test")

        time.sleep(5)
        login_page.click_on_submit_button()
        time.sleep(5)
       # assert login_page.error_message_is_displayed, "Error message is not diaplyaed, but it should be"
        #assert login_page.error_message_text == "Your password is invalid!", "Error message is not expected"

        error_message_locator = self.driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed, "Error message is not diaplyaed, but it should be"
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"