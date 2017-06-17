#!/bin/sh
"""Read configuration file, file captures, archive & move captures, and package captures to email."""
# messenger0.py
# look for files in the capture directory then process them
import os
import subprocess
import configparser
import time


class SpiboxMessenger:
    """Create the messenger"""
    def __init__(self):
        """Initialize the ConfigParser"""
        spibox_conf = configparser.ConfigParser()
        spibox_conf.read('/home/pi/spibox/development/spibox.conf')
        self.emailsubject = spibox_conf.get('email', 'emailsubject')
        self.emailrecipient = spibox_conf.get('email', 'emailrecipient')
        self.emailon = spibox_conf.get('email', 'on')
        print(self.emailrecipient)

    def get_file_list(self):
        """Create photo file list of camera captures"""
        self.filelist = []
        for file in os.listdir("/home/pi/spibox/development/capture"):   # return list of entries
            if file.endswith(".jpg"):
                # ( '.png', '.gif', '.bmp', '.yuv', '.rgb', '.rgba', '.bgr', '.bgra', '.h264', '.mjpeg')
                self.filelist.append(file)

    def move_files(self):
        """Natively move files from filelist into archive"""
        for filename in self.filelist:
            print('moving' + filename)
            pid = subprocess.call(['sudo', 'mv', '/home/pi/spibox/development/captures/' +
                                   filename, '/home/pi/spibox/development/captures/archive/'])

    def email_files(self):
        """mpack each file into MIME format and send off"""
        print(len(self.filelist))
        for filename in self.filelist:
            print('emailing' + filename)
            # by default mpack -c will check for file type
            # -s subject, -c content type, encoded the named file, mail to recipient
            cmd = 'mpack -s "'+self.emailsubject+'" -c image/jpeg /home/pi/spibox/development/captures/' \
                  + filename + ' '+self.emailrecipient
            pid = subprocess.call(cmd, shell=True)  # could possibly shlex.split cmd to shell=False


messenger = SpiboxMessenger()
while True:
    time.sleep(10)
    messenger.__init__()
    messenger.get_file_list()
    if messenger.emailon == "YES":
        messenger.email_files()
    messenger.move_files()
