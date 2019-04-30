import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigation to the application home page
        cls.driver.get("http://demo-store.seleniumacademy.com/")
        # ?don't know why need this title here
        cls.driver.title

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product name displayed
        # currently on result page using find_element_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(3, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()

        # get all the anchor elements which have product name displayed
        # currently on result page using find_element_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)
