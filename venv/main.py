import numpy as np
import matplotlib.pyplot as plt
from Graph3DGenerator import Graph3DGenerator
from mpl_toolkits.mplot3d import Axes3D
from MainWindow import *

# python -m PyQt5.uic.pyuic -x main_form.ui -o main_form.py

app = QtWidgets.QApplication(sys.argv)
myapp = MyWin()
myapp.show()
sys.exit(app.exec_())

# k1 = input("Input x0: ")
# x0 = 0 if not k1 else float(k1) # 0
# k2 = input("Input y0: ")
# y0 = 1 if not k2 else float(k2) #1
# k3 = input("Input z0: ")
# z0 = 1 if not k3 else float(k3) #1
#
# k1 = input("Input f1(x, y, z) :") # "10*(y-x)"
# func1 = "10*(y-x)" if not k1 else k1
# k2 =  input("Input f2(x, y, z) :")
# func2 = "x*(28-z)-y" if not k2 else k2 # "x*(28-z)-y"
# k3 = input("Input f3(x, y, z) :")
# func3 = "x*y-8/3*z" if not k3 else k3 # "x*y-8/3*z"
#
# k1 = input("Input N: ")
# N = 100 if not k1 else float(k1) # 0.1
#
# k1 = input("Input tn: ")
# tn = 10 if not k1 else float(k1) # 10
#
# funcs = [func1, func2, func3]
# vals = {'x' : x0, 'y': y0, 'z': z0}
#
# graph = Graph3DGenerator(funcs, vals)
# X, Y, Z = graph.makeGraph(tn, N)
#
# fig = plt.figure()
# axes = Axes3D(fig)
# axes.plot(X, Y, Z)
#
# plt.grid(True)
# plt.title("Главный график")
#
# fig, ax = plt.subplots(3)
# ax[0].plot(X, Y)
# ax[1].plot(Z, Y)
# ax[2].plot(X, Z)
# plt.show()