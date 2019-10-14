import numpy as np
import matplotlib.pyplot as plt
from RungeKutta import RK_calculus
from mpl_toolkits.mplot3d import Axes3D

k1 = input("Input x0: ")
x0 = 0 if not k1 else float(k1) # 0
k2 = input("Input y0: ")
y0 = 1 if not k2 else float(k2) #1
k3 = input("Input z0: ")
z0 = 1 if not k3 else float(k3) #1

k1 = input("Input f1(x, y, z) :") # "10*(y-x)"
func1 = "10*(y-x)" if not k1 else k1
k2 =  input("Input f2(x, y, z) :")
func2 = "x*(28-z)-y" if not k2 else k2 # "x*(28-z)-y"
k3 = input("Input f3(x, y, z) :")
func3 = "x*y-8/3*z" if not k3 else k3 # "x*y-8/3*z"

k1 = input("Input h (hop): ")
hop = 0.1 if not k1 else float(k1) # 0.1

k1 = input("Input tn: ")
tn = 10 if not k1 else float(k1) # 10
N = int(tn / hop)

funcs = [func1, func2, func3]
vals = {'x' : x0, 'y': y0, 'z': z0}

rk = RK_calculus(vals, funcs, hop)
COORDS = [ rk.getNextValues() for i in range(N) ]

X = list( map(lambda i: i["x"] , COORDS) )
Y = list( map(lambda i: i["y"] , COORDS) )
Z = list( map(lambda i: i["z"] , COORDS) )
#print(COORDS)

fig = plt.figure()

axes = Axes3D(fig)
axes.plot(X, Y, Z)

plt.show()