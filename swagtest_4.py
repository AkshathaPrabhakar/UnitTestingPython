import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class PasswordFieldTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver for Chrome with options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--no-sandbox")  # Disable sandboxing
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

    def test_password_field(self):
        # Open the Sauce Demo login page
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the password field
        password_field = self.driver.find_element(By.ID, "password")

        # Check if the password field is displayed and enabled
        if password_field.is_displayed() and password_field.is_enabled():
            result = "Password field has been recognized"
        else:
            result = "Password field has not been recognized"

        # Print the result
        print("Password field check result:", result)

        # Assert the result
        self.assertEqual(result, "Password field has been recognized", "The password field is not displayed or enabled")


if __name__ == "__main__":
    unittest.main()
