# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")
plt.rcParams['font.family'] = 'IPAPGothic'

class Graph:
    def __init__(self, title, style):
        self.title = title
        self.style = style
        self.fig, self.ax = plt.subplots()
        self.x = []
        self.y = []
        self.xlabel = None
        self.ylabel = None
        self.legend = None

    def add_data(self, x, y, name=None):
        if len(x) == len(y):
            self.x.append(x)
            self.y.append(y)
            return 1
        else:
            print("ERROR: The data length of x and y is different.")
            return -1

    def draw(self, output=None, show=False):
        try:
            for i in range(len(self.x)):
                self.ax.plot(self.x[i], self.y[i])
            self.ax.set_title(self.title)
            self.ax.set_xlabel(self.xlabel)
            self.ax.set_ylabel(self.ylabel)

            if output: plt.savefig(output)
            if show: plt.show()
            return 1
        except:
            return -1
