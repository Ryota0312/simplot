import unittest
from simplot import Simplot

class TestSimplot(unittest.TestCase):
    def test_differentlen(self):
        g = Simplot.Graph("TestGraph", "line")
        self.assertEqual(-1, g.add_data([1,2,3,4,5,6], [10,20,30,40,50], name="Test"))
    
    def test_linegraph1(self):
        g = Simplot.Graph("TestGraph", "line")
        g.add_data([1,2,3,4,5], [10,20,30,40,50], name="Test")
        self.assertEqual(1, g.draw())

    def test_linegraph2(self):
        g = Simplot.Graph("TestGraph", "line")
        g.add_data([1,2,3,4,5], [10,20,30,40,50], name="Test1")
        g.add_data([1,2,3,4,5], [20,30,40,50,60], name="Test2")
        self.assertEqual(1, g.draw())
        
