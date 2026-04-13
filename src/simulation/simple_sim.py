# src/simulation/simple_sim.py

import os
import cv2
import numpy as np
from src.config import (
    GRID_WIDTH, GRID_HEIGHT, CELL_SIZE,
    COLOR_BG, COLOR_ROAD, COLOR_LANE,
    COLOR_OBSTACLE, COLOR_ROBOT, COLOR_PATH,
    ROBOT_START, ROBOT_GOAL,
    OBSTACLE_COLUMNS, OBSTACLE_GAP_HEIGHT,
    SAVE_FRAMES, FRAMES_DIR
)

class Simple2DSim:
    """
    Simple 2D grid-based simulation rendered as an image.
    """

    def __init__(self):
        # 0 = free, 1 = obstacle, 2 = road
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=np.int32)
        self._create_road_and_obstacles()
        self.robot_pos = ROBOT_START  # (x, y)
        self.goal_pos = ROBOT_GOAL
        self.step_count = 0
        self.path = None

        if SAVE_FRAMES and not os.path.exists(FRAMES_DIR):
            os.makedirs(FRAMES_DIR, exist_ok=True)

    def _create_road_and_obstacles(self):
        """
        Create a horizontal road across the map and place obstacles with gaps.
        """
        # Mark a horizontal road band
        road_y_min = GRID_HEIGHT // 2 - 5
        road_y_max = GRID_HEIGHT // 2 + 5
        self.grid[road_y_min:road_y_max, :] = 2  # road

        # Place vertical obstacles on the road
        for col in OBSTACLE_COLUMNS:
            gap_center = GRID_HEIGHT // 2
            gap_y_min = gap_center - OBSTACLE_GAP_HEIGHT // 2
            gap_y_max = gap_center + OBSTACLE_GAP_HEIGHT // 2
            for y in range(road_y_min, road_y_max):
                if not (gap_y_min <= y <= gap_y_max):
                    self.grid[y, col] = 1  # obstacle

    def reset(self):
        self.__init__()

    def set_path(self, path):
        self.path = path

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT

    def is_obstacle(self, pos):
        x, y = pos
        return self.grid[y, x] == 1

    def step_robot(self, next_pos):
        """
        Move robot to next_pos if valid, otherwise stay.
        """
        if self.in_bounds(next_pos) and not self.is_obstacle(next_pos):
            self.robot_pos = next_pos
        self.step_count += 1

    def reached_goal(self):
        return self.robot_pos == self.goal_pos

    def get_occupancy_grid(self):
        """
        Returns a 2D array: 0 = free, 1 = obstacle.
        """
        occ = (self.grid == 1).astype(np.int32)
        return occ

    def render(self, draw_path=True):
        """
        Render the grid, robot, goal, and optional path into a BGR image.
        """
        h = GRID_HEIGHT * CELL_SIZE
        w = GRID_WIDTH * CELL_SIZE
        img = np.zeros((h, w, 3), dtype=np.uint8)
        img[:] = COLOR_BG

        # Draw road and obstacles
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell = self.grid[y, x]
                px = x * CELL_SIZE
                py = y * CELL_SIZE
                if cell == 2:  # road
                    cv2.rectangle(
                        img,
                        (px, py),
                        (px + CELL_SIZE - 1, py + CELL_SIZE - 1),
                        COLOR_ROAD,
                        thickness=-1,
                    )
                elif cell == 1:  # obstacle
                    cv2.rectangle(
                        img,
                        (px, py),
                        (px + CELL_SIZE - 1, py + CELL_SIZE - 1),
                        COLOR_OBSTACLE,
                        thickness=-1,
                    )

        # Draw lane centerline (simple horizontal line on the road)
        center_y = GRID_HEIGHT // 2
        cv2.line(
            img,
            (0, center_y * CELL_SIZE + CELL_SIZE // 2),
            (w, center_y * CELL_SIZE + CELL_SIZE // 2),
            COLOR_LANE,
            thickness=2,
        )

        # Draw path
        if draw_path and self.path is not None:
            for (x, y) in self.path:
                px = x * CELL_SIZE
                py = y * CELL_SIZE
                cv2.rectangle(
                    img,
                    (px, py),
                    (px + CELL_SIZE - 1, py + CELL_SIZE - 1),
                    COLOR_PATH,
                    thickness=1,
                )

        # Draw goal
        gx, gy = self.goal_pos
        cv2.circle(
            img,
            (gx * CELL_SIZE + CELL_SIZE // 2, gy * CELL_SIZE + CELL_SIZE // 2),
            CELL_SIZE // 2,
            (255, 255, 0),
            thickness=2,
        )

        # Draw robot
        rx, ry = self.robot_pos
        cv2.rectangle(
            img,
            (rx * CELL_SIZE, ry * CELL_SIZE),
            (rx * CELL_SIZE + CELL_SIZE - 1, ry * CELL_SIZE + CELL_SIZE - 1),
            COLOR_ROBOT,
            thickness=-1,
        )

        return img

    def save_frame(self, img):
        if not SAVE_FRAMES:
            return
        frame_path = os.path.join(FRAMES_DIR, f"frame_{self.step_count:04d}.png")
        cv2.imwrite(frame_path, img)