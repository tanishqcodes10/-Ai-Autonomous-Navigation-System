# src/utils/visualization.py

import cv2

def show_image(window_name, image, delay=1):
    cv2.imshow(window_name, image)
    key = cv2.waitKey(delay) & 0xFF
    return key  # can be used to quit on 'q'

def overlay_text(image, text, pos=(10, 30)):
    out = image.copy()
    cv2.putText(
        out,
        text,
        pos,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )
    return out