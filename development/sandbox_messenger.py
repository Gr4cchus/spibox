import os
import subprocess

filelist = []
# i = 0
for file in os.listdir("/home/pi/spibox/development/captures"):   # return list of entries
    print("\nHere is the ", file)
    if file.endswith(".jpg"):
        print("This ended with jpg", file)
        # ( '.png', '.gif', '.bmp', '.yuv', '.rgb', '.rgba', '.bgr', '.bgra', '.h264', '.mjpeg')
        print("File list inside if statement", filelist)
        # filelist.extend([None])    # extend list by appending from iterable
        # print("File extend has run the extend", filelist)
        # print("the var i=", i)
        filelist.append(file)
        # print("Heres after filelist[i] = file", filelist)
        # print("i = i + 1", i)

for filename in filelist:
    print('moving' + filename)
    pid = subprocess.call(['sudo', 'mv', '/home/pi/spibox/development/captures/' +
                           filename, '/home/pi/spibox/development/captures/archive/'])
