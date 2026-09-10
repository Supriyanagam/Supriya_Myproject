# Intelligent Driver Monitoring System

## Overview

The Intelligent Driver Monitoring System is a computer-vision prototype that monitors a driver's face through a camera and provides an alert when possible drowsiness or yawning is detected.

## Features

- Real-time camera monitoring
- Face detection
- Eye-state monitoring
- Yawning/smile-region detection
- Drowsiness alert
- Simple modular Python structure

## Technologies

- Python
- OpenCV
- Haar Cascade computer-vision models

## Project Structure

```text
Intelligent_Driver_Monitoring_System/
│
├── main.py
├── config.py
├── utils.py
├── alert.py
├── requirements.txt
├── README.md
├── .gitignore
└── models/
    └── README.md
```

## Requirements

- Python 3.9 or newer
- A webcam/camera
- OpenCV

## Installation

Create a virtual environment if desired:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Press `Q` to close the camera window.

## How It Works

1. The camera captures video frames.
2. OpenCV detects the driver's face.
3. The system checks whether eyes are being detected.
4. It checks the lower face for a mouth/smile-region pattern.
5. If a possible drowsiness or yawning condition remains for the configured time, an alert is generated.

## Important Note

This is an academic prototype. Haar Cascade detection can produce false positives and false negatives, so it should not be used as a safety-critical automotive system without proper validation and more robust models.

## Future Enhancements

- CNN/deep-learning based driver-state classification
- Face landmark detection and Eye Aspect Ratio (EAR)
- Head-pose estimation
- Phone-use detection
- Seat-belt detection
- Night-time/IR camera support
- GPS/GSM emergency notification
- Cloud dashboard and event logging
