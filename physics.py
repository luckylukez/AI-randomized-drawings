import numpy as np
import math
import itertools as it
from matplotlib import pyplot as plt

class Ball():
    def __init__(self, mass, start_pos, start_v = (10,0), start_a=(0,0)):
        self.x, self.y = start_pos
        self.v_x, self.v_y = start_v
        self.a_x, self.a_y = start_a
        self.mass = mass

        self.world = None

        self.dt = 0.01

        self.x_history = [self.x]
        self.y_history = [self.y]

    def move(self):
        self.x = self.x + self.v_x * self.dt
        self.y = self.y + self.v_y * self.dt

        self.v_x = self.v_x + self.a_x * self.dt
        self.v_y = self.v_y + self.a_y * self.dt

        self.x_history.append(self.x)
        self.y_history.append(self.y)

    @property
    def pos(self):
        return (self.x, self.y)

class World():
    def __init__(self, balls, dim=(100,100), G=10, iterations=1000):
        self.balls = balls
        self.n_balls = len(self.balls)
        for ball in self.balls:
            ball.world = self
        self.x_dim, self.y_dim = dim
        self.G = G
        self.iterations = iterations
        self.iteration = 0

    def run(self):
        for i in range(self.iterations):
            self.calculate_accelerations() # Updates acceleration in balls
            for ball in self.balls:
                ball.move()
            if self.iteration % 100 == 0:
                print(self.iteration)
            self.iteration += 1


    def calculate_accelerations(self):
        forces = np.zeros([self.n_balls, self.n_balls, 2])

        ballindexes = [(i,a) for i,a in enumerate(self.balls)]

        for (i,a), (j,b) in it.combinations(ballindexes, 2):
            r = math.dist(a.pos,b.pos)
            dx = abs(a.x-b.x)
            dy = abs(a.y-b.y)
            F = self.G * a.mass*b.mass / r**2
            Fx = F * dx/r
            Fy = F * dy/r

            if a.x > b.x:
                Fx = -Fx
            if a.y > b.y:
                Fy = -Fy

            # This should make it so that the force of (i,j) is the force put on i by j
            forces[i,j,0] = Fx
            forces[i,j,1] = Fy
            forces[j,i,0] = -Fx
            forces[j,i,1] = -Fy
        
        for i, ball in enumerate(self.balls):
            Fx_tot = np.sum(forces[i,:,0])
            Fy_tot = np.sum(forces[i,:,1])
            ball.a_x = Fx_tot / ball.mass
            ball.a_y = Fy_tot / ball.mass

    def plot(self):
        for ball in self.balls:
            plt.plot(ball.x_history, ball.y_history)

        plt.show()


def main():
    b1 = Ball(10, (20,20), start_v=(-1,0))
    b2 = Ball(10, (20,40), start_v=(1,0))
    b3 = Ball(20, (35,35), start_v=(-0.5,-0.5))

    world = World([b1,b2,b3])
    world.run()
    world.plot()

if __name__ == '__main__':
    main()