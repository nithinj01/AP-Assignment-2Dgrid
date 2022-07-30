import unittest
import ShortestDistance


class Testlinesegment(unittest.TestCase):
    def test_closest_line(self):
        grid1 = [['0', '#', '0', '#'],
                 ['#', '0', '#', 'B'],
                 ['0', '#', '#', '#'],
                 ['A', '#', '#', '#']]
        actual = ShortestDistance.min_Distance(grid1)
        expected = 5
        self.assertEqual(actual, expected)

    def test_closest_line_noway(self):
        grid2 = [['0', '#', '0', '#'],
                 ['#', '0', '0', 'B'],
                 ['0', '#', '#', '0'],
                 ['A', '#', '#', '0']]
        actual1 = ShortestDistance.min_Distance(grid2)
        expected1 = -1  # no way to destination
        self.assertEqual(actual1, expected1)
