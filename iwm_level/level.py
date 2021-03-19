from xml.etree.ElementTree import Element, ElementTree, SubElement
from xml.etree import ElementTree

class Level:
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 608

	def __init__(self):
		self.name = ''
		self.version = 71 # todo
		self.block_type_0_id = 0
		self.block_type_1_id = 0
		self.background_id = 0
		self.spike_type_id = 0
		self.size = (1, 1)
		self.colors = '0' * 600 # todo
		self.scroll_mode_id = 0
		self.music_id = 0

	def get_pixel_width(self):
		return Level.SCREEN_WIDTH * self.size[0]
	
	def get_pixel_height(self):
		return Level.SCREEN_HEIGHT * self.size[1]

	def save(self, filepath):
		xml_root = Element('sfm_map')

		xml_head = SubElement(xml_root, 'head')

		for name, value in [
			('name', self.name),
			('version', self.version),
			('tileset', self.block_type_0_id),
			('tileset2', self.block_type_1_id),
			('bg', self.background_id),
			('spikes', self.spike_type_id),
			('width', self.get_pixel_width()),
			('height', self.get_pixel_height()),
			('colors', self.colors),
			('scroll_mode', self.scroll_mode_id),
			('music', self.music_id),
			('num_objects', 0), # todo
		]:
			xml_head_subelement = SubElement(xml_head, name)
			xml_head_subelement.text = str(value)

		xml_objects = SubElement(xml_root, 'objects')

		with open(filepath, 'wb') as file:
			ElementTree.ElementTree(xml_root).write(file)
