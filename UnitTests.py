import unittest

class UnitTests1(unittest.TestCase):
    
    def test_Test1(self):
        a = 'hello'
        self.assertEqual(a, "hello")
        
    def test_Test2(self):
        b = 'world'
        self.assertEqual(b, "world")
        
class UnitTests2(unittest.TestCase):
    
    def setUp(self):
        self.c = 'hello'
    
    def tearDown(self):
        self.c = 'HELLO'
    
    def test_Test1(self):
        self.assertEqual(self.c, "hello")

if __name__ == '__main__':
    a = 'hello'
    b = 'world'
    unittest.main()