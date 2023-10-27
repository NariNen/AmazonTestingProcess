from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.driver = driver
        pass

    def fill_username_field(self, username):
        userNameFildElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFildElement, username)
        # userNameFildElement.clear()
        # userNameFildElement.send_keys(username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)
        # continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFildElement = self._find_element(By.ID, "ap_password")
        # passFildElement.clear()
        # passFildElement.send_keys(password)
        self._fill_field(passwordFildElement, password)

    def click_to_signin_button(self):
        sleep(7)
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signInButtonElement)
        # signInButtonElement.click()
        sleep(7)
