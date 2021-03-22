from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from .event import Event
from .levelobjecttype import LevelObjectType


class LevelObject:
	def __init__(self, object_type: LevelObjectType, x = 0, y = 0, parameters = None, *, slot = None, sprite_angle = None, events = None,
				 slotted_objects=None):
		if parameters is None:
			parameters = dict()
		if events is None:
			events = []
		if slotted_objects is None:
			slotted_objects = []

		self.type = object_type
		self.x = x
		self.y = y
		self.slot = slot
		self.rotation = sprite_angle
		self.events = events
		self.parameters = parameters
		self.slotted_objects = slotted_objects

	def to_xml(self) -> Element:
		xml_object = Element('object')
		xml_object.attrib['type'] = str(int(self.type))
		xml_object.attrib['x'] = str(self.x)
		xml_object.attrib['y'] = str(self.y)
		if self.slot is not None:
			xml_object.attrib['slot'] = str(self.slot)
		if self.rotation is not None:
			xml_object.attrib['sprite_angle'] = str(self.rotation)

		for event in self.events:
			xml_object.append(event.to_xml())

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_object, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = f'{value:g}'

		for slotted_object in self.slotted_objects:
			xml_slotted_object = slotted_object.to_xml()
			xml_slotted_object.tag = 'obj'
			xml_object.append(xml_slotted_object)

		return xml_object

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')

	@staticmethod
	def from_xml(xml_object: Element):
		level_object = LevelObject(0)

		for key, value in xml_object.attrib.items():
			if key == 'type':
				level_object.type = LevelObjectType(int(value))
			elif key == 'x':
				level_object.x = int(value)
			elif key == 'y':
				level_object.y = int(value)
			elif key == 'slot':
				level_object.slot = int(value)
			elif key == 'sprite_angle':
				level_object.rotation = int(value)

		for child in xml_object:
			if child.tag == 'event':
				level_object.events.append(Event.from_xml(child))
			elif child.tag == 'param':
				level_object.parameters[child.attrib['key']] = float(child.attrib['val'])
			elif child.tag == 'obj':
				level_object.slotted_objects.append(LevelObject.from_xml(child))

		return level_object

	@staticmethod
	def from_xml_string(xml_string: str):
		return LevelObject.from_xml(ElementTree.fromstring(xml_string))
