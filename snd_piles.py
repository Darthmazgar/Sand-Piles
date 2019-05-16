import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


class SandPiles:
    def __init__(self,N):
        self.N = N
        self.grid = np.zeros((N,N))
        self.animation = True
        self.grains_per_update = 1
        self.MPH = 3

    def topple_towers(self):
        all_toppled = False
        while not all_toppled:
            cnt = 0
            for i in range(self.N):
                for j in range(self.N):
                    if self.MPH == 4:
                        if self.grid[i][j] >= self.MPH:
                            cnt += 1
                            self.grid[i][j] -= self.MPH
                            self.grid[(i+1) % self.N][j] += 1
                            self.grid[(i-1) % self.N][j] += 1
                            self.grid[i][(j+1) % self.N] += 1
                            self.grid[i][(j-1) % self.N] += 1
                    elif self.MPH == 8:
                        if self.grid[i][j] >= self.MPH:
                            cnt += 1
                            self.grid[i][j] -= self.MPH
                            self.grid[(i+1) % self.N][j] += 1
                            self.grid[(i+1) % self.N][(j+1) % self.N] += 1
                            self.grid[(i+1) % self.N][(j-1) % self.N] += 1
                            self.grid[(i-1) % self.N][j] += 1
                            self.grid[(i-1) % self.N][(j+1) % self.N] += 1
                            self.grid[(i-1) % self.N][(j-1) % self.N] += 1
                            self.grid[i][(j+1) % self.N] += 1
                            self.grid[i][(j-1) % self.N] += 1  
                    else:
                        if self.grid[i][j] >= self.MPH:
                            original = self.grid[i][j]
                            choices = np.array([self.grid[(i+1) % self.N][j], self.grid[(i-1) % self.N][j], self.grid[i][(j+1) % self.N], self.grid[i][(j-1) % self.N]])
                            while original - self.MPH <= self.grid[i][j]:
                                self.grid[i][j] -= 1
                                choice = np.random.choice(choices)
                                choice += 1


            if cnt == 0:
                all_toppled = True

    def add_sand(self, x=None, y=None):
        if not x:
            x = int(self.N / 2)
        if not y:
            y = int(self.N / 2)
        self.grid[x][y] += 1

    def update(self, k):
        for z in range(self.grains_per_update):
            self.add_sand()
            self.topple_towers()
        if self.animation:  # If animating then plot slice.
            self.fig.clear()
            plt.title("Sand Piles")
            plt.imshow(self.grid, interpolation='nearest',
                           cmap='coolwarm', origin='lower')
            plt.colorbar()

    def run_animation(self):
        self.animation = True
        self.fig = plt.figure()
        anim_running = True
        def onClick(event):
            nonlocal anim_running
            if anim_running:
                print("Paused.")
                anim.event_source.stop()
                anim_running = False
            else:
                print("Resume.")
                anim.event_source.start()
                anim_running = True
        self.fig.canvas.mpl_connect('button_press_event', onClick)
        anim = FuncAnimation(self.fig, self.update, interval=25)
        plt.show()

def main():
    s = SandPiles(50)
    s.run_animation()

if __name__ == '__main__':
    main()