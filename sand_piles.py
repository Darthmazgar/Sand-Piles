# import matplotlib.pyplot as plt
import numpy as np

class Grid:
	def __init__(self, MAX_SIZE, sand, square_size):
		self.MAX_SIZE = MAX_SIZE  # Square size, this is a max side size
		self.sc = sand
		self.h = square_size
		self.w = square_size
		self.MPH = 4  # Max pile height
		self.grid = np.zeros([self.w, self.h])

	def get_index(self, x, y):
		if x >= self.w or y >= self.h:
			return False
		index = x + y * self.w
		if index > self.MAX_SIZE**2:
			return False
		else:
			return index

	def get_coords(self, index):
		x = index % self.w
		y = int(index / self.w)
		if x >= self.w or y >= self.h:
			return False
		else:
			return [x, y]

	def add_sand(self, x=True, y=True):
		if x and y:
			x = int(self.w/2)  # Sets default to the middle of the grid
			y = int(self.h/2)

		self.grid[x][y] += 1
		return self.grid

	def topple_sand(self, x, y):
		self.grid[x][y] -= 4
		self.grid[x][y+1] += 1
		self.grid[x][y-1] += 1
		self.grid[x+1][y] += 1
		self.grid[x-1][y] += 1
		return 0


	def check_grid(self, grid):
		pass

	def display_grid(self):
		print(self.grid)


def main():
	grid = Grid(10, 10, 11)
	for i in range(9):
		grid.add_sand()
		grid.display_grid()

main()
