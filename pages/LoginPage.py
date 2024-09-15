from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username_field_name = "username"
    password_field_name = "password"
    submit_button_locator = "submit"
    password_error_field_name = "error"

    def enter_username(self,username):
        element= self.driver.find_element(By.ID,self.username_field_name)
        element.send_keys(username)

    def enter_password(self,password):
        element = self.driver.find_element(By.ID,self.password_field_name)
        element.send_keys(password)

    def click_on_submit_button(self):
        element = self.driver.find_element(By.ID,self.submit_button_locator)
        element.click()

    def error_message_is_displayed(self):
        element= self.driver.find_element(By.ID,self.password_error_field_name)
        return element.is_displayed
    
    def error_message_text(self):
        element= self.driver.find_element(By.ID,self.password_error_field_name)
        return element.text
    
    

