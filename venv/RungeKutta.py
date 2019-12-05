import numpy as np
from math import *
import copy

class RK_calculus:
    def __init__(self, _zero_vals, _funcs, _hop):
        self.vals = _zero_vals
        self.functions = _funcs
        #if len(self.functions) == 3:

        self.hop = _hop

    def getNextValues(self):
        if not self.vals:
            raise ValueError("No zero values")

        list_axis = ['x', 'y', 'z']
        result = {}

        k1 = {"x":0, "y":0, "z":0}
        k1["x"] = eval( self.functions[0], self.vals )
        k1["y"] = eval( self.functions[1], self.vals )
        k1["z"] = eval( self.functions[2], self.vals )

        k2 = {"x":0, "y":0, "z":0}
        args = {}
        args["x"] = self.vals["x"] + k1["x"]*self.hop/2
        args["y"] = self.vals["y"] + k1["y"]*self.hop/2
        args["z"] = self.vals["z"] + k1["z"]*self.hop/2
        k2["x"] = eval( self.functions[0], args )
        k2["y"] = eval( self.functions[1], args )
        k2["z"] = eval( self.functions[2], args )

        k3 = {"x":0, "y":0, "z":0}
        args["x"] = self.vals["x"] + k2["x"]*self.hop/2
        args["y"] = self.vals["y"] + k2["y"]*self.hop/2
        args["z"] = self.vals["z"] + k2["z"]*self.hop/2
        k3["x"] = eval( self.functions[0], args )
        k3["y"] = eval( self.functions[1], args )
        k3["z"] = eval( self.functions[2], args )

        k4 = {"x":0, "y":0, "z":0}
        args["x"] = self.vals["x"] + k3["x"]*self.hop
        args["y"] = self.vals["y"] + k3["y"]*self.hop
        args["z"] = self.vals["z"] + k3["z"]*self.hop
        k4["x"] = eval( self.functions[0], args )
        k4["y"] = eval( self.functions[1], args )
        k4["z"] = eval( self.functions[2], args )

        result["x"] = self.vals["x"] + self.hop/6 * (k1["x"] + (k2["x"] + k3["x"])*2 + k4["x"])
        result["y"] = self.vals["y"] + self.hop/6 * (k1["y"] + (k2["y"] + k3["y"])*2 + k4["y"])
        result["z"] = self.vals["z"] + self.hop/6 * (k1["z"] + (k2["z"] + k3["z"])*2 + k4["z"])

        self.vals = copy.copy(result)
        return result

