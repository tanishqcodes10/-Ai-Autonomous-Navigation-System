 AI-Based Autonomous Navigation System
 Overview

This project implements a simplified **AI-based autonomous navigation system** in a fully virtual 2D simulation environment using Python and OpenCV. The system demonstrates an end-to-end pipeline of **perception**, **path planning**, and **control**, similar to what is used in autonomous vehicles, warehouse robots, and delivery robots.

A simulated robot navigates from a start position to a goal while following a lane and avoiding obstacles using classical computer vision and A* path planning — all on a standard laptop, without any real hardware or GPU.

 Problem Statement

Design and implement an autonomous navigation system that:

- Perceives a lane and obstacles from camera-like images.
- Plans a safe path from start to goal using a grid-based map.
- Navigates the robot along that path while avoiding collisions.
- Runs entirely in simulation so it can be used as portfolio proof on GitHub.

Industry Relevance

Autonomous navigation is a core capability in:

- Self-driving cars and ADAS systems.
- Warehouse and factory autonomous mobile robots (AMRs/AGVs).
- Delivery robots, service robots, and inspection robots.
- Drones and smart mobility platforms.

Companies typically develop and validate such systems in virtual environments (e.g., CARLA, Gazebo) before deploying to real robots. This project mirrors that workflow at a student-friendly scale, making it ideal as a **proof-of-work** project for internships and placements.

Tech Stack

- **Language:** Python 3.10+
- **Libraries:**
  - NumPy
  - OpenCV (cv2)
  - Matplotlib (optional, for plots)
- **Concepts:**
  - Classical computer vision (Canny, Hough transform, color segmentation)
  - Grid-based A* path planning
  - Basic navigation and control
  - 2D simulation and visualization

Architecture

High-level pipeline:

1. **Map & Simulation**
   - Create a 2D grid world with a horizontal road, lane line, obstacles, and a robot.
   - Render the world into an RGB image for each simulation step.

2. **Perception (OpenCV)**
   - Lane detection using edge detection + Hough transform.
   - Obstacle detection using color segmentation (red blocks).

3. **Path Planning (A*)**
   - Construct an occupancy grid from the map.
   - Compute a collision-free path from start to goal using A*.

4. **Navigation / Control**
   - Follow the planned path cell by cell.
   - Replan if the path becomes blocked (extensible to dynamic obstacles).

5. **Visualization & Logging**
   - Display the simulation in real time using OpenCV.
   - Save frames for GIF/video creation.
   - Log run statistics.


Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/ai-autonomous-navigation-system.git
cd ai-autonomous-navigation-system
```

2. **Create a virtual environment**

```bash
python -m venv .venv   # Windows
# or
python3 -m venv .venv  # macOS / Linux
```

3. **Activate the environment**

```bash
.venv\Scripts\Activate.ps1   # Windows PowerShell
# or
source .venv/bin/activate    # macOS / Linux
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

 How to Run

From the project root:

```bash
python main.py
```

- A window titled **"AI-Based Autonomous Navigation"** will open.
- The green robot starts on the left and moves towards the goal on the right.
- Lane lines and obstacle bounding boxes are overlaid for visualization.
- Press `q` to quit early.

## Simulation Workflow

1. The map is generated as a grid with a central road and red obstacle columns.
2. A* computes an initial path from the start cell to the goal cell.
3. Each simulation step:
   - The world is rendered as an image.
   - Lane and obstacle detection are run on the image.
   - The robot moves to the next cell along the path.
   - Frames are displayed and optionally saved to `outputs/frames/`.
4. The run ends when the robot reaches the goal or the max number of steps is exceeded.

Results

- The robot successfully navigates from start to goal while staying on the road and passing through gaps between obstacles.
- The visualization shows:
  - Road and lane.
  - Red obstacles.
  - Planned path in red.
  - Green robot.
  - Obstacle bounding boxes and lane lines.

 Screenshots

Add your actual images here after running:

- `assets/images/navigation1.png`
- `assets/images/navigation2.png`
- `assets/images/output.png`
  

Example:

```markdown




```

## Future Improvements

- Real-time camera input (webcam) instead of synthetic images.
- Integration with ROS and Gazebo/CARLA for 3D robotics simulation.
- Improved lane detection (curved lanes, multiple lanes).
- Dynamic obstacles and real-time replanning.
- SLAM-based mapping and localization.
- Multi-robot navigation and coordination.
- Cloud-based dashboard and telemetry.
- Autonomous warehouse robot or drone-specific variants.

## Learning Outcomes

By working on this project you will:

- Understand the core building blocks of autonomous navigation systems.
- Gain practical experience with OpenCV for perception.
- Implement and tune A* path planning on grid maps.
- Build a small but complete robotics simulation pipeline in Python.
- Learn how to structure, document, and publish an industry-style project on GitHub.

## Author

- Tanishq Jakate – Student / AI Enthusiast  
- GitHub: [tanishqcodes10]()  
- LinkedIn: (www.linkedin.com/in/tanishq-jakate-93617a402)
