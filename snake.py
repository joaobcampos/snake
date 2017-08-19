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
from PyQt5.QtCore import Qt, QBasicTimer, QTimer
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
	
	#Apple settings
	apple_pos = 0
	apple_color = 0
	apple_number = 0
	apple_active = False
	apple_eaten = False
	
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
		self.snake =[[(self.x_max // 2 - 1), self.y_max // 2], [(self.x_max // 2), self.y_max // 2], [(self.x_max // 2 + 1), self.y_max // 2], [(self.x_max // 2 + 2), self.y_max // 2] , [(self.x_max // 2 + 3), self.y_max // 2]]
		self.speed = 50
		#Has the game begun?
		game_started = False
		
		#Set timer
		self.timer = QBasicTimer()
		self.timer.start(self.speed, self)
		
		#Apple settings
		self.apple_pos = [0, 0]
		self.apple_color = Qt.white
		self.apple_number = 0
		self.apple_active = False
		self.apple_eaten = False
		
		random.seed()
		self.apple_activate()
		self.show()

	def paintEvent(self, e):
	
		qp = QPainter()
		qp.begin(self)
		self.drawSnake(qp)
		self.drawApple(qp)
		qp.end()
		
		
	def drawSnake(self, qp):
		qp.setBrush(Qt.red)
		qp.setPen(Qt.yellow)
		size = self.size()
		for i in self.snake:
			qp.drawRect((i[0] * self.BoardWidth // self.x_max), (i[1] * self.BoardHeight // self.y_max), self.BoardWidth // self.x_max, self.BoardHeight // self.y_max)
		self.update()

	def drawApple(self, qp):
		if self.apple_active == True and self.apple_eaten == False:
			qp.setBrush(Qt.blue)
			qp.setPen(Qt.green)
		else:
			qp.setBrush(Qt.transparent)
			qp.setPen(Qt.transparent)
		radx = 10
		rady = 20
		qp.drawEllipse((self.apple_pos[0] * self.BoardWidth // self.x_max), (self.apple_pos[1] * self.BoardHeight // self.y_max), radx, rady)
		self.update()

	def keyPressEvent(self, e):
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
		self.move()

	def apple_activate(self):
		try:
			if self.game_started == False:
				self.apple_active = False
			else:
				self.apple_active = not self.apple_active
				print("Cycle with apple active: " + str(self.apple_active))
				#If there is a new apple, then it could not be eaten.
				if self.apple_active == False:
					self.apple_eaten = False
				#The apple's position is defined for the interval defined
				margin = 20
				self.apple_pos[0] = random.randint(margin, self.x_max - margin)
				self.apple_pos[1] = random.randint(margin, self.y_max - margin)
		finally:
			
			duration = random.randint(5, 20) * 1000
			#duration = 10000
			QTimer.singleShot(duration, self.apple_activate)

	def apple_eat(self):
		#set margin for eating
		margin_x = self.snake[-1][0] - self.apple_pos[0]
		margin_y = self.snake[-1][1] - self.apple_pos[1]
		eat_margin = 1
		print("apple active: " + str(self.apple_active) )
		print("apple eaten: " + str(self.apple_eaten) )
		if(abs(margin_x) < eat_margin and abs(margin_y) < eat_margin and self.apple_active == True and self.apple_eaten == False):
			print("\n\n\n\n\n\n\n\n")
			print("Apple was eaten")
			self.apple_number = self.apple_number + 1
			add_square = self.snake[0]
			self.snake.insert(0, add_square)
			self.apple_eaten = True
			print(self.apple_number)
	
	def move(self):
		if self.game_started == False:
			return
		current_x = self.snake[-1][0]
		current_y = self.snake[-1][1]
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
			sys.exit()
		#Check if new position collides with the snake:
		if [current_x, current_y] in self.snake and [current_x, current_y] != self.snake[-2]:
			print("Game over")
			sys.exit()
		self.snake.append([current_x, current_y]) 
		self.snake.pop(0)

	
	def timerEvent(self, e):
		if e.timerId() == self.timer.timerId():
			self.move()
			self.apple_eat()
		else:
			super(Example, self).timerEvent(e)

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
