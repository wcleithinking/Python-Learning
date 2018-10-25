# -*- coding: utf-8 -*-
#! /usr/bin/python

# Import Libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# Time Settings
t_start = 0
t_end = 60
dt = 0.001
t_log = np.arrange( t_start, t_end, dt )

# Initial Settings
x = []  # x
y = []  # y
theta = []  # theta

# Start Simulation
for t in t_log:
    x.append