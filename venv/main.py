import numpy as np
import matplotlib.pyplot as plt
from Graph3DGenerator import Graph3DGenerator
from mpl_toolkits.mplot3d import Axes3D
from MainWindow import *

# python -m PyQt5.uic.pyuic -x main_form.ui -o main_form.py
# pyinstaller --name="Kursach" --windowed --onefile venv/main.py

app = QtWidgets.QApplication(sys.argv)
myapp = MyWin()
myapp.show()
sys.exit(app.exec_())