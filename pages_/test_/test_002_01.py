from selenium import webdriver
from pages_.loginPage import LoginPage



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


loginPageObject = LoginPage(driver)
loginPageObject.fill_username_field("lineclean6@gmail.com")
loginPageObject.click_to_continue_button()
loginPageObject.fill_pass_field("Amazon0.")
loginPageObject.click_to_signin_button()


driver.close()
