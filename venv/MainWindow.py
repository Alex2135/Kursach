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

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_plot_graph.clicked.connect(self.plot_graph_clicked)
        self.ui.button_plot_projections.clicked.connect(self.plot_projections)
        self.graph = None

    def make_graph(self):
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

    def plot_graph_clicked(self):
        X, Y, Z = self.make_graph()

        fig = plt.figure()
        axes = Axes3D(fig)
        axes.plot(X, Y, Z)

        plt.grid(True)
        plt.title("Главный график")
        plt.show()

    def plot_projections(self):
        if not self.graph:
            self.make_graph()

        fig, ax = plt.subplots(3)
        ax[0].plot( *(self.graph.getProjections("x", "Y")), label="x 0 y")
        #ax[0].title("xOy")
        ax[1].plot( *(self.graph.getProjections("z", "Y")), label="z 0 y")
        #ax[1].title("zOy")
        ax[2].plot( *(self.graph.getProjections("x", "z")), label="x 0 z")
        #ax[2].title("xOz")
        for axis in ax:
            axis.legend(loc='upper left', shadow=True)

        plt.show()

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()
