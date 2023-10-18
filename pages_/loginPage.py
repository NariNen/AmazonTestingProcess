from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_username_field(self, username):
        userNameFildElement = self.driver.find_element(By.ID, "ap_email")
        userNameFildElement.clear()
        userNameFildElement.send_keys(username)

    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()

    def fill_pass_field(self, password):
        passFildElement = self.driver.find_element(By.ID, "ap_password")
        passFildElement.clear()
        passFildElement.send_keys(password)

    def click_to_signin_button(self):
        sleep(7)
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
        sleep(7)
