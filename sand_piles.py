# import matplotlib.pyplot as plt
# import numpy as np

class Grid:
	def __init__(self, MAX_SIZE, sand, square_size):
		self.MAX_SIZE = MAX_SIZE
		self.sc = sand
		self.h = square_size
		self.w = square_size

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

	def add_sand(self):
		pass

	def check_grid(self, grid):
		pass

	def display_grid(self):
		pass

def main():
	grid = Grid(10, 10, 10)
	for i in range(10):
		for j in range(10):
			print(grid.get_index(j, i))

main()
