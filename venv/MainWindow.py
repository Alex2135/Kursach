import sys
import FixQT

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main_form import *
from Graph3DGenerator import Graph3DGenerator

import numpy as np
import matplotlib.pyplot as plt
from Graph3DGenerator import Graph3DGenerator
from mpl_toolkits.mplot3d import Axes3D
from PlaneGraph import PlaneGraph
from PlanePuankareGenerator import PlanePuankareGenerator

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_plot_graph.clicked.connect(self.plotGraphClicked)
        self.ui.button_plot_projections.clicked.connect(self.plotProjections)
        self.ui.button_plot_graph_with_plane.clicked.connect(self.plotGraphWithPlane)
        self.ui.button_plot_Puankare_plane.clicked.connect(self.plotPuankarePlane)
        self.graph : Graph3DGenerator
        self.graph_plane : PlaneGraph
        self.graph_Puankare : PlanePuankareGenerator

    def makeGraph(self):
        func_x = self.ui.func_dx.text()
        func_y = self.ui.func_dy.text()
        func_z = self.ui.func_dz.text()
        funcs = [func_x, func_y, func_z]

        x0 = float(self.ui.x_0.text())
        y0 = float(self.ui.y_0.text())
        z0 = float(self.ui.z_0.text())
        vals = {'x': x0, 'y': y0, 'z': z0}

        tn = int(self.ui.tn.text())
        N = int(self.ui.NBig.text())
        self.graph = Graph3DGenerator(funcs, vals)
        return self.graph.makeGraph(tn, N)

    def plotPuankarePlane(self):
        X, Y, Z = self.makeGraph()
        self.graph_plane = PlaneGraph()
        self.graph_plane["a"] = float(self.ui.plane_a.text())
        self.graph_plane["b"] = float(self.ui.plane_b.text())
        self.graph_plane["c"] = float(self.ui.plane_c.text())
        self.graph_plane["d"] = float(self.ui.plane_d.text())

        plane_X, plane_Y, plane_Z = self.graph_plane.makeGraph(X, Y)

        # X, Y, Z - graph
        # plane_X, plane_Y, plane_Z - plane
        generator = PlanePuankareGenerator(self.graph, self.graph_plane)
        self.graph_Puankare = generator.makeGraph(2)
        X = list(map(lambda i: i["x"], self.graph_Puankare))
        Y = list(map(lambda i: i["y"], self.graph_Puankare))
        Z = list(map(lambda i: i["z"], self.graph_Puankare))

        fig, ax = plt.subplots()

        ax.scatter(X, Y)
        plt.show()

    def plotGraphWithPlane(self):
        X, Y, Z = self.makeGraph()

        fig = plt.figure()
        axes = Axes3D(fig)
        axes.scatter(X[0], Y[0], Z[0], color="green")
        i = len(X) - 1
        axes.scatter(X[i], Y[i], Z[i], color="red")

        axes.plot(X, Y, Z, alpha=1)

        self.graph_plane = PlaneGraph()
        self.graph_plane["a"] = float( self.ui.plane_a.text() )
        self.graph_plane["b"] = float( self.ui.plane_b.text() )
        self.graph_plane["c"] = float( self.ui.plane_c.text() )
        self.graph_plane["d"] = float( self.ui.plane_d.text() )

        plt3 = fig.gca()
        plane_X, plane_Y, plane_Z = self.graph_plane.makeGraph(X, Y)
        plt3.plot_surface( plane_X, plane_Y, plane_Z, color="purple" )

        # X, Y, Z - graph
        # plane_X, plane_Y, plane_Z - plane
        generator = PlanePuankareGenerator(self.graph, self.graph_plane)
        self.graph_Puankare = generator.makeGraph()

        plt.grid(True)
        plt.title("Главный график")
        plt.show()


    def plotGraphClicked(self):
        X, Y, Z = self.makeGraph()

        fig = plt.figure()
        axes = Axes3D(fig)
        i = len(X) - 1
        axes.scatter(X[0], Y[0], Z[0], color="green")
        axes.scatter(X[i], Y[i], Z[i], color="red")
        axes.plot(X, Y, Z)

        plt.grid(True)
        plt.title("Главный график")
        plt.show()

    def plotProjections(self):
        if not self.graph:
            self.makeGraph()

        fig, ax = plt.subplots(3)
        ax[0].plot( *(self.graph.getProjections("x", "Y")), label="x 0 y")
        ax[1].plot( *(self.graph.getProjections("z", "Y")), label="z 0 y")
        ax[2].plot( *(self.graph.getProjections("x", "z")), label="x 0 z")

        for axis in ax:
            axis.legend(loc='upper left', shadow=True)

        plt.show()

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()
