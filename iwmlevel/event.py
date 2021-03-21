from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from .action import Action


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

	@staticmethod
	def from_xml(xml_event: Element):
		event = Event(0)
		event.id = int(xml_event.attrib['eventIndex'])

		for child in xml_event:
			if child.tag == 'param':
				event.parameters[child.attrib['key']] = int(child.attrib['val'])
			elif child.tag == 'event':
				event.actions.append(Action.from_xml(child))

		return event

	@staticmethod
	def from_xml_string(xml_string: str):
		return Event.from_xml(ElementTree.fromstring(xml_string))
