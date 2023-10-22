from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, By, value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By, value))
        except:
            print("Error:Element Not found")
            exit(1)

    def _get_title(self):
        return self.driver.title
