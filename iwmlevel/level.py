import struct
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from .graphics_data import GraphicsData


class Level:
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 608

	def __init__(self, name = '', size = (1, 1), game_version = 76):
		self.name = name
		self.version = game_version
		self.block_0_graphics = GraphicsData()
		self.block_1_graphics = GraphicsData()
		self.background_graphics = GraphicsData()
		self.spike_graphics = GraphicsData()
		self.size = size
		self.scroll_mode_id = 0
		self.music_id = 0
		self.objects = []

	def get_pixel_width(self) -> int:
		return Level.SCREEN_WIDTH * self.size[0]
	
	def get_pixel_height(self) -> int:
		return Level.SCREEN_HEIGHT * self.size[1]

	def to_xml(self) -> Element:
		xml_map = Element('sfm_map')

		xml_head = SubElement(xml_map, 'head')

		for name, value in [
			('name', self.name),
			('version', self.version),
			('tileset', self.block_0_graphics.type_id),
			('tileset2', self.block_1_graphics.type_id),
			('bg', self.background_graphics.type_id),
			('spikes', self.spike_graphics.type_id),
			('width', self.get_pixel_width()),
			('height', self.get_pixel_height()),
			('colors', None), # handled later
			('scroll_mode', self.scroll_mode_id),
			('music', self.music_id),
			('num_objects', len(self.objects)),
		]:
			xml_head_subelement = SubElement(xml_head, name)
			xml_head_subelement.text = str(value)

		colors_string = ''
		def colors_string_append_integer(x: int):
			nonlocal colors_string
			colors_string += x.to_bytes(4, byteorder='little').hex().upper()
		def colors_string_append_float(x: float):
			nonlocal colors_string
			colors_string += struct.pack('d', x).hex().upper()
		colors_string_append_integer(0x25a) # probably 2d array identifier
		colors_string_append_integer(6) # array height
		colors_string_append_integer(4) # array width
		for get_inverted_flag in (False, True):
			for hsv_index in range(3):
				for graphics_data in (
						self.block_0_graphics,
						self.background_graphics,
						self.spike_graphics,
						self.block_1_graphics,
				):
					colors_string_append_integer(0)
					if get_inverted_flag:
						colors_string_append_float(1.0 if graphics_data.color_hsv_inverted[hsv_index] else 0.0)
					else:
						colors_string_append_float(graphics_data.color.as_hsv_tuple()[hsv_index])
		xml_head.find('colors').text = colors_string

		xml_objects = SubElement(xml_map, 'objects')

		return xml_map

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')

	def save(self, filepath: str) -> None:
		with open(filepath, 'w') as f:
			f.write(self.to_xml_string())
