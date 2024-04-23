import unittest
import xmlrunner
import os

# Import your test classes
from swagtest_1 import ContentCheckerTest
from swagtest_2 import LoginButtonTest
from swagtest_3 import UsernameFieldTest
from swagtest_4 import PasswordMaskingTest
from swagtest_5 import LoginTest
from swagtest_6 import InvalidLoginTest
from swagtest_7 import AddToCartTest
from swagtest_8 import ShoppingCartTest

def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    # Add the specific test cases
    test_suite.addTests(loader.loadTestsFromTestCase(ContentCheckerTest))
    test_suite.addTests(loader.loadTestsFromTestCase(LoginButtonTest))
    test_suite.addTests(loader.loadTestsFromTestCase(UsernameFieldTest))
    test_suite.addTests(loader.loadTestsFromTestCase(PasswordMaskingTest))
    test_suite.addTests(loader.loadTestsFromTestCase(LoginTest))
    test_suite.addTests(loader.loadTestsFromTestCase(InvalidLoginTest))
    test_suite.addTests(loader.loadTestsFromTestCase(AddToCartTest))
    test_suite.addTests(loader.loadTestsFromTestCase(ShoppingCartTest))
    return test_suite

if __name__ == '__main__':
    # Create a directory to store the XML reports
    xml_output_dir = 'test-reports'
    if not os.path.exists(xml_output_dir):
        os.makedirs(xml_output_dir)

    # Run the entire test suite and generate XML reports
    with open(f'{xml_output_dir}/TEST-report.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        runner.run(suite())

    # Transform the XML report to HTML using XSLT
    xslt_file = 'Conversion.xslt'  # Name of the XSLT file
    xml_file = f'{xml_output_dir}/TEST-report.xml'  # Path to the XML report file
    html_output = f'{xml_output_dir}/Testresultreport.html'  # Path for the HTML output file

    # Transform XML to HTML using XSLT
    import lxml.etree as ET
    dom = ET.parse(xml_file)
    xslt = ET.parse(xslt_file)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    with open(html_output, 'wb') as f:
        f.write(ET.tostring(newdom, pretty_print=True))

    print(f"HTML report generated at: {html_output}")
