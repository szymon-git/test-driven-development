import unittest
import kalkulator

class TestCalculator(unittest.TestCase):

    def test_kalkulator(self):
        self.assertEqual(kalkulator.dodaj(1,2), 3)

    def test_kalkulator(self):
        self.assertEqual(kalkulator.odejmij(7,2), 5)

    def test_kalkulator(self):
        self.assertEqual(kalkulator.pomnoz(3,2), 6)

    def test_kalkulator(self):
        self.assertEqual(kalkulator.podziel(10,2), 5)

if __name__ == '__main__':
    unittest.main()
