#!/bin/python3

import math
import os
import random
import re
import sys

class Car:
    def __init__(self, max_speed, units):
        self.units = units
        self.max_speed = max_speed

    def __str__(self):
        return("Car with the maximum speed of " + str(self.max_speed) + " " + str(self.units))
    pass

class Boat:
    def __init__(self, knots):
        self.knots = knots

    def __str__(self):
        return("Boat with the maximum speed of " + str(self.knots))
    pass


if __name__ == '__main__':
    car = Car(8, "ciao")
    print(car)

    boat = Boat(45)
    print(boat)