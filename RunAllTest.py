# import unittest
# from test_1 import CourseraPageTest
# from test_2 import HTMLContentCheckerTest
# from test_3 import TestLogin

# def suite():
#     loader = unittest.TestLoader()
#     test_suite = unittest.TestSuite()
#     # Add the specific test cases
#     test_suite.addTests(loader.loadTestsFromTestCase(CourseraPageTest))
#     test_suite.addTests(loader.loadTestsFromTestCase(HTMLContentCheckerTest))
#     test_suite.addTests(loader.loadTestsFromTestCase(TestLogin))
#     return test_suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     # Run the entire suite
#     result = runner.run(suite())

import unittest
from swagtest_1 import ContentCheckerTest

def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    # Add the specific test cases
    test_suite.addTests(loader.loadTestsFromTestCase(ContentCheckerTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # Run the entire suite
    result = runner.run(suite())
