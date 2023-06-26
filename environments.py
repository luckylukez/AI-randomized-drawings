import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Gymnasium is a project that provide an API for all single agent reinforcement 
# learning environments that include implementations of common environments: 
# cartpole, pendulum, mountain-car, mujoco, atari, and more.
CEG = [261.63, 329.63, 392.00]

class ChordSim(gym.Env):
    def init(self, dim=[0,500], chord=CEG, reward_func_type='constant', delta_t = 0.01):
        self.dim = dim
        self.chord = chord
        self.stat = self.chord[0]
        self.delta_t = delta_t
        self.action_space = spaces.Discrete(2)

        match reward_func_type:
            case 'constant':
                self.reward_func = lambda x : constant_reward(x, self.chord, self.dim/40)

    def step(self, action):
        assert self.action_space.contains(action)

        
    def calc_ball_reward(self):
        return None
    


class Ball_1D():
    def __init__(self, mass, start_pos, start_v = (10,0), start_a=(0,0)):
        self.x, self.y = start_pos
        self.v_x, self.v_y = start_v
        self.a_x, self.a_y = start_a
        self.mass = mass

        self.world = None

        self.dt = 0.01

        self.x_history = [self.x]

    def move(self):
        self.x = self.x + self.v_x * self.dt
        self.y = self.y + self.v_y * self.dt

        self.v_x = self.v_x + self.a_x * self.dt
        self.v_y = self.v_y + self.a_y * self.dt

        self.x_history.append(self.x)
        self.y_history.append(self.y)

    @property
    def abs_v(self):
        return np.abs(self.v)
    
    @property
    def abs_a(self):
        return np.abs(self.a)


def calc_edge_reward(x, span):
    width = span / 10
    if x < width:
        return np.power(width-x, 3)
    if x > span - width:
        return np.pow(x-(span-width), 3)
    else:
        return 0
    
def constant_reward(x, chord, radius):
    for note in chord:
        if note > chord-radius and chord < chord+radius:
            return 1
    return 0


