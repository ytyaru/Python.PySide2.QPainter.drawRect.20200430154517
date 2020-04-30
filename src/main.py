from PySide2 import QtCore, QtGui, QtWidgets 
import sys 
class Painter(QtWidgets.QWidget):
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.begin(self)
         
        painter.setBrush(QtCore.Qt.lightGray)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRect(self.rect())
         
        painter.setBrush(QtGui.QColor(255, 0, 0, 85))
        painter.drawRect(10, 10, 80, 80)
         
        painter.setBrush(QtGui.QColor(0, 255, 0, 85))
        painter.drawRect(30, 30, 80, 80)
         
application = QtWidgets.QApplication(sys.argv)
window = Painter()
window.setWindowFlags(QtCore.Qt.Window)
window.resize(160,120)
window.show()
sys.exit(application.exec_())
