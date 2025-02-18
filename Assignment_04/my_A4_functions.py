# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Matthew Mockabee
#
# Date: 2/17/2025
# 
##################################################
#
# Sample Script for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy as np

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def matrix_inverse(mat_in):
    """
    Replicate the numpy method linalg.inv() that calculates the inverse of 
    a two-by-two matrix mat in.
    The inverse of the matrix A denoted A−1, is a matrix the same size as A 
    such that A * A−1 = I, where I is the identity matrix with ones on the
    diagonal and zeros elsewhere. It can be used to solve the systems of 
    equations A * x = b by multiplying A−1 with b toget x = A−1 * b

    
    Parameters:
        mat_in (numpy.ndarray): Input 2x2 matrix
        
    Returns:
        numpy.ndarray: Inverse matrix if it exists
        None: if matrix is not invertible
    """
    if mat_in.shape != (2, 2):
        print("Warning: Input must be a 2x2 matrix")
        return None
        
    a11, a12 = mat_in[0, 0], mat_in[0, 1]
    a21, a22 = mat_in[1, 0], mat_in[1, 1]
    
    det = a11*a22 - a12*a21
    
    if det == 0:
        print("Error: Determinant cannot be zero")
        return None
    else: mat_out = np.zeros((2, 2))
    mat_out[0, 0] = a22/det
    mat_out[0, 1] = -a12/det
    mat_out[1, 0] = -a21/det
    mat_out[1, 1] = a11/det
    
    return mat_out

# Exercise 2


# Exercise 3


def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, an example without the >>> does not get run with doctest.
    
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]
    """
    
    return None


# Exercise 4



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################
