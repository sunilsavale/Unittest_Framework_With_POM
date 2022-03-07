from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage():

    # Locators of the Login page and Logout button
    input_username_id = "Email"
    input_password_id = "Password"
    login_button_xpath = ".//button[text()='Log in']"
    logout_button_xpath = ".//a[contains(@href,'/logout')]"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Clear The username Field
    def Username(self):
        self.driver.find_element(By.ID, self.input_username_id).clear()

    # Send the Username
    def SetUsername(self, username):
        self.driver.find_element(By.ID, self.input_username_id).send_keys(username)

    # Clear The Password Field
    def Password(self):
        self.driver.find_element(By.ID, self.input_password_id).clear()

    # Send the password into the password field
    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)

    # Click the login button
    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    # Click the Logout the Button
    def ClickLogout(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.logout_button_xpath)))

