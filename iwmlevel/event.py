from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from .action import Action
from .eventtype import EventType


class Event:
	def __init__(self, event_type: EventType, parameters = None):
		if parameters is None:
			parameters = dict()

		self.type = event_type
		self.actions = []
		self.parameters = parameters

	def to_xml(self) -> Element:
		xml_event = Element('event')
		xml_event.attrib['eventIndex'] = str(int(self.type))

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_event, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = f'{value:g}'

		for action in self.actions:
			xml_event.append(action.to_xml())

		return xml_event

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')

	@staticmethod
	def from_xml(xml_event: Element):
		event = Event(0)
		event.type = EventType(int(xml_event.attrib['eventIndex']))

		for child in xml_event:
			if child.tag == 'param':
				event.parameters[child.attrib['key']] = float(child.attrib['val'])
			elif child.tag == 'event':
				event.actions.append(Action.from_xml(child))

		return event

	@staticmethod
	def from_xml_string(xml_string: str):
		return Event.from_xml(ElementTree.fromstring(xml_string))
