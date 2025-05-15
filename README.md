#Screen Template Matching Scanner
This project captures your screen and searches for a specific image template within the screenshot. It uses Python libraries mss for screen capture, OpenCV for image processing, and keyboard to control the scanning with keyboard input.

Features
Continuously listens for keyboard commands:

Press s to scan the screen for the template image.

Press q to quit the program.

Detects all matching locations of the template image on your screen.

Prints the coordinates of detected matches.

Requirements
Python 3.x

mss

opencv-python

numpy

keyboard

Installation
Install the required Python packages using pip:

bash
Copy
Edit
pip install mss opencv-python numpy keyboard
Usage
Place your template image at ./image/image.png.

Run the script.

Press s to scan your primary monitor for the template.

Coordinates of detected matches will be printed in the console.

Press q to exit the program.

How It Works
The script loads a grayscale template image.

When you press s, it grabs a screenshot of your primary monitor.

Converts the screenshot to grayscale and searches for the template using OpenCV's matchTemplate method.

Prints the position(s) where the template matches above a defined threshold (default 0.8).

Notes
Make sure the template image matches what you expect on screen (same resolution, no scaling).

The matching threshold can be adjusted in the script for more or fewer detections.
