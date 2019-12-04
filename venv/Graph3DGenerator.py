from RungeKutta import RK_calculus

class Graph3DGenerator:
    def __init__(self, funcs, start={'x' : 0, 'y': 0, 'z': 0}):
        self.funcs = funcs
        self.start = start
        self.COORDS = []

    def makeGraph(self, tn, N):
        hop = tn / N

        rk = RK_calculus(self.start, self.funcs, hop)
        self.COORDS = [rk.getNextValues() for i in range(N)]
        X = list(map(lambda i: i["x"], self.COORDS))
        Y = list(map(lambda i: i["y"], self.COORDS))
        Z = list(map(lambda i: i["z"], self.COORDS))

        return X, Y, Z

    def getProjections(self, axisNameOne, axisNameTwo):
        axisNameOne = axisNameOne.lower()
        axisNameTwo = axisNameTwo.lower()
        axisOne = list(map(lambda i: i[axisNameOne], self.COORDS))
        axisTwo = list(map(lambda i: i[axisNameTwo], self.COORDS))

        return axisOne, axisTwo