from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from iwmlevel.actiontype import ActionType


class Action:
	def __init__(self, action_type: ActionType, parameters = None):
		if parameters is None:
			parameters = dict()
			
		self.type = action_type
		self.parameters = parameters

	def to_xml(self) -> Element:
		xml_action = Element('event')
		xml_action.attrib['eventIndex'] = str(int(self.type))

		for key, value in self.parameters.items():
			xml_parameter = SubElement(xml_action, 'param')
			xml_parameter.attrib['key'] = key
			xml_parameter.attrib['val'] = f'{value:g}'

		return xml_action

	def to_xml_string(self) -> str:
		return ElementTree.tostring(self.to_xml(), encoding='utf-8').decode('utf-8')

	@staticmethod
	def from_xml(xml_action: Element):
		action = Action(0)
		action.type = ActionType(int(xml_action.attrib['eventIndex']))

		for child in xml_action:
			if child.tag == 'param':
				action.parameters[child.attrib['key']] = float(child.attrib['val'])

		return action

	@staticmethod
	def from_xml_string(xml_string: str):
		return Action.from_xml(ElementTree.fromstring(xml_string))
