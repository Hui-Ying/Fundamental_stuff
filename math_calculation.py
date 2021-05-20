#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import libraries
import scipy.integrate as integrate
import numpy as np
from numpy import sqrt, sin, cos, pi
from scipy.integrate import odeint
from matplotlib import pyplot as plt

# Q1. Integral
# Integrate exp[1+sin(x)cos(x)] dx  , [0,3*pi]
result = integrate.quad(lambda x: np.exp(1+sin(x) + cos(x)), 0,3*pi)

# Q2. Solve second order DE
# Differential eq:
# u”(t)+2tu’(t)+u(t)=2sin(t), u’(0)=1, u(0)=0

# hints:
# a’+2ta+u=2sin(t)
# u’=a

def f(u,t):
    return (u[1], -2*u[1]*t-u[0]+2*np.sin(t)) # u[1] = u'(t); u''(t) = -2*u[1]*t-u[0]+2*np.sin(t)

y0 = [0,1]
ts = np.linspace(1,50,500)
us = odeint(f, y0, ts)
ys = us[:,0]
plt.plot(ts, ys, "-")
plt.plot(ts, ys, "r*")
plt.xlabel("x")
plt.ylabel("y")
plt.title("(D**s + 2*tD + 1)u = 2*sin(t)")
plt.show()

    