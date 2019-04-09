import unittest
from location import *


class TestLab1(unittest.TestCase):
    """Tests the boilerplate methods in the Location
    class."""

    def test_init(self):
        """Tests each attribute of a Location object
        is correct."""
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = Location("Hell", 0, -200)

        self.assertEqual(loc1.name, "SLO")
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)
        self.assertEqual(loc2.name, "Paris")
        self.assertEqual(loc2.lat, 48.9)
        self.assertEqual(loc4.name, "Hell")
        self.assertEqual(loc4.lon, -200)
        self.assertEqual(loc1.name, loc3.name)

    def test_repr(self):
        """Tests the string representation of each
        Location object."""
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = Location("Hell", 0, -200)

        self.assertEqual(repr(loc1), "Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
        self.assertEqual(repr(loc4), "Location('Hell', 0, -200)")

    def test_eq(self):
        """Tests for equality of Location objects."""
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = Location("Hell", 0, -200)
 
        self.assertEqual(loc1, loc3)
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc2, loc4)

if __name__ == "__main__":
        unittest.main()
