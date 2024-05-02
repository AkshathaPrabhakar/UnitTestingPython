import unittest
from swagtest_1 import ContentCheckerTest
from swagtest_2 import LoginButtonTest
from swagtest_3 import UsernameFieldTest
from swagtest_4 import PasswordFieldTest
from swagtest_5 import LoginTest
from swagtest_6 import InvalidLoginTest
from swagtest_7 import AddToCartTest
from swagtest_8 import ShoppingCartTest

## This is sample code to test the code changes difference ##
def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    # Add the specific test cases
    test_suite.addTests(loader.loadTestsFromTestCase(ContentCheckerTest))
    test_suite.addTests(loader.loadTestsFromTestCase(LoginButtonTest))
    test_suite.addTests(loader.loadTestsFromTestCase(UsernameFieldTest))
    test_suite.addTests(loader.loadTestsFromTestCase(PasswordFieldTest))
    test_suite.addTests(loader.loadTestsFromTestCase(LoginTest))
    test_suite.addTests(loader.loadTestsFromTestCase(InvalidLoginTest))
    test_suite.addTests(loader.loadTestsFromTestCase(AddToCartTest))
    test_suite.addTests(loader.loadTestsFromTestCase(ShoppingCartTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # Run the entire suite
    result = runner.run(suite())
