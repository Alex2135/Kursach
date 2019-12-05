import numpy as np
import math

class PlaneGraph:
    def __init__(self, a=1, b=1, c=1, d=1):
        self.koef = { "a":1, "b":1, "c":1, "d":1 }
        self.X = []
        self.Y = []
        self.Z = []

    def __setitem__(self, instance, value):
        self.koef[instance] = value

    def getCoords(self):
        return self.X, self.Y, self.Z

    def isPointOnPlane(self, point, eps=0.0001):
        # ax+by+cz+d=0
        result = point["z"] - (-(self.koef["a"]) * point["x"] - self.koef["b"] * point["y"] - self.koef["d"]) * 1. / self.koef["c"]
        return 0 <= result <= eps

    def makeGraph(self, X, Y):
        max_X = math.ceil(max(X))
        min_X = math.ceil(min(X))
        max_Y = math.ceil(max(Y))
        min_Y = math.ceil(min(Y))

        plane_X, plane_Y = np.meshgrid(range(min_X, max_X), range(min_Y, max_Y))
        plane_Z = (-(self.koef["a"]) * plane_X - self.koef["b"] * plane_Y - self.koef["d"]) * 1. / self.koef["c"]
        self.X = plane_X
        self.Y = plane_Y
        self.Z = plane_Z

        return plane_X, plane_Y, plane_Z