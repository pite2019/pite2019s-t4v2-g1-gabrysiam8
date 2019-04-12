import random 

class Flight:

	def __init__(self):
		self.plane = Plane()

	def fly(self):
		while True:
			self.plane.turbulation()
			yield "Current orientation: {:.3f}".format(self.plane.angle)
			state = self.plane.correction()
			if state:
				yield "Orientation after correction: {:.3f}".format(self.plane.angle)
			else:
				yield "Plane crush!!!"
				break
			


class Plane:

	def __init__(self):
		self.angle = 0

	def turbulation(self):
		self.angle = random.gauss(45, 45/3)

	def correction(self):
		if self.angle > 0:
			if self.angle >= 90:
				return False
			correction = 0.5 * self.angle
			self.angle -= correction
			return True
		