from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


class Action:
	def __init__(self, id: int, parameters = dict()):
		self.id = id
		self.parameters = parameters

	def to_xml(self) -> Element:
		xml_action = Element('event')
		xml_action.attrib['eventIndex'] = str(self.id)

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_action, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = str(value)

		return xml_action

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')
