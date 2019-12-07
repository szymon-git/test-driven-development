import unittest
import program

class TestHelloWorld(unittest.TestCase):

    def test_HelloWorld(self):
        self.assertEqual(program.HelloWorld(), "HelloWorld")

if __name__ == '__main__':
    unittest.main()
