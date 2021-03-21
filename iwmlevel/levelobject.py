from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


class LevelObject:
	def __init__(self, type_id: int, x = 0, y = 0, parameters = dict(), *, slot = None, events = [], slotted_objects = []):
		self.type_id = type_id
		self.x = x
		self.y = y
		self.slot = slot
		self.events = events
		self.parameters = parameters
		self.slotted_objects = slotted_objects

	def to_xml(self) -> Element:
		xml_object = Element('object')
		xml_object.attrib['type'] = str(self.type_id)
		xml_object.attrib['x'] = str(self.x)
		xml_object.attrib['y'] = str(self.y)
		if self.slot is not None:
			xml_object.attrib['slot'] = str(self.slot)

		for event in self.events:
			xml_object.append(event.to_xml())

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_object, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = str(value)

		for slotted_object in self.slotted_objects:
			xml_slotted_object = slotted_object.to_xml()
			xml_slotted_object.tag = 'obj'
			xml_object.append(xml_slotted_object)

		return xml_object

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')
