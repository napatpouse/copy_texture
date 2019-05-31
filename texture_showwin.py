from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
import sys 
import os
import texture_tranfer
reload(texture_tranfer)
from shiboken import wrapInstance
import maya.OpenMayaUI as mui

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    if ptr is not  None:
        return wrapInstance(long(ptr), QMainWindow)

class MyMainWindow(QMainWindow):
	def __init__(self, parent = None):
		super(MyMainWindow, self).__init__(parent)
		loader = QUiLoader()
		file = QFile( os.path.dirname(__file__) + "/texture.ui")
		file.open(QFile.ReadOnly)
		self.ui = loader.load(file)
		file.close
		self.texture_tranfer = texture_tranfer.Active()
		self.setCentralWidget(self.ui)
		self.do_connection()

	def do_connection(self):
		self.ui.pushButton.clicked.connect(self.press_one)
		self.ui.pushButton_2.clicked.connect(self.press_two)
		self.ui.pushButton_3.clicked.connect(self.press_three)

	def press_one(self):
		self.texture_tranfer.set_file()
	def press_two(self):
		self.texture_tranfer.copyfile_to_newpath()
	def press_three(self):
		self.texture_tranfer.connected()
		

w = MyMainWindow(getMayaWindow())
w.show()
