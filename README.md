# Moduler Screen Template Matching Scanner

A Python module for detecting occurrences of a specific image template on your screen using OpenCV and MSS.  
Designed for easy integration into other projects, allowing you to scan your screen programmatically with simple function calls.

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

