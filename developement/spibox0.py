"""Basic Template"""
# The PIR will always output low (0V) unless movement is detected, in which case it will output high (3.3V).
# PIR-OUT GPIO pin as an input, and use Python to detect any voltage change.

# import GPIO library
import RPi.GPIO as GPIO
import time

# set GPIO pin numbering, BOARD or BCM and input pin/channels
try:
    GPIO.setmode(GPIO.BCM)
    PIR_Pin = 4
    GPIO.setup(PIR_Pin, GPIO.IN)

# Notify program startup
    print("Starting test")
    time.sleep(2)
    print("Rdy")

# Check input status of PIR_Pin
    while True:
        if GPIO.input(PIR_Pin):
            print(GPIO.input(4))
            print("Motion Detected!")   # input is high
        time.sleep(1)

except KeyboardInterrupt:
    print("  Bye for now")
# Reset GPIO
    GPIO.cleanup()