import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def tearDown(self):
        print("tearDown")
        # close the browser window
        self.driver.quit()
