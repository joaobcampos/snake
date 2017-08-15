#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In the example, we draw randomly 1000 red points 
on the window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QBasicTimer
import sys, random
from enum import Enum

class Direction(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

class Example(QWidget):
	
	BoardWidth = 0
	BoardHeight = 0
	x_max = 0
	y_max = 0
	snake = []
	direction = 1
	game_started = False
	speed = 0
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      
		#Initialize board
		self.BoardWidth = 2000
		self.BoardHeight = 2000
		self.setGeometry(0, 0, self.BoardWidth, self.BoardHeight)
		self.setWindowTitle('Snake')
		#Set background
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(p)
		
		#Set snake parameters
		self.direction = 4
		self.x_max = 125
		self.y_max = 125
		self.snake =[[(self.x_max // 2 - 1), self.y_max // 2], [(self.x_max // 2), self.y_max // 2], [(self.x_max // 2 + 1), self.y_max // 2]]
		self.speed = 1000
		#Has the game begun?
		game_started = False
		
		#Set timer
		self.timer = QBasicTimer()
		self.timer.start(self.speed, self)

		self.show()
		
	
	def paintEvent(self, e):
	
		qp = QPainter()
		qp.begin(self)
		self.drawSnake(qp)
		qp.end()
		
		
	def drawSnake(self, qp):
		qp.setBrush(Qt.red)
		qp.setPen(Qt.yellow)
		size = self.size()
		for i in self.snake:
			qp.drawRect((i[0] * self.BoardWidth // self.x_max), (i[1] * self.BoardHeight // self.y_max), self.BoardWidth // self.x_max, self.BoardHeight // self.y_max)
		self.update()
			
	def keyPressEvent(self, e):
		print("Entered keyPressEvent")
		self.game_started = True
		if e.key() == Qt.Key_Left:
			if(self.direction != 3 and self.direction != 4):
				self.direction = 3
		if e.key() == Qt.Key_Right:
			if(self.direction != 3 and self.direction != 4):
				self.direction = 4
		if e.key() == Qt.Key_Up:
			if(self.direction != 1 and self.direction != 2):
				self.direction = 1
		if e.key() == Qt.Key_Down:
			if(self.direction != 1 and self.direction != 2):
				self.direction = 2
		print(self.direction)

	def move(self):
		print("Entered move function")
		if self.game_started == False:
			return
		print("The position of the head")
		current_x = self.snake[-1][0]
		current_y = self.snake[-1][1]
		print(current_x)
		print(current_y)
		if self.direction == 1:
			#Go up
			current_y = current_y - 1
		if self.direction == 2:
			#Go down
			current_y = current_y + 1
		if self.direction == 3:
			#Go left
			current_x = current_x - 1
		if self.direction == 4:
			#Go Right
			current_x = current_x + 1
		
		#Check if new position collides with board limits
		if current_x < 0 or current_x >= self.x_max or current_y < 0 or current_y >= self.y_max:
			print("Game over")
			print(self.snake)
			sys.exit()
		#Check if new position collides with the snake:
		'''if [current_x, current_y] in self.snake:
			print("Game over invalid position")
			print([current_x, current_y])
			print(self.snake)
			sys.exit()'''
		self.snake.append([current_x, current_y]) 
		self.snake.pop(0)
		#self.update()
	
	def timerEvent(self, e):
		if e.timerId() == self.timer.timerId():
			print("s")
			print(self.snake)
			self.move()
		else:
			super(Example, self).timerEvent(e)

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
