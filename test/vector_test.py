import math
import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(1.0, -2.0, -12.04)
        return super().setUp()

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_strdunder(self):
        self.assertEqual(str(self.v2), "(1.0, -2.0, -12.0)")

    def test_addition(self):
        sum = self.v1 + self.v2
        res = [getattr(sum, var) for var in ["x", "y", "z"]]
        self.assertEqual(res, [2.0, -4.0, -14.04])

    def test_subtraction(self):
        res = [getattr(self.v1 - self.v2, var) for var in ["x", "y", "z"]]
        self.assertEqual(res, [0.0, 0.0, 10.04])

    def test_multiplication_by_num1(self):
        with self.assertRaises(ValueError):
            self.v1 * 3

    def test_multiplication_by_num2(self):
        with self.assertRaises(ValueError):
            3 * self.v1

    def test_multiplication(self):
        res = [getattr(self.v1 * self.v2, var) for var in ["x", "y", "z"]]
        self.assertEqual(res, [1.0, 4.0, 24.08])

    def test_division_by_num(self):
        with self.assertRaises(ValueError):
            self.v1 / 3

    def test_division(self):
        result = [getattr(self.v1 / self.v2, var) for var in ["x", "y", "z"]]
        expected = [1.0, 1.0, 0.166112957]
        self.assertTrue(any([math.isclose(a, b) for a, b in zip(result, expected)]))


if __name__ == "__main__":
    unittest.main()
