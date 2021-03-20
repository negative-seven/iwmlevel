import colorsys


class Color:
	def __init__(self):
		self.hue = 0.0
		self.saturation = 0.0
		self.value = 0.0

	def as_hsv_tuple(self):
		return self.hue, self.saturation, self.value
