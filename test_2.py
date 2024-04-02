import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

##################### HTML CONTENT CHECKER OF LOGIN PAGE , TITLE OF THE PAGE #########################
class HTMLContentCheckerTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver for Chrome
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

    def test_check_learning_word(self):
        # Replace "your_html_file.html" with the actual URL of your HTML file
        url = "http://127.0.0.1:5500/webpage1.html"
        
        # Open the URL in Chrome
        self.driver.get(url)

        # Fetch the HTML content
        html_content = self.driver.page_source

        # Check if the word "Learning" is present in the HTML content
        if "Learning" in html_content:
            result = "Pass"
        else:
            result = "Fail"

        # Print the result
        print(result)
        
        # Assert the result
        self.assertEqual(result, "Pass", "The word 'Learning' is not present in the HTML content")

if __name__ == "__main__":
    unittest.main()
