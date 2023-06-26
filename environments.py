import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Gymnasium is a project that provide an API for all single agent reinforcement 
# learning environments that include implementations of common environments: 
# cartpole, pendulum, mountain-car, mujoco, atari, and more.
CEG = [261.63, 329.63, 392.00]

class ChordSim(gym.Env):
    def init(self, dim=[0,500], chord=CEG, reward_func_type='constant'):
        self.dim = dim
        self.chord = chord
        match reward_func_type:
            case 'constant':
                self.reward_func = lambda x : constant_reward(x, self.chord, self.dim/40)

        
    def calc_ball_reward(self):
        return None


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


