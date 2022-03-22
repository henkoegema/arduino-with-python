#Created by Ian Neill 02-21-2022
#Reference to:  https://www.youtube.com/watch?v=h1DCbOOPD_k&t=3s

from dataclasses import dataclass
from vpython import *
import numpy as np
import time
import serial

scene.background = color.white
scene.width = 1200
scene.height = 600
scene.center = vector (-40,20,0)
efficiency = 0.95 #95%
amps = 10
therm = 11
gpm = 2

class aMeter:
    def __init__(self,mPos,scaleList,scaleH,mLabel):
        self.mPos = mPos
        self.scaleList = scaleList
        self.scaleH = scaleH
        self.mLabel = mLabel
        box(pos=vector(0,3,0)+self.mPos,size=vector(12,8,-.1),color=color.white)
        box(pos=vector(0,3,.5)+self.mPos,size=vector(12,8,1),color=color.white,opacity=.4)
        text(pos=vector(0,1.8,0)+self.mPos,text=mLabel,align='center',color=color.black)
        cylinder(pos=self.mPos,radius=.5,axis=vector(0,0,.5),color=color.black)
        for tic in np.linspace(4/5*pi,1/5*pi,((len(scaleList)-1)*5)+1):
            box(pos=vector(5*cos(tic),5*sin(tic),.1)+self.mPos,axis=vector(cos(tic),sin(tic),0),size=vector(.3,.1,0.2),color=color.black)
        
        ct=0
        for tic in np.linspace(4/5*pi,1/5*pi,len(scaleList)):
            box(pos=vector(5*cos(tic),5*sin(tic),.1)+self.mPos,axis=vector(cos(tic),sin(tic),0),size=vector(.5,.1,0.2),color=color.black)
            text(pos=vector(5*1.1*cos(tic),5*1.1*sin(tic),0)+self.mPos,axis=rotate(vector(cos(tic),sin(tic),0),angle=-pi/2),text=str(self.scaleList[ct]),align='center',color=color.black,height=self.scaleH)

            ct += 1

        self.ptr=arrow(pos=vector(0,0,.4)+self.mPos,axis=vector(0,5,0),shaftwidth=0.2,headwidth=0.2,color=color.red)

    def update(self,value):
        self.value=value
        self.ptr.axis=vector(5*cos(self.value),5*sin(self.value),0)

def mapThis(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

arduPort = serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)

########## Radiator ##########
extrusion(path=[vector(0,0,0),vector(0,27,0)],color=[color.red,color.blue],shape=[[shapes.ellipse(pos=(i,0),width=.3,height=1)]for i in range(0,25,1)])

########## Piping ##########
cylinder(pos=vector(0,27,-25),radius=1,axis=vector(0,0,30),color=color.blue)
cylinder(pos=vector(0,0,-25),radius=1,axis=vector(0,0,32),color=color.red)
cylinder(pos=vector(1,0,7),radius=1,axis=vector(-65,0,0),color=color.blue)
cylinder(pos=vector(-70,42,-2),radius=1,axis=vector(0,0,10),color=color.red)
cylinder(pos=vector(-70,42,7),radius=1,axis=vector(0,-30,0),color=color.red)
cylinder(pos=vector(-71,12,7),radius=1,axis=vector(7,0,0),color=color.red)
cylinder(pos=vector(-64,13,7),radius=1,axis=vector(0,-14,0),color=color.red)
cylinder(pos=vector(-70,7,-2),radius=1,axis=vector(0,0,5),color=color.blue)
cylinder(pos=vector(-71,7,3),radius=1,axis=vector(52,0,0),color=color.blue)
cylinder(pos=vector(1,27,5),radius=1,axis=vector(-19,0,0),color=color.blue)
cylinder(pos=vector(-18,27,5),radius=2,axis=vector(-.3,0,0),color=color.blue)
cylinder(pos=vector(-20,22,3),radius=1,axis=vector(0,-15,0),color=color.blue)
cylinder(pos=vector(-20,22,3),radius=1.5,axis=vector(0,-.3,0),color=color.blue)

########## Boiler ##########
cylinder(pos=vector(-70,25,-2),radius=20,axis=vector(0,0,-70),texture=textures.metal,color=color.yellow)
box(pos=vector(-70,5,-37),size=vector(30,30,68),color=color.red,texture=textures.stucco)

########## Blower ##########
fan=[]
bladeSize=vector(12,8,.5)
radBlade=6.5
for blades in np.linspace(0,2*pi,5,False):
    bladevect=vector(radBlade*sin(blades),radBlade*cos(blades),0)
    fan.append(ellipsoid(pos=bladevect,axis=bladevect,size=bladeSize,color=color.yellow))
    fan[-1].rotate(angle=pi/8,axis=bladevect)
fan.append(cylinder(radius=3,axis=vector(0,0,2),color=color.yellow))
fan.append(cylinder(radius=14,axis=vector(0,0,1),color=color.white,opacity=.01))
blower=compound(fan,pos=vector(-5,14,-12.5),axis=vector(0,0,1))
cylinder(pos=vector(-6.5,14,-12.5),axis=vector(-6,0,0),radius=4,color=color.black)

########## Water Pump ##########
fan=[]
bladeSize=vector(4,3,.5)
radBlade=1.5
for blades in np.linspace(0,2*pi,7,False):
    bladevect=vector(radBlade*sin(blades),radBlade*cos(blades),0)
    fan.append(ellipsoid(pos=bladevect,axis=bladevect,size=bladeSize,color=color.yellow))
    fan[-1].rotate(angle=pi/2,axis=bladevect)
fan.append(cylinder(radius=1,pos=vector(0,0,-.5),axis=vector(0,0,2),color=color.yellow))
fan.append(ring(pos=vector(0,0,0),axis=vector(0,0,1),thickness=1.7,radius=2,color=color.white,opacity=.7))
pump=compound(fan,pos=vector(-20,27,5),axis=vector(0,0,1))
cylinder(radius=1.5,pos=vector(-20,27,3),axis=vector(0,-5,0),color=color.white,opacity=.7) 
cylinder(pos=vector(-23,27,5),axis=vector(-8,0,0),radius=3,color=color.black)
cylinder(pos=vector(-23,27,5),axis=vector(1.5,0,0),radius=2,color=color.black)

########## Thermometer ##########
cylinder(pos=vector(-64,13,7),axis=vector(0,20,0),radius=.4,color=color.white,opacity=.3)
sphere(pos=vector(-64,33,7),radius=.4,color=color.white,opacity=.1)
thermReading=cylinder(pos=vector(-64,13,7),radius=.2,axis=vector(0,11,0),color=color.red)
cylinder(pos=vector(-64,13,7),radius=.6,axis=vector(0,2,0),color=color.black)
box(pos=vector(-64,24,6.5),size=vector(4,20,.1),color=color.white)

for tic in np.linspace(16,32,17):
    box(pos=vector(-63,tic,6.6),size=vector(.3,.1,0.2),color=color.black)

extrusion(path=[vector(-65,16,6.60),vector(-65,24,6.60),vector(-65,32,6.60)],color=[color.blue,color.green,color.red],shape=shapes.ellipse(width=.1,height=.4))


m1=aMeter(vector(-25,33,0),[1,1.5,2,2.5,3,3.5,4],.7,'L/Min')
m2=aMeter(vector(-8,32,0),[200,400,600.800,1000,1200],.5, 'RPMs')
m3=aMeter(vector(-82,25,-2),[0,100,200,300,400,500],.5,'Volts DC')
ss=label(pos=vector(-50,50,0),text='')

while True:
    rate(30)
    blower.rotate(-pi/8, axis=vector(1,0,0))
    pump.rotate(-pi/8, axis=vector(1,0,0))
    if (arduPort.in_waiting > 0):
        data = arduPort.read_until()
        data = data.decode()
        data = data[:-2]
        data = data.split(':')
        data = [int(i) for i in data]
        print(data[0])
        value1=mapThis(data[0],0,1023,4/5*pi,1/5*pi)
        gpm = mapThis(data[0],0,1023,1,4)
        m1.update(value1)
        value2 = mapThis(data[1],0,1023,4/5*pi,1/5*pi)
        rpm = mapThis(data[1],0,1023,200,1200)
        m2.update(value2)
        value3 = mapThis(data[2],0,1023,4/5*pi,1/5*pi)
        volts = mapThis(data[2],0,1023,0,500)
        m3.update(value3)

        ##### Calculate Temperature #####
        systemNet = ((volts * amps * efficiency) / 5000) - ((gpm * rpm)/5000)
        therm += systemNet /10
        therm = min(19, max(3, therm))
        thermReading.axis.y = therm
        ss.text = str(round(systemNet,2))
        













