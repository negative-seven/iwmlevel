from .color import Color


class GraphicsData:
	def __init__(self):
		self.type_id = 0
		self.color = Color()
		self.color_hsv_inverted = [False, False, False]
