import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, style):
        self.style = style
        self.fig, self.ax = plt.subplots()
        self.x = None
        self.y = None
        self.legend = None

    def add_data(self, x, y):
        self.x = x
        self.y = y

    def draw(self, output=None):
        self.ax.plot(self.x, self.y)
        self.ax.set_title("title")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

        return 1
