import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

class Brush():
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.x = random.random()*self.x_dim
        self.y = random.random()*self.y_dim

    def move(self):
        self.x = self.x + 0.5        
        self.y = self.y + 0.5

        # This should be removed because out of bound should not be possible
        if self.x > self.x_dim:
            self.x = self.x - self.x_dim

        if self.y > self.y_dim:
            self.y = self.y - self.y_dim

        return (self.x, self.y)

    def set_canvas(self, canvas):
        self.canvas = canvas

    def get_pos(self):
        return (self.x, self.y)


class Painting():
    def __init__(self, dim, brushes, iterations):
        self.iterations = iterations
        (self.x_dim, self.y_dim) = dim

        self.brushes = brushes
        for brush in self.brushes:
            brush.set_canvas(self)

        self.data = [[self.brushes[i].get_pos()] for i in range(len(self.brushes))]

        # Create empty figure
        self.Figure = plt.figure()
        plt.xlim(0,self.x_dim)
        plt.ylim(0,self.y_dim)

    def move_brushes(self):
        for i in range(len(self.brushes)):
            (x,y) = self.brushes[i].move()
            self.data[i].append((x,y))

    def generate_data(self):
        for i in range(self.iterations):
            self.move_brushes()

    def plot_data(self):
        for i in range(len(self.brushes)):
            x_values = [self.data[i][j][0] for j in range(self.iterations)]
            y_values = [self.data[i][j][1] for j in range(self.iterations)]
            plt.plot(x_values, y_values)
        plt.gca().set_aspect('equal')
        plt.show()

    def create_video():
        return None
