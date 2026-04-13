# src/perception/vision.py

import cv2
import numpy as np

def detect_lane(image):
    """
    Detects lane line in the image using Canny + Hough.
    Returns a list of lines (x1, y1, x2, y2).
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=50,
        maxLineGap=10
    )

    detected_lines = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            detected_lines.append((x1, y1, x2, y2))
    return detected_lines

def draw_lane_lines(image, lines, color=(255, 255, 255), thickness=2):
    """
    Overlay detected lane lines on image.
    """
    if lines is None:
        return image
    out = image.copy()
    for (x1, y1, x2, y2) in lines:
        cv2.line(out, (x1, y1), (x2, y2), color, thickness)
    return out

def detect_obstacles(image):
    """
    Detect obstacles by color segmentation (red rectangles).
    Returns a list of bounding boxes (x, y, w, h).
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Lower/upper red ranges
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bboxes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Filter small detections
        if w * h > 50:
            bboxes.append((x, y, w, h))
    return bboxes

def draw_obstacle_boxes(image, bboxes, color=(0, 255, 255), thickness=2):
    out = image.copy()
    for (x, y, w, h) in bboxes:
        cv2.rectangle(out, (x, y), (x + w, y + h), color, thickness)
    return out