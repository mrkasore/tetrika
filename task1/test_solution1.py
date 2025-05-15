import unittest
from solution import  strict

@strict
def add(a: int, b: int) -> int:
    return a + b

@strict
def concat(a: str, b: str) -> str:
    return a + b

@strict
def negate(flag: bool) -> bool:
    return not flag

@strict
def divide(x: float, y: float) -> float:
    return x / y

class TestStrictDecorator(unittest.TestCase):

    def test_add_valid(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            add(2, "3")

    def test_concat_valid(self):
        self.assertEqual(concat("hi", "there"), "hithere")

    def test_concat_invalid(self):
        with self.assertRaises(TypeError):
            concat("hi", 5)

    def test_negate_valid(self):
        self.assertTrue(negate(False))

    def test_negate_invalid(self):
        with self.assertRaises(TypeError):
            negate(1)

    def test_divide_valid(self):
        self.assertAlmostEqual(divide(6.0, 2.0), 3.0)

    def test_divide_invalid(self):
        with self.assertRaises(TypeError):
            divide(6, "2")

if __name__ == '__main__':
    unittest.main()