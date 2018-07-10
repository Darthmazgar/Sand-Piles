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
		self.next_grid = self.grid

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
		#print(x, y)
		self.next_grid[x][y] -= self.MPH
		if x > 0 and y < self.w:
			self.next_grid[y][x+1] += 1
			self.next_grid[y][x-1] += 1
		if y > 0 and x < self.h:
			self.next_grid[y+1][x] += 1
			self.next_grid[y-1][x] += 1
		return 0

	def check_grid(self):
		complete = True
		for i in range(self.h-1):  # Not sure about the -1s here
			for j in range(self.w-1):
				if self.grid[j][i] >= self.MPH:
					if complete:
						complete = False
					self.topple_sand(j, i)
		return complete

	def complete_update(self):
		self.grid = self.next_grid
		return 0

	def display_grid(self):
		print(self.grid)
		return 0

	def add_all_sand(self):
		for i in range(self.sc):
			self.add_sand()
			cond = False
			while not cond:
				cond = self.check_grid()
			self.complete_update()
		return 0


def main():
	grid = Grid(10, 20, 9)
	grid.add_all_sand()
	grid.display_grid()

main()
