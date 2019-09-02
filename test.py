%matplotlib inline
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 02:32:11 2018
@author: Azumi Mamiya
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    alpha = [10**(-5),
            10**(-5.4),
            10**(-5.5),
            10**(-5.6),
            10**(-5.7),
            10**(-6),]
    beta=10**(-1)
    hassei_t=[0,6,18,22,32,40,47]
    x,y=[],[]
    
    for t in range(60):
        lam=10**(-6)
        for ti in hassei_t:
            if  ti<t:
                lam += alpha[ti//10]*np.exp(-beta*(t-ti))
        x.append(t)
        y.append(lam)
    plot(x,y)

def plot(x,y):
    plt.plot(x,y,'-',markersize=1)
    plt.ylim(10**(-6),10**(-5))
if __name__ == "__main__":
    main()