# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:28:47 2019

@author: bmcn6

Sources:
    https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
    
What to do:
    Type "1" for category 1,
    "2" for category 2
    "quit" to finish training
"""

import serial
import cv2       
import time                
import os                  

#settings for creating the servo control
arduino = serial.Serial('COM3', 9600)   # create serial object named arduino

'''while True:                                             # create loop
    command = str(input ("Servo position: "))       # query servo position
    arduino.write(str.encode(command))                          # write position to serial port
    reachedPos = str(arduino.readline())            # read serial port for arduino echo
    print(reachedPos)                               # print arduino echo to console
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

# Move servo to start position
servo_Pos = '90'
arduino.write(str.encode(servo_Pos))                          # write position to serial port
reachedPos = str(arduino.readline())            # read serial port for arduino echo
print(reachedPos)                               # print arduino echo to console

while True:  # TODO this camera feed isn't continuous
    command = str(input ("Item Category (1 or 2): "))
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if command == 'quit':
        # ESC pressed
        print("Escape hit, closing...")
        break
    
    elif command == '1':
        # Take Image
        os.chdir('D:\Documents\PythonProjects\BeanSorter\TrainingData\Category1')
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        time.sleep(1)
        
        #Move Servo
        servo_Pos = '0'
        arduino.write(str.encode(servo_Pos))                          # write position to serial port
        reachedPos = str(arduino.readline())            # read serial port for arduino echo
        print(reachedPos)                               # print arduino echo to console
        time.sleep(1)
        arduino.write(str.encode('90'))                          # write position to serial port
        print("reset position 1")
        
    elif command == '2':
        # Take Image
        os.chdir('D:\Documents\PythonProjects\BeanSorter\TrainingData\Category2')
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        time.sleep(1)
        
        #Move Servo
        servo_Pos = '160'
        arduino.write(str.encode(servo_Pos))                          # write position to serial port
        reachedPos = str(arduino.readline())            # read serial port for arduino echo
        print(reachedPos)                               # print arduino echo to console
        time.sleep(2)
        arduino.write(str.encode('90'))                          # TODO write this bigger
        print("reset position 2")
        
    
        
cam.release()

cv2.destroyAllWindows()

arduino.close()