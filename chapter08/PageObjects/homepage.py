from base import BasePage
from base import InvalidPageException

class HomePage(BasePage):
    _home_page_slideshow_locator = 'slideshow-container'

    def __init__(self, driver):
        print("Reach-HomePage")
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            print("Homepage02-validate")
            driver.\
            find_element_by_class_name(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")
