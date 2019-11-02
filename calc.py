import os
import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon

class CalcWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.__result = 0
		self.__temp = ''
		self.__operator = ''
		self.initUI()


	def initUI(self):
		#self.resize(300, 200)
		self.move(0,0)
		self.setWindowTitle('Calc')
		self.setFixedSize(225, 200)

		#button
		item = ['AC', '+/-', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '00', '.', '=']
		button = [QPushButton(i) for i in item]	
		grid = QGridLayout()
		cnt = 0
		for i in range(int(len(item)/4)):
			for j in range(4):
				#button[cnt].setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
				if j == 3:
					button[cnt].setStyleSheet("background-color:orange")	
				grid.addWidget(button[cnt], i, j)
				cnt += 1
		for i in range(3, len(button)-1):
			if i%4 == 3:
				button[i].clicked.connect(self.on_click_operator)	
			else:
				button[i].clicked.connect(self.on_click_num)	
		button[0].clicked.connect(self.on_click_ac)
		button[len(button)-1].clicked.connect(self.on_click_equal)

		#label
		self.label = QLabel(str(self.__result))
		self.label.resize(15, 100)
		self.label.setStyleSheet("background-color:gray")
		self.label.setFont(QFont('Arial', 12))
		#self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

		#layout
		vbox = QVBoxLayout()
		vbox.addWidget(self.label)
		vbox.addLayout(grid)
		self.setLayout(vbox)

		self.show()


	def on_click_num(self):
		self.__temp += self.sender().text()
		self.label.setText(self.__temp)

	
	def on_click_operator(self):
		if self.__temp == '':	
			self.label.setText('input number...')
			self.__result = 0
			self.__temp = ''
			self.__operator = ''
		elif self.__operator == '' or self.__operator == '+':	
			self.__result += float(self.__temp)
			self.__temp = ''
			self.__operator = self.sender().text()
			self.label.setText(str(self.__result))	
		elif self.__operator == '-':	
			self.__result -= float(self.__temp)
			self.__temp = ''
			self.__operator = self.sender().text()
			self.label.setText(str(self.__result))	
		elif self.__operator == '*':	
			self.__result *= float(self.__temp)
			self.__temp = ''
			self.__operator = self.sender().text()
			self.label.setText(str(self.__result))	
		elif self.__operator == '/':	
			self.__result /= float(self.__temp)
			self.__temp = ''
			self.__operator = self.sender().text()
			self.label.setText(str(self.__result))	
		else:
			self.label.setText('Error...')
			self.__result = 0
			self.__temp = ''
			self.__operator = ''


	def on_click_equal(self):
		if self.__temp == '':	
			self.label.setText('input number...')
		elif self.__operator == '' or self.__operator == '+':	
			self.__result += float(self.__temp)
			self.label.setText(str(self.__result))	
		elif self.__operator == '-':	
			self.__result -= float(self.__temp)
			self.label.setText(str(self.__result))	
		elif self.__operator == '*':	
			self.__result *= float(self.__temp)
			self.label.setText(str(self.__result))	
		elif self.__operator == '/':	
			self.__result /= float(self.__temp)
			self.label.setText(str(self.__result))	
		else:
			self.label.setText('Error...')
		self.__result = 0
		self.__temp = ''
		self.__operator = ''


	def on_click_ac(self):
		self.__result = 0
		self.__temp = ''
		self.__operator = ''
		self.label.setText(str(self.__result))	


def icon_path(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)
		
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon(icon_path('calc.ico')))
	window = CalcWindow()
	sys.exit(app.exec_())
