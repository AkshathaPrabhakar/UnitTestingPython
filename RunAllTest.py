import unittest
from swagtest_1 import ContentCheckerTest
from swagtest_2 import LoginButtonTest

def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    # Add the specific test cases
    test_suite.addTests(loader.loadTestsFromTestCase(ContentCheckerTest))
    test_suite.addTests(loader.loadTestsFromTestCase(LoginButtonTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # Run the entire suite
    result = runner.run(suite())