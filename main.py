import mss
import cv2 as cv
import numpy as np
import keyboard

template = cv.imread("./image/image.png", cv.IMREAD_GRAYSCALE)
if template is None:
    print("Template image not found.")
    exit()

print("Press 's' to scan for matches, 'q' to quit.")

while True:
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break

    if keyboard.is_pressed('s'):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = np.array(sct.grab(monitor))
            frame = cv.cvtColor(screenshot, cv.COLOR_BGRA2BGR)
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            result = cv.matchTemplate(frame_gray, template, cv.TM_CCOEFF_NORMED)
            threshold = 0.8
            locations = np.where(result >= threshold)
            locations = list(zip(*locations[::-1]))  # (x, y)

            if locations:
                for pt in locations:
                    center_x = pt[0]
                    center_y = pt[1]
                    print(f"Match at: ({center_x}, {center_y})")
            else:
                print("No match found.")

        keyboard.wait('s', suppress=True)