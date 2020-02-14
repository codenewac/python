import unittest

from city_functions11_1 import city_function

class CityTestCase(unittest.TestCase):
    """测试该函数"""
    def test_city_country_population(self):
        full_name=city_function('santiago','chile',50000)
        self.assertEqual(full_name,'Santiago,Chile - population 50000')
unittest.main()