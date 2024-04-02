import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

##################### TO CHECK THE ALERT TEXT: INVALID USERNAME OR PASSWORD  #########################

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver for Chrome
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_invalid_login_alert(self):
        # Open the login page
        self.driver.get("http://127.0.0.1:5500/webpage1.html")

        # Find the username, password input fields, and the login button
        username_input = self.driver.find_element_by_name("uname")
        password_input = self.driver.find_element_by_name("psw")
        login_button = self.driver.find_element_by_css_selector("button[type='submit']")

        # Enter invalid username and password
        username_input.send_keys("akshata")
        password_input.send_keys("Learning")

        # Click the login button
        login_button.click()

        try:
            # Wait for the alert to appear (you might need to adjust the timeout based on your application)
            alert = Alert(self.driver)
            alert_text = alert.text
            alert.accept()

            # Assert that the alert contains the expected text
            expected_alert_text = "Invalid username or password"
            self.assertIn(expected_alert_text, alert_text, f"Expected: {expected_alert_text}, Actual: {alert_text}")

        except Exception as e:
            # Handle the case where there is no alert or any other exception
            self.fail(f"Failed to detect alert: {e}")

if __name__ == '__main__':
    unittest.main()
