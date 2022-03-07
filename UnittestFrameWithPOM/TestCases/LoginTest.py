import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObject.LoginPage import LoginPage
import HtmlTestRunner
import sys
sys.path.append("D:\POM")
import time

class LoginTest(unittest.TestCase):
        Base_Url = "https://admin-demo.nopcommerce.com/"
        username = "admin@yourstore.com"
        password = "admin"
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 10)

        @classmethod
        def setUpClass(cls):
            cls.driver.get(cls.Base_Url)
            cls.driver.maximize_window()

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
            print("Test Completed")

        # Write the Actual Test Case Here

        def test_LoginTest(self):
            login_page = LoginPage(self.driver, self.wait)  # Driver will available for the this test

            # Send Username
            login_page.Username()
            login_page.SetUsername(self.username)

            # Send Password
            login_page.Password()
            login_page.SetPassword(self.password)

            # click the login Button
            login_page.ClickLogin()
            time.sleep(3)

            # Verify the title of page
            titleofpage = self.driver.title
            self.assertEqual("Dashboard / nopCommerce administration", titleofpage, "This is not webpage title")

            # Click the logout button
            time.sleep(5)
            login_page.ClickLogout()


# To Generate the HTML Report
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\\sunil\\POM\\Reports"))