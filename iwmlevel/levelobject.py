from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


class LevelObject:
	def __init__(self, type_id: int, x = 0, y = 0, parameters = dict()):
		self.type_id = type_id
		self.x = x
		self.y = y
		self.parameters = parameters

	def to_xml(self) -> Element:
		xml_object = Element('object')
		xml_object.attrib['type'] = str(self.type_id)
		xml_object.attrib['x'] = str(self.x)
		xml_object.attrib['y'] = str(self.y)

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_object, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = str(value)

		return xml_object

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')
