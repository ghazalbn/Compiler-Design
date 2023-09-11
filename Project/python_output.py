
# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
 
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 500, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for components
    def UiComponents(self):
        DSB = QDoubleSpinBox()
        DSB.setGeometry(2,1,10,5)
        DSB.setPrefix('$')
        DSB.setRange(1,9)
        DSB = QDoubleSpinBox()
        DSB.setGeometry(100, 100, 150, 40)
        DSB.setMinimum(0)

App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
