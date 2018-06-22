# _*_ coding: utf-8 _*_
#! /usr/bin/python 

# Import Libraries
import numpy as np
import math
import matplotlib.pyplot as plt

# Initial Settings
t_start = 0
t_end = 30
dt = 0.001
t_log = np.arange(t_start,t_end,dt)
theta = []
d = []
x = [10]
u = []
xd = []
dot_xd = []
# RLS
hat_theta = []
# ESO
error_ESO = []
pole_ESO = 5
hat_x1 = [8]
hat_x2 = [0]
hat_d = []
kp = 1

# Start Simulation
for t in t_log:
    xd.append( 2*math.sin(t) )
    dot_xd.append( 2*math.cos(t) )
    hat_theta.append( 2 )
    # ESO
    if t==0:
        hat_x1.append(hat_x1[-1])
        hat_x2.append(hat_x2[-1])
        error_ESO.append(hat_x1[-1] - x[-1])
    else:
        error_ESO.append( hat_x1[-1] - x[-1] )
        hat_x1.append( hat_x1[-1] + dt*( hat_x2[-1] + u[-1] - 2*pole_ESO*error_ESO[-1] ) )
        hat_x2.append( hat_x2[-1] + dt*( 0 - pole_ESO*pole_ESO*error_ESO[-1] ))
    # Controller
    hat_d.append( hat_x2[-1] )
    u.append( dot_xd[-1] - hat_d[-1] - kp*( x[-1] - xd[-1] ) )
    # True System
    theta.append( 2+0.2*math.sin(t) )
    d.append( theta[-1]*x[-1] )
    x.append( x[-1] + dt*( d[-1] + u[-1] ) )

# Plot
# tracking results
plt.figure(1)
plt.subplot(211)
plt.plot(t_log, xd[:], 'r-', label='xd')
plt.plot(t_log, x[:-1],'b-.',label='x')
plt.xlim(t_start, t_end)
plt.title('Tracking Results')
plt.legend(loc='upper right')
plt.grid(True)
plt.subplot(212)
plt.plot(t_log,u[:],'k-.',label='u')
plt.xlim(t_start, t_end)
plt.legend(loc='lower right')
plt.grid(True)
plt.xlabel('Time [s]')
plt.show()
# ESO
plt.figure(2)
plt.subplot(211)
plt.plot(t_log, x[:-1], 'r-', label='d')
plt.plot(t_log, hat_x1[:-1], 'b-.', label='hat_x')
plt.xlim(t_start, t_end)
plt.title('ESO')
plt.legend(loc='upper right')
plt.grid(True)
plt.subplot(212)
plt.plot(t_log, d[:],'r-',label='d')
plt.plot(t_log, hat_d[:],'b-.',label='hat_d')
plt.xlim(t_start,t_end)
plt.legend(loc='upper right')
plt.grid(True)
plt.xlabel('Time [s]')
plt.show()

