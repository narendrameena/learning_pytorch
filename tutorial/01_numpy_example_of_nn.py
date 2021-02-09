#!/usr/bin/env python3

'''

#author narumeena 
#description building and running a neural network using numpy

'''

# -*- coding: utf-8 -*- #


import numpy as np 
import math


#create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

#Randomly initialize weights 
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()


learning_rate = 1e-6

for t in range(2000):
    #Forward Pass: compute prediction y 
    #y = a + b x + c x ^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss 
    loss = np.square(y_pred - y).sum()
    if t % 100 ==99:
        print(t, loss)

    #Backprop to compute gradients of a, b, c, d with respect to loss 

    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x ).sum()
    grad_c = (grad_y_pred * x **2 ).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    #ßprint(grad_a)
    # update weights 
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d 

print(f'Result: y = {a} + {b} x + {c} x^2  +  {d} x^3')
