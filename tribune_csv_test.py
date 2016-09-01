from tribune_csv import convert_to_utc, prepend_baseurl, prepare_csv
import unittest

class TestFunctions(unittest.TestCase):

    def test_convert_to_utc(self):
        self.assertEqual(convert_to_utc("Tue, 30 Aug 2016 22:42:48 -0500"), "2016-08-30")

    def test_prepend_baseurl(self):
        self.assertEqual(prepend_baseurl('article', '/foo'), 'https://www.texastribune.org/foo')

        self.assertEqual(prepend_baseurl('image', '/foo'), 'https:/foo')

        self.assertEqual(prepend_baseurl('invalid', '/foo'), None)

    def test_prepare_csv(self):
        data = [['c', 2, 'baz'], ['b', 1, 'bar'], ['a', 0, 'foo']]
        expected_output = [['Article URL', 'Date', 'Author', 'Headline', 'Image URL'], ['a', 0, 'foo'], ['b', 1, 'bar'], ['c', 2, 'baz']]
        self.assertEqual(prepare_csv(data), expected_output)

if __name__ == '__main__':
    unittest.main()
