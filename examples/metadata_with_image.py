#!/usr/bin/python3

# Obtain an image from the camera along with the exact metadata that
# that describes that image.

from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)

preview_config = picam2.preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

request = picam2.capture_request()
image = request.make_image("main") # image from the "main" stream
metadata = request.get_metadata()
request.release() # requests must always be returned to libcamera

image.show()
print(metadata)
