import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import random

from abc import ABC, abstractmethod

class Brush(ABC):
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.x = random.random()*self.x_dim
        self.y = random.random()*self.y_dim

        # These are updated in move()
        self.x_history = []
        self.y_history = []

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
        self.x_history.append(self.x)
        self.y_history.append(self.y)
        
        self.x = self.x + 0.5        
        self.y = self.y + 0.5

        # This should be removed because out of bound should not be possible
        if self.x > self.x_dim:
            self.x = self.x - self.x_dim

        if self.y > self.y_dim:
            self.y = self.y - self.y_dim


class Painting():
    def __init__(self, dim, brushes, iterations): 
        self.iterations = iterations
        (self.x_dim, self.y_dim) = dim

        self.brushes = brushes
        for brush in self.brushes:
            brush.set_canvas(self)

        # Create empty figure
        self.Figure = plt.figure()
        plt.xlim(0,self.x_dim)
        plt.ylim(0,self.y_dim)

    def move_brushes(self):
        for brush in self.brushes:
            brush.move()

    def generate_data(self):
        for i in range(self.iterations):
            self.move_brushes()

    def plot_data(self):
        for brush in self.brushes:
            x_values = brush.x_history
            y_values = brush.y_history
            plt.plot(x_values, y_values)
        plt.gca().set_aspect('equal')
        plt.show()

    def generate_gif(self):
        
        fig, ax = plt.subplots()

        def animation_function(frame):
            ax.clear
            ax.set_xlim(0, self.x_dim)
            ax.set_ylim(0, self.y_dim)
            lines = []
            for brush in self.brushes:
                x_values = brush.x_history[:frame]
                y_values = brush.y_history[:frame]
                line, = ax.plot(x_values, y_values, color='red', lw=2)
                lines.append(line)
            if frame%10 == 0:
                print('-------------------------frame {}-----------------------------'.format(frame))
            return tuple(lines)
        
        ani = FuncAnimation(fig, animation_function, interval=20, blit=True, repeat=True, frames=self.iterations)    
        ani.save("drawing.gif", dpi=300, writer=PillowWriter(fps=25))

