# main.py

import cv2
from src.config import MAX_STEPS
from src.simulation.simple_sim import Simple2DSim
from src.planning.a_star import a_star
from src.perception.vision import detect_lane, draw_lane_lines, detect_obstacles, draw_obstacle_boxes
from src.control.navigation import get_next_step, is_path_blocked
from src.utils.visualization import show_image, overlay_text

def run_simulation():
    sim = Simple2DSim()
    occ_grid = sim.get_occupancy_grid()

    # Initial path planning
    path = a_star(occ_grid, sim.robot_pos, sim.goal_pos)
    sim.set_path(path)

    if path is None:
        print("No path found from start to goal. Check map configuration.")
        return

    for step in range(MAX_STEPS):
        img = sim.render(draw_path=True)

        # Perception: lane detection
        lane_lines = detect_lane(img)
        img = draw_lane_lines(img, lane_lines)

        # Perception: obstacle detection (from rendered image)
        obstacle_bboxes = detect_obstacles(img)
        img = draw_obstacle_boxes(img, obstacle_bboxes)

        # Update occupancy grid if new obstacles are detected
        # (In this simple setup, obstacles are static, so occupancy grid is constant)

        # Check if path blocked (for dynamic obstacles, we would update occ_grid)
        if is_path_blocked(path, occ_grid):
            path = a_star(occ_grid, sim.robot_pos, sim.goal_pos)
            sim.set_path(path)
            if path is None:
                print("Path became blocked; re-planning failed.")
                break

        # Navigation: choose next step along the path
        next_pos = get_next_step(sim.robot_pos, path)
        sim.step_robot(next_pos)

        # Overlay debug text
        status_text = f"Step: {step} | Pos: {sim.robot_pos} | Goal: {sim.goal_pos}"
        img = overlay_text(img, status_text, pos=(10, 30))

        # Save frame
        sim.save_frame(img)

        # Show frame
        key = show_image("AI-Based Autonomous Navigation", img, delay=30)
        if key == ord('q'):
            break

        # Check goal
        if sim.reached_goal():
            print(f"Goal reached in {step} steps!")
            img = overlay_text(img, "GOAL REACHED", pos=(10, 60))
            show_image("AI-Based Autonomous Navigation", img, delay=2000)
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_simulation()