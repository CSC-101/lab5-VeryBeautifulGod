import data
import lab5
import unittest
from data import Point

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(1, 30, 30)
        time2 = data.Time(2, 45, 15)
        result = lab5.time_add(time1, time2)
        expected = data.Time(4, 15, 45)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        time1 = data.Time(23, 59, 59)
        time2 = data.Time(0, 0, 1)
        result = lab5.time_add(time1, time2)
        expected = data.Time(24, 0, 0)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending_1(self):
        input_list = [5, 4, 3, 2, 1]
        result = lab5.is_descending(input_list)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        input_list = [5, 5, 4, 2, 1]
        result = lab5.is_descending(input_list)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between_1(self):
        input_list = [1, 3, 2, 5, 4]
        lower = 1
        upper = 3
        result = lab5.largest_between(input_list, lower, upper)
        expected = 3
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        input_list = [10, 20, 30, 40, 50]
        lower = -1
        upper = 6
        result = lab5.largest_between(input_list, lower, upper)
        expected = 4
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin_1(self):
        input_points = [Point(1, 2), Point(3, 4), Point(0, 5), Point(-6, -8)]
        result = lab5.furthest_from_origin(input_points)
        expected = 3
        self.assertEqual(expected, result)

    def test_furthest_from_origin_empty(self):
        input_points = []
        result = lab5.furthest_from_origin(input_points)
        expected = None
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
