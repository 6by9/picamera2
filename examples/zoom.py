#!/usr/bin/python3

# How to do digital zoom using the "ScalerCrop" control.

from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)

preview_config = picam2.preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

size = picam2.sensor_resolution

for i in range(20):
    # This syncs us to the arrival of a new camera frame:
    picam2.capture_metadata()

    size = [int(s * 0.95) for s in size]
    offset = [(r - s) // 2 for r, s in zip(picam2.sensor_resolution, size)]
    picam2.set_controls({"ScalerCrop": offset + size})

time.sleep(2)
