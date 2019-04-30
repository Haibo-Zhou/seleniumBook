from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class DragAndDropTest(unittest.TestCase):
    URL = 'http://jqueryui.com/resources/demos/droppable/default.html'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def test_drag_and_drop(self):
        driver = self.driver

        source = driver.find_element_by_id('draggable')
        target = driver.find_element_by_id('droppable')

        ActionChains(self.driver).drag_and_drop(source, target).perform()
        self.assertEqual('Dropped!', target.text)

    def tearDown(self):
        self.driver.close()

if __name__== '__main__':
    unittest.main(verbosity=2)
