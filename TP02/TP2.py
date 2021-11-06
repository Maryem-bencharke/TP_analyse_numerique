# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

def polylagrange(X , x , i):
    res = 1
    n = len(X)

    for j in range(n):
        if j!=i:
            res = res * ((x-X[j])/(X[i]-X[j]))
        else:
            return False
    return res

def Interplagrange(X , f , x):
    res = 0
    n = len(X)
    for i in range(n):
        res +=(f(X[i]) * polylagrange(X , x , i))
    return res

def courbe(f , a , b , n):
    #X = np.linspace(a , b , n+1)
    X =[(a+b)/2 +((b-a)/2)*np.cos(((2*k+1)/n+1)*np.pi/2) for k in range(n+1)]
    y = f(X)
    pt_trace = np.linspace(a , b , (n+1)*20)
    y_courbe_f = f(pt_trace)
    y_courbe_P = []
    for x in pt_trace:
        y_courbe_P += [Interplagrange(X ,f ,x)]
    plt.plot(pt_trace , y_courbe_f , 'b')
    plt.plot(pt_trace , y_courbe_P , 'r')
    plt.plot(X , y , 'ro')
    plt.grid()
    plt.show()

def f(x):
    return np.sin(x)
a = 0
b = 2*np.pi
n = 3

courbe(f , a , b , n)


f1=lambda x:1/(1+np.power(x,2))
a = -5
b = 5
n = 30
courbe(f1 , a , b , n)
