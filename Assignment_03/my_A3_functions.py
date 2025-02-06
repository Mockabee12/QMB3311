# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Matthew Mockabee & Grant Heisey
#
# Date: 2/3/2025
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import 


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def CESutility_valid(good_x: float, good_y: float, parameter: float) -> float:
    """ Returns the same value as CESutility() when x and y are non-negative
    numbers and r is strictly positive but
    returns the value None otherwise"""
    
    if good_x < 0:
        print("Error: good_x cannot be negative.")
        return None
    if good_y < 0:
        print("Error: good_y cannot be negative.")
        return None
    if parameter <= 0:
        print("Error: paramter must be strictly positive")
        return None
    return ((good_x ** parameter) + (good_y ** parameter)) ** (1 / parameter)

# ...

# Define the rest of your functions for Exercises 2-4.
 



# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.

print(CESutility_valid(4, 5, 1))
print(CESutility_valid(-4, 5, 1))
print(CESutility_valid(8, -10, 2))
print(CESutility_valid(8, 10, -2))

##################################################
# End
##################################################