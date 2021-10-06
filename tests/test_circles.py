import unittest
from artwork_grabber.circles import circle_area
from math import pi

# Run "python -m unittest" from the ROOT DIRECTORY of the project, e.g., "/Users/mgermaine93/Desktop/CODE/album-artwork-finder", in order for this to work properly.


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
