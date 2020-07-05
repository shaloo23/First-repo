#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:31:28 2020

@author: shaloo
"""
import math
import time

U = float(input('initial velocity: '))
_o = float(input('angle of throwing in degrees: '))

pi=math.pi
o = pi*(_o)/180
g = 9.81
t=0

Ux = U*(math.cos(o))
print(Ux)
Uy = U*(math.sin(o))

def velocity(Ux,Uy,t):
    Vx=Ux
    Vy=Uy-(g*t)
    print('vertical component of velocity','%.2f'%Vy)
    print('horizontal component of velocity','%.2f'%Vx)

def position(Ux,Uy,t):
    Px=Ux*t
    Py=Uy*t-(0.5*g*(t*t))
    print('vertical component of positon','%.2f'%Py)
    print('horizontal component of position','%.2f'%Px,'\n')
    
while True:
    if t<=(2*Uy/g):
        time.sleep(1)
        print('time','%.2f'%t)
        velocity(Ux,Uy,t)
        position(Ux,Uy,t)
        t=t+0.1
    else:
        time.sleep(1)
        t=(2*Uy/g)
        print('time','%.2f'%t)
        velocity(Ux,Uy,t)
        position(Ux,Uy,t)
        break
    
  

