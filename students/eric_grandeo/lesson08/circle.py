#!/usr/bin/env python3

'''
A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.
'''

class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self._diameter = None
        
        
    @property 
    def diameter(self):
        self._diameter = self.radius*2
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value/2           

        


