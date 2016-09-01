from tribune_csv import transform_data, convert_to_utc, prepend_baseurl, prepare_csv
import unittest

class TestFunctions(unittest.TestCase):

    def test_utc_conversion(self):
        self.assertEqual(convert_to_utc("Tue, 30 Aug 2016 22:42:48 -0500"), "2016-08-30")

if __name__ == '__main__':
    unittest.main()
