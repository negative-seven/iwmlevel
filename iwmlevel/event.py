from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


class Event:
	def __init__(self, id: int, parameters = None):
		if parameters is None:
			parameters = dict()

		self.id = id
		self.actions = []
		self.parameters = parameters

	def to_xml(self) -> Element:
		xml_event = Element('event')
		xml_event.attrib['eventIndex'] = str(self.id)

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_event, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = str(value)

		for action in self.actions:
			xml_event.append(action.to_xml())

		return xml_event

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')
