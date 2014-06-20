class Wheel(object):
	wheel_type = ["small", "medium", "large"]
	def __init__(self, cost, model, wheels_type):
		"""initiating wheels, wheels type will be either 1,2,or 3 which 
		is small , medium or large"""
		self.wheels_type  = wheel_type[wheels_type]
		self.cost = cost
		self.model = model
		