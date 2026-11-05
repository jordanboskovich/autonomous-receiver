import unittest
from field import FieldPosition

class TestFieldPosition(unittest.TestCase):

    def test_distance_calculation(self):
        """Test Euclidean distance between two points (3-4-5 right triangle)."""
        receiver = FieldPosition(0.0, 0.0)
        defender = FieldPosition(3.0, 4.0)
        self.assertEqual(receiver.distance_to(defender), 5.0)

    def test_boundary_checking(self):
        """Test in-bounds and out-of-bounds coordinate checks."""
        valid_pos = FieldPosition(50.0, 25.0)
        out_of_bounds_pos = FieldPosition(-5.0, 25.0)

        self.assertTrue(valid_pos.is_within_bounds())
        self.assertFalse(out_of_bounds_pos.is_within_bounds())

if __name__ == '__main__':
    unittest.main()