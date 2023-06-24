import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Gymnasium is a project that provide an API for all single agent reinforcement 
# learning environments that include implementations of common environments: 
# cartpole, pendulum, mountain-car, mujoco, atari, and more.


class ChordSim(gym.Env):
    def init(self, n=2, dim=(100,100)):
        self.balls = []
        for i in range(n):
            self.balls.append(Ball(...))
    
    def calc_ball_reward(self):




def calc_edge_reward(x, span):
    width = span / 10
    if x < width:
        return np.power(width-x, 3)
    if x > span - width:
        return np.pow(x-(span-width), 3)
    else:
        return 0
     

