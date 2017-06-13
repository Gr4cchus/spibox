"""Basic Template Testing PiCamera Preview"""
# The PIR will always output low (0V) unless movement is detected, in which case it will output high (3.3V).
# PIR-OUT GPIO pin as an input, and use Python to detect any voltage change.


import RPi.GPIO as GPIO
import time
import datetime
import picamera

try:
    def get_file_name():
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    GPIO.setmode(GPIO.BCM)
    PIR_Pin = 4
    GPIO.setup(PIR_Pin, GPIO.IN)
# Instance created
    camera = picamera.PiCamera()

    print("Starting test")
    time.sleep(2)
    print("Rdy")
    camera.start_preview()

    # while True:
    #     if GPIO.input(PIR_Pin):
    #         print(GPIO.input(4))
    #         print("Motion Detected!")   # input is high
    #         captured_picture = get_file_name() + '.jpg'
    #         camera.capture(captured_picture)
    #     time.sleep(1)

except KeyboardInterrupt:
    print("  Bye for now")
    GPIO.cleanup()
import picamera
camera = picamera.PiCamera()
camera.start_preview()
