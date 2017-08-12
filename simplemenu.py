#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
os.chdir('C:\\Users\jcampos\Desktop\pyqt5')
"""
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: January 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
	
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
        
        
	def initUI(self):               
		
		btn_snake = QPushButton('snake', self)
		btn_snake.setToolTip('click here if you want to play snake')
		btn_snake.resize(btn_snake.sizeHint())
		btn_snake.move(500, 250)
		
		btn_paddle = QPushButton('paddle', self)
		btn_paddle.setToolTip('click here if you want to play the paddle game')
		btn_paddle.resize(btn_paddle.sizeHint())
		btn_paddle.move(500, 500)
		
		qbtn = QPushButton('Quit', self)
		#qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.clicked.connect(self.close)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(500, 750)
		
		self.setGeometry(0, 0, 1000, 1000)
		self.setWindowTitle('Simple menu')    
		self.show()

if __name__ == '__main__':
    
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())