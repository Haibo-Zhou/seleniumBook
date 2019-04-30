import unittest
from appium import webdriver


class SearchProductsOnIPhone(unittest.TestCase):
    def setUp(self):
        desired_caps={
            'app': 'safari',
            'browserName': 'Safari',
            'platformName': 'iOS',
            'platformVersion': '11.4',
            'deviceName': 'iPhone 8'
        }

        # to connect to Appium server use RemoteWebDriver
        # and pass desired capabilities
        self.driver = \
            webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.implicitly_wait(30)

    def test_search_by_category(self):

        # click on search icon
        #self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name='banner']/XCUIElementTypeLink[3]/XCUIElementTypeLink").click()
        self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"banner\"]/XCUIElementTypeLink[3]/XCUIElementTypeLink").click()
             #driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"banner\"]/XCUIElementTypeLink[3]/XCUIElementTypeLink")
        # get the search textbox
        self.search_field = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name='banner']/XCUIElementTypeOther[2]/XCUIElementTypeSearchField")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver\
            .find_elements_by_xpath("//div[@class='category-products']/ul/li")

        # check count of products shown in results
        self.assertEqual(3, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
