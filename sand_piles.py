# import matplotlib.pyplot as plt
# import numpy as np

class Grid:
	def __init__(self, MAX_SIZE, sand, square_size):
		self.MAX_SIZE = MAX_SIZE
		self.sc = sand
		self.h = square_size
		self.w = square_size

	def get_index(self, x, y):
		index = x + y * self.w
		return index

	def get_coords(self, index):
		pass

	def add_sand(self):
		pass

	def check_grid(self, grid):
		pass

	def display_grid(self):
		pass

def main():
	grid = Grid(10, 10, 10)

main()
