"""Deterministic contracts for synthetic public verification code."""
import unittest
from calculations import average, clamp


class CalculationContracts(unittest.TestCase):
    def test_lower_boundary(self):
        self.assertEqual(clamp(-4, 0, 10), 0)

    def test_upper_boundary(self):
        self.assertEqual(clamp(20, 0, 10), 10)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_inside_bounds(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)

    def test_empty_average(self):
        self.assertEqual(average([]), 0)

    def test_average(self):
        self.assertEqual(average([1, 2, 6]), 3)


if __name__ == "__main__":
    unittest.main()
