import numpy as np
from math import *
import copy

class RK_calculus:
    def __init__(self, _zero_vals, _funcs, _hop):
        self.vals = _zero_vals
        self.functions = _funcs
        self.hop = _hop

    def getNextValues(self):
        if not self.vals:
            raise ValueError("No zero values")

        list_axis = ['x', 'y', 'z']
        result = {}

        for i in range(3):
            axis = list_axis[i]
            function = self.functions[i]
            result[axis] = self.RungeKutta(function, self.vals[axis])

        self.vals = copy.copy(result)
        return result

    def RungeKutta(self, _func, _val):
        koef1 = self.k1(_func)
        koef2 = self.k2(_func)
        koef3 = self.k3(_func)
        koef4 = self.k4(_func)

        result = _val + self.hop / 6 * ( koef1 + 2 * (koef2 + koef3) + koef4)
        return result

    def k1(self, _func):
        vals_copy = copy.copy(self.vals)
        result = self.hop * eval(_func, vals_copy)
        return result

    def k2(self, _func):
        vals_copy = copy.copy(self.vals)
        for key, value in vals_copy.items():
            vals_copy[key] = value + self.hop / 2 * self.k1(_func)

        result = self.hop * eval(_func, vals_copy)
        return result

    def k3(self, _func):
        vals_copy = copy.copy(self.vals)
        for key, value in vals_copy.items():
            vals_copy[key] = value + self.hop / 2 * self.k2(_func)

        result = self.hop * eval(_func, vals_copy)
        return result

    def k4(self, _func):
        vals_copy = copy.copy(self.vals)
        for key, value in vals_copy.items():
            vals_copy[key] = value + self.hop * self.k3(_func)

        result = self.hop * eval(_func, vals_copy)
        return result