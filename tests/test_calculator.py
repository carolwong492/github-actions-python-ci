import unittest
from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(subtract(6, 2), 4)
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-1, -1), 0)
  
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(2, 4), 0.5)
        self.assertEqual(divide(-4, 2), -2)
        # COMPLETE HERE
  
    if __name__ == '__main__':
        unittest.main()