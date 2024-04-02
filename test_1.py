import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##################### TO CHECK AFTER CLICKING SIGN BUTTON, IT SHOULD IDENTIFY THE TEXT TO VERIFY IT IS ON CORRECT PAGE  #########################

class CourseraPageTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver for Chrome
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def click_sign_up_button(self):
        # Wait for the Sign Up button to be clickable
        wait = WebDriverWait(self.driver, 20)
        sign_up_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "signup-btn")))

        # Click the Sign Up button
        sign_up_button.click()

        # Add a delay to allow time for the page to load (adjust as needed)
        time.sleep(10)

    def test_welcome_text_on_sign_in_page(self):
        # Open the Coursera page
        self.driver.get("http://127.0.0.1:5500/webpage1.html")

        # Call the click_sign_up_button function
        self.click_sign_up_button()

        # Wait for the welcome text to be present on the Sign In page
        wait = WebDriverWait(self.driver, 20)
        welcome_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Welcome to Sign In Page']")))

        # Check if the welcome text is displayed
        self.assertTrue(welcome_text.is_displayed(), "Welcome text is displayed on the Sign In page")


if __name__ == '__main__':
    unittest.main()
