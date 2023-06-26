import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Gymnasium is a project that provide an API for all single agent reinforcement 
# learning environments that include implementations of common environments: 
# cartpole, pendulum, mountain-car, mujoco, atari, and more.
CEG = [261.63, 329.63, 392.00]

class ChordSim(gym.Env):
    def init(self, start_pos=261.63, dim=[0,500], chord=CEG, reward_func_type='constant', delta_t = 0.01, a_const=1,
             reward_radius=10):
        self.dim = dim
        self.chord = chord
        self.stat = self.chord[0]
        self.delta_t = delta_t
        self.reward_radius = reward_radius
        self.action_space = spaces.Discrete(3)
        self.a_const = a_const
        self.a = 0
        self.v = 0
        self.x = start_pos
        self.t = 0
        self.T = 20 # seconds

        match reward_func_type:
            case 'constant': 
                # This basically converts an external function to a class function
                self.position_reward_func = lambda : span_constant_reward(self.x, self.chord, self.dim/40)
        self.edge_punishment = lambda : calc_edge_reward(self.x, self.dim)

    def get_total_reward(self):
        return (self.position_reward_func(self.x) 
                + abs(self.v) 
                + abs(self.a)
                + self.edge_punishment(self.x))

    def step(self, action):
        assert self.action_space.contains(action)
        
        
        self.a = (action - 1) * self.a_const

        next_v = self.v + self.a*self.delta_t
        avg_v = (self.v + next_v)/2
        next_x = self.x + avg_v*self.delta_t

        self.v = next_v
        self.x = next_x

        self.t += self.delta_t
        
        terminated = self.t >= self.T

        reward = self.calculate_reward()

        return (self.state, reward, terminated)
            
    @property
    def state(self):
        return (self.x, self.v, self.a)


def calc_edge_reward(x, span):
    width = span / 10
    if x < width:
        return np.power(width-x, 3)
    if x > span - width:
        return np.pow(x-(span-width), 3)
    else:
        return 0
    
def span_constant_reward(x, chord, radius):
    for note in chord:
        if note > chord-radius and chord < chord+radius:
            return 1
    return 0


