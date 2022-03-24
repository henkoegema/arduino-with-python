#Using an Arduino with Python LESSON 11: Controlling an LED from Python
#https://www.youtube.com/watch?v=VdSFwYrYqW0&t=683s

import serial
from vpython import *

arduinoData = serial.Serial('/dev/ttyACM0',115200)

myOrb = sphere(color = color.black, radius = 1)

while True:
    myCmd = input('Please input your color R:G:B 0-255 ')
    myCmd = myCmd + '\r'
    arduinoData.write(myCmd.encode())
    myColor = myCmd.split(':')
    red = int(myColor[0])
    green = int(myColor[1])
    blue = int(myColor[2])

    myOrb.color = vector(red / 255, green / 255, blue / 255)


     