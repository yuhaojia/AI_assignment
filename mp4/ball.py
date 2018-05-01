import random 

class ball(object):
	def __init__(self):
		self.x = 0.5
		self.y = 0.5
		self.v_x = 0.03
		self.v_y = 0.01

	def bounceFromPaddle(self):
		self.x = 2 - self.x
		U = random.uniform(-0.015, 0.015)
		V = random.uniform(-0.03, 0.03)
		self.v_x = -self.v_x + U
		self.v_y = self.v_y + V
		if abs(self.v_x) < 0.03:
			self.v_x = -0.03
		if abs(self.v_x) > 1:
			self.v_x = -1

	def checkBounceFromWall(self):
		if self.y < 0:
			self.y = -self.y
			self.v_y = -self.v_y
		elif self.y > 1:
			self.y = 2 - self.y
			self.v_y = -self.v_y
		elif self.x < 0:
			self.x = - self.x
			self.v_x = -self.v_x

	def checkBounceFromWall_human(self):
		if self.y < 0:
			self.y = -self.y
			self.v_y = -self.v_y
		elif self.y > 1:
			self.y = 2 - self.y
			self.v_y = -self.v_y

	def bounceFromPaddle_human(self):
		self.x = abs(self.x)
		U = random.uniform(-0.015, 0.015)
		V = random.uniform(-0.03, 0.03)
		self.v_x = -self.v_x + U
		self.v_y = self.v_y + V
		if abs(self.v_x) < 0.03:
			self.v_x = 0.03
		if abs(self.v_x) > 1:
			self.v_x = 1

	def update(self):
		self.x = self.x + self.v_x
		self.y = self.y + self.v_y
		self.checkBounceFromWall()

	def initBall(self):
		self.x = 0.5
		self.y = 0.5
		self.v_x = 0.03
		self.v_y = 0.01

	def update_human(self):
		self.x = self.x + self.v_x
		self.y = self.y + self.v_y
		self.checkBounceFromWall_human()
