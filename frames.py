class Frame(object):
	frame_type = ["aluminium", "carbon", "steel"]
	def __init__(self, cost, weight, frames_type):
		"""initiating frames, frames type will be either 1,2,or 3 which 
		is aluminium , carbon or steel"""
		self.frames_type  = frame_type[frames_type]
		self.cost = cost
		self.weight = weight