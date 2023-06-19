import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

from abc import ABC, abstractmethod

class Brush(ABC):
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.x = random.random()*self.x_dim
        self.y = random.random()*self.y_dim

        self.canvas = None

    @abstractmethod
    def move(self):
        pass

    def set_canvas(self, canvas):
        self.canvas = canvas

    def get_pos(self):
        return (self.x, self.y)
    
    @property
    def is_out_of_bounds(self):
        return self.x < 0 or self.y < 0 or self.x > self.x_dim or self.y > self.y_dim
    
class StraightBrush(Brush):
    
    def move(self):
        self.x = self.x + 0.5        
        self.y = self.y + 0.5

        # This should be removed because out of bound should not be possible
        if self.x > self.x_dim:
            self.x = self.x - self.x_dim

        if self.y > self.y_dim:
            self.y = self.y - self.y_dim

        return (self.x, self.y)


class Painting():
    def __init__(self, dim, brushes, iterations): 
        self.iterations = iterations
        (self.x_dim, self.y_dim) = dim

        self.brushes = brushes
        for brush in self.brushes:
            brush.set_canvas(self)

        self.data = [[brush.get_pos()] for brush in self.brushes]

        # Create empty figure
        self.Figure = plt.figure()
        plt.xlim(0,self.x_dim)
        plt.ylim(0,self.y_dim)

    def move_brushes(self):
        for i, brush in enumerate(self.brushes):
            (x,y) = brush.move()
            self.data[i].append((x,y))

    def generate_data(self):
        for i in range(self.iterations):
            self.move_brushes()

    def plot_data(self):
        for data_i in self.data:
            x_values = [data_i[j][0] for j in range(self.iterations)]
            y_values = [data_i[j][1] for j in range(self.iterations)]
            plt.plot(x_values, y_values)
        plt.gca().set_aspect('equal')
        plt.show()

    def create_video():
        return None
