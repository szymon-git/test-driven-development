import unittest
import tester

class TestString(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(tester.doUpper("ala_ma_kota"), "ALA_MA_KOTA")

    def test_lower(self):
        self.assertEqual(tester.doLower("AlA_I_AS"), "ala_i_as")

    def test_replace(self):
        str = tester.doReplace("bananas", "apples", "I like bananas")
        self.assertTrue(str.index("apples") > 0)

    def test_len(self):
        self.assertEqual(tester.doLen("Samochod"), 8)

    def test_capitalize(self):
        self.assertEqual(tester.doCapitalize("adam"), "Adam")


if __name__ == '__main__':
    unittest.main()
