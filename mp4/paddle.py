import random 
from ball import *

class paddle(object):
	def __init__(self, agent):
		self.height = 0.2
		self.x = 1
		self.y = 0.5 - self.height / 2
		self.v = 0.04
		self.agent = agent

	def checkBoundary(self):
		if self.y < 0:
			self.y = 0
		if self.y > 1 - self.height:
			self.y = 1 - self.height

	def Qupdate(self, action):
		self.y = self.y + action * self.v
		self.checkBoundary()

	def update(self, action):
		self.Qupdate(action)

	def initPaddle(self):
		self.height = 0.2
		self.x = 1
		self.y = 0.5 - self.height / 2
		self.v = 0.04



