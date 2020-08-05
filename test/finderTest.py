##
# Tests for finder.py
##

import unittest
from src.histogram import histogram_localization


class finderTest(unittest.TestCase):
    def test_something(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0, 0]]
        sensor_right = 0.8
        p_move = 1.0
        p = histogram_localization(colors, measurements, motions, sensor_right, p_move)
        self.assertAlmostEqual(p[0][1], 0.06667, places=3)


if __name__ == '__main__':
    unittest.main()
