# src/config.py

import numpy as np

# Map configuration
GRID_WIDTH = 80      # number of cells in X
GRID_HEIGHT = 60     # number of cells in Y
CELL_SIZE = 20       # pixels per cell for rendering

# Colors (BGR for OpenCV)
COLOR_BG = (30, 30, 30)
COLOR_ROAD = (70, 70, 70)
COLOR_LANE = (200, 200, 200)
COLOR_OBSTACLE = (0, 0, 255)
COLOR_ROBOT = (0, 255, 0)
COLOR_PATH = (255, 0, 0)

# Robot configuration
ROBOT_START = (5, GRID_HEIGHT // 2)         # (x, y) in grid cells
ROBOT_GOAL = (GRID_WIDTH - 5, GRID_HEIGHT // 2)

# Simulation
MAX_STEPS = 500
SAVE_FRAMES = True
FRAMES_DIR = "outputs/frames"

# Map obstacles configuration (simple vertical obstacles in the road)
OBSTACLE_COLUMNS = [20, 35, 45]   # x positions
OBSTACLE_GAP_HEIGHT = 6          # vertical gap in cells for robot to pass

np.random.seed(42)