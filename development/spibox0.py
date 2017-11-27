#!/bin/bash
"""Setup components, take photos, and define their location and filename"""
# The PIR will always output low (0V) unless movement is detected, in which case it will output high (3.3V).
# PIR-OUT GPIO pin as an input, and use Python to detect any voltage change.


import RPi.GPIO as GPIO
import time
import datetime
import picamera
import os

try:
    def setup_gpio():
        """Setup GPIO pin numbering system,input pin, and resting resistor state i.e. high or low"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir_pin, GPIO.IN, GPIO.PUD_DOWN)

    def get_file_name():
        """Use datetime to create filename"""
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S" + '.jpg')

    def setup_picamera():
        """Setup picamera instance and parameters"""
        camera = picamera.PiCamera()    # careful, leaving this open keeps a hidden preview, draining battery.
        camera.resolution = (1024, 768)
        return camera

    def photo(camera):
        """Take photo and append filename"""
        print('Motion detected! Taking snapshot')
        os.chdir(working_directories[1])
        camera.capture(get_file_name(), format='jpeg')
        os.chdir(working_directories[0])

    def my_callback_take_photo(channel):
        """A Call back for a rising/falling edge event on PIR sensor to take a photo"""
        if GPIO.input(pir_pin):
            print("Rising Edge detected on pin %s" % channel)
            photo(initialized_camera)
        else:
            print("Falling edge detected")

    def directories():
        """Get a list of common working directories"""
        directory_listing = []
        directory_listing.append(os.getcwd())
        directory_listing.append('/home/pi/spibox/development/capture')
        return directory_listing

    def menu():
        """User menu options"""
        print("\n1: Start",
              "\n2: Set Camera initialization/adjustment time",
              "\n3: Start Webcam",
              "\n4: Quit")

    working_directories = directories()

    pir_pin = 4
    setup_gpio()
    print("GPIO pins set")
    initialized_camera = setup_picamera()
    print("Camera initialized")
    time.sleep(2)
    print("Warm-up time finished")

    # Multi-threaded callback
    GPIO.add_event_detect(pir_pin, GPIO.BOTH, callback=my_callback_take_photo)

    while True:
        print(GPIO.input(4))
        time.sleep(1)

# except KeyboardInterrupt:
#     print("  Bye for now")
#     GPIO.cleanup()
#     initialized_camera.close()
finally:
    print("Bye for now")
    initialized_camera.close()
    GPIO.cleanup()
