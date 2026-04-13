# src/planning/a_star.py

import heapq

def heuristic(a, b):
    """Manhattan distance heuristic for grid."""
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(node, grid_width, grid_height):
    """4-connected neighbors (up, down, left, right)."""
    (x, y) = node
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            neighbors.append((nx, ny))
    return neighbors

def a_star(occupancy_grid, start, goal):
    """
    Run A* on a 2D occupancy grid.

    occupancy_grid: 2D array, 0 = free, 1 = obstacle
    start, goal: (x, y) tuples in grid coordinates
    """
    grid_height, grid_width = occupancy_grid.shape

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in get_neighbors(current, grid_width, grid_height):
            x, y = neighbor
            if occupancy_grid[y, x] == 1:  # obstacle
                continue

            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # no path found