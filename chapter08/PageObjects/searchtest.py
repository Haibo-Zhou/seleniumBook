import unittest
from homepage import HomePage
from basetestcase import BaseTestCase

class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        print("test01_homepage")
        homepage = HomePage(self.driver)
        print("start search")
        search_results = homepage.search.searchFor('earphones')
        print("1st_assertEqual")
        self.assertEqual(2, search_results.product_count)
        print("open product page")
        product = search_results.open_product_page('MADISON OVEREAR HEADPHONES')
        print("2nd_assertEqual")
        self.assertEqual('MADISON OVEREAR HEADPHONES', product.name)
        self.assertEqual('$125.00', product.price)
        self.assertEqual('IN STOCK', product.stock_status)

if __name__ == '__main__':
    unittest.main(verbosity=2)
