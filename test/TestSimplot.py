import unittest
from simplot import Simplot

class TestSimplot(unittest.TestCase):
    def setUp(self):
        self.obj = Simplot.Graph("line")

    def test_one(self):
        self.obj.add_data([1,2,3,4,5], [10,20,30,40,50])
        self.assertEqual(1, self.obj.draw())
