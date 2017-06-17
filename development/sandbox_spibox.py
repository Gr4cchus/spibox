"""Basic Template"""
# The PIR will always output low (0V) unless movement is detected, in which case it will output high (3.3V).
# PIR-OUT GPIO pin as an input, and use Python to detect any voltage change.

# import GPIO library
import RPi.GPIO as GPIO
import time
import picamera
import datetime


# set GPIO pin numbering, BOARD or BCM and input pin/channels
try:
    def get_file_name():
        """Use datetime to create filename"""
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    GPIO.setmode(GPIO.BCM)
    PIR_Pin = 4
    GPIO.setup(PIR_Pin, GPIO.IN)

# Notify program startup
    print("Starting test")
    time.sleep(2)
    print("Rdy")

    # Instance created
    camera = picamera.PiCamera()  # careful, leaving this open keeps a hidden preview, draining battery.
    camera.resolution = (1024, 768)

# Check input status of PIR_Pin
    while True:
        if GPIO.input(PIR_Pin):
            print(GPIO.input(4))
            print("Motion Detected!")   # input is high
            camera.capture(get_file_name(), format='jpeg')
        time.sleep(1)

except KeyboardInterrupt:
    print("  Bye for now")
# Reset GPIO
    GPIO.cleanup()