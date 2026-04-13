# src/control/navigation.py

from src.config import GRID_WIDTH, GRID_HEIGHT

def get_next_step(robot_pos, path):
    """
    Given current robot position and path (list of (x, y) cells),
    choose the next cell to move to.
    """
    if not path:
        return robot_pos

    # Find robot index in path (approximate)
    try:
        idx = path.index(robot_pos)
    except ValueError:
        # If not exactly on the path, find closest point
        dists = [(abs(px - robot_pos[0]) + abs(py - robot_pos[1]), i)
                 for i, (px, py) in enumerate(path)]
        dists.sort()
        idx = dists[0][1]

    # Move to next point if exists
    next_idx = min(idx + 1, len(path) - 1)
    next_pos = path[next_idx]
    return next_pos

def is_path_blocked(path, occupancy_grid):
    """
    Simple check: if any cell in the path is now an obstacle, consider blocked.
    """
    if path is None:
        return True
    for (x, y) in path:
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True
        if occupancy_grid[y, x] == 1:
            return True
    return False
