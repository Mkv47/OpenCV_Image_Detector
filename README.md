# Screen Template Matching Scanner

A simple Python tool to capture your screen and detect occurrences of a specified image template using OpenCV and MSS.  
Control scanning and quitting with keyboard inputs.

---

## Features

- Press **`s`** to scan the primary monitor for the template image.
- Detects and prints coordinates of all matches found.
- Press **`q`** to quit the program gracefully.
- Uses normalized cross-correlation for template matching.

---

## Requirements

- Python 3.x
- [mss](https://pypi.org/project/mss/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)
- [keyboard](https://pypi.org/project/keyboard/)

---

## Installation

Install dependencies with pip:

```bash
pip install mss opencv-python numpy keyboard

