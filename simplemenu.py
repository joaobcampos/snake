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
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton)
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QIcon


class Example(QMainWindow):
	
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
        
        
	def initUI(self):               
		
		'''exitAct = QAction(QIcon('exit.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit application')
		exitAct.triggered.connect(qApp.quit)
		self.statusBar()
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)'''
		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50, 50)
		
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Simple menu')    
		self.show()

if __name__ == '__main__':
    
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())