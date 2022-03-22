#!/usr/bin/env python
"""Functions for modeling ROSBot"""

#from inspect import _Object
from xml.dom.expatbuilder import ElementInfo
import numpy as np
from math import cos, sin
#import me416_utilities
from std_msgs.msg import String

def model_parameters():
    """Returns two constant model parameters"""
    k = 1.0
    d = 0.5
    return k, d

def system_matrix(theta):
    """Returns a numpy array with the A(theta) matrix for a differential drive robot"""
    return A


def system_field(z, u):
    """Computes the field at a given state for the dynamical model"""
    return dot_z


def euler_step(z, u, stepSize):
    """Integrates the dynamical model for one time step using Euler's method"""
    return zp

def twist_to_speeds(speed_linear, speed_angular):
    right = speed_linear*0.5
    left = speed_linear*0.5

    right = right + speed_angular*0.5
    left = left - speed_angular*0.5

    return left, right

class KeyToVelocities(object):
    """Translate key presses to into velocities for the robot"""
    def __init__(self):
        self.speed_linear = 0.0
        self.speed_angular = 0.0
        self.SPEED_DELTA = 0.2
        text_description = String()
        key = String()
        
    def update_speeds(self, key):
        
        if key == 'W' or key == 'w':
            if self.speed_linear + self.SPEED_DELTA > 1.0:
                self.speed_linear = 1.0
            self.speed_linear = self.speed_linear + self.SPEED_DELTA
            text_description = "Increase linear speed"
        elif key == 'S' or key == 's':
            if self.speed_linear + self.SPEED_DELTA < -1.0:
                self.speed_linear = -1.0
            self.speed_linear = self.speed_linear - self.SPEED_DELTA
            text_description = "Decrease linear speed"
        elif key == 'A' or key == 'a':
            if self.speed_angular + self.SPEED_DELTA > 1.0:
                self.speed_angular = 1.0
            self.speed_angular = self.speed_angular + self.SPEED_DELTA
            text_description = "Increase angular speed"
        elif key == 'D' or key == 'd':
            if self.speed_angular + self.SPEED_DELTA < -1.0:
                self.speed_angular = -1.0
            self.speed_angular = self.speed_angular - self.SPEED_DELTA
            text_description = "Decrease angular speed"
        elif key == 'Z' or key == 'z':
            self.speed_linear = 0
        elif key == 'C' or key == 'c':
            self.speed_angular = 0
        elif key == 'X' or key == 'x':
            self.speed_angular = 0
            self.speed_linear = 0
        else:
            text_description = "Invalid command"

        return self.speed_angular, self.speed_linear, text_description
