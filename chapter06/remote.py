import unittest
from selenium.webdriver.remote import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SearchProducts(unittest.TestCase):
    def setUp(self):

        self.driver = \
            webdriver.WebDriver(command_executor="http://10.0.0.4:4444/wd/hub",desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def testSearchByCategory(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver\
            .find_elements_by_xpath("//h2[@class='product-name']/a")

        # check count of products shown in results
        self.assertEqual(3, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
