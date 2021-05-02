import unittest

import sys
sys.path.append('src')

from operations import operations

class TestStringMethods(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(operations.is_even(2))
        self.assertTrue(operations.is_even(4))
        self.assertTrue(operations.is_even(10))
        self.assertTrue(operations.is_even(80))
        self.assertTrue(operations.is_even(200))
        self.assertTrue(operations.is_even(2000000000000000))
        self.assertTrue(operations.is_even(8965000000000000000000000000000000000000))
        self.assertFalse(operations.is_even(1))
        self.assertFalse(operations.is_even(3))
        self.assertFalse(operations.is_even(5))
        self.assertFalse(operations.is_even(7))
        self.assertFalse(operations.is_even(111))
        self.assertFalse(operations.is_even(138543518424365468465146541))
        self.assertFalse(operations.is_even(13854351842436546846514654122315435645619))
    
    def test_is_power_of_2(self):
        self.assertTrue(operations.is_power_of_2(2))
        self.assertTrue(operations.is_power_of_2(4))
        self.assertTrue(operations.is_power_of_2(8))
        self.assertTrue(operations.is_power_of_2(16))
        self.assertTrue(operations.is_power_of_2(32))
        self.assertTrue(operations.is_power_of_2(64))
        self.assertTrue(operations.is_power_of_2(512))
        self.assertTrue(operations.is_power_of_2(1024))
        self.assertTrue(operations.is_power_of_2(65536))
        self.assertFalse(operations.is_power_of_2(1))
        self.assertFalse(operations.is_power_of_2(15))
        self.assertFalse(operations.is_power_of_2(18))
        self.assertFalse(operations.is_power_of_2(24))
        self.assertFalse(operations.is_power_of_2(48))
        self.assertFalse(operations.is_power_of_2(100))

    def test_find_closest_upper_power_of_2(self):
        self.assertEqual(operations.find_closest_upper_power_of_2(15), 16)
        self.assertEqual(operations.find_closest_upper_power_of_2(5), 8)
        self.assertEqual(operations.find_closest_upper_power_of_2(9), 16)
        self.assertEqual(operations.find_closest_upper_power_of_2(25), 32)
        self.assertEqual(operations.find_closest_upper_power_of_2(100), 128)
        self.assertEqual(operations.find_closest_upper_power_of_2(200), 256)
        self.assertEqual(operations.find_closest_upper_power_of_2(712), 1024)
        self.assertEqual(operations.find_closest_upper_power_of_2(1000000), 1048576)

    def test_find_closest_lower_power_of_2(self):
        self.assertEqual(operations.find_closest_lower_power_of_2(15), 8)
        self.assertEqual(operations.find_closest_lower_power_of_2(5), 4)
        self.assertEqual(operations.find_closest_lower_power_of_2(9), 8)
        self.assertEqual(operations.find_closest_lower_power_of_2(25), 16)
        self.assertEqual(operations.find_closest_lower_power_of_2(100), 64)
        self.assertEqual(operations.find_closest_lower_power_of_2(200), 128)
        self.assertEqual(operations.find_closest_lower_power_of_2(712), 512)
        self.assertEqual(operations.find_closest_lower_power_of_2(1000000), 524288)

    def test_find_closest_power_of_2(self):
        self.assertEqual(operations.find_closest_power_of_2(15), 16)
        self.assertEqual(operations.find_closest_power_of_2(5), 4)
        self.assertEqual(operations.find_closest_power_of_2(9), 8)
        self.assertEqual(operations.find_closest_power_of_2(25), 32)
        self.assertEqual(operations.find_closest_power_of_2(100), 128)
        self.assertEqual(operations.find_closest_power_of_2(200), 256)
        self.assertEqual(operations.find_closest_power_of_2(712), 512)
        self.assertEqual(operations.find_closest_power_of_2(1000000), 1048576)

    def test_get_operations(self):
        self.assertEqual(operations.get_operations(15), 5)
        self.assertEqual(operations.get_operations(4), 2)
        self.assertEqual(operations.get_operations(1248390), 27)
        self.assertEqual(operations.get_operations(179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368), 1025)


if __name__ == '__main__':
    unittest.main()
    