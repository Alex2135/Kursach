import numpy as np
from PlaneGraph import  PlaneGraph
from Graph3DGenerator import Graph3DGenerator

class PlanePuankareGenerator:
    def __init__(self, graph, plane):
        self.graph : Graph3DGenerator = graph
        self.plane : PlaneGraph = plane
        self.graph_plane =  []

    def makeGraph(self, dot_eps = 0.1):
        result = []

        # [ {"x":0, "y":0, "z":0} ]
        graph_coords = self.graph.COORDS

        for point in graph_coords:
            if self.plane.isPointOnPlane(point, dot_eps):
                result.append(point)

        return result
"""
self.graph = [
    [x1, x2, x3],
    [y1, y2, y3],
    [z1, z2, z3] 
]
"""