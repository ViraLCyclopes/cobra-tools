from generated.formats.achievements.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class ConditionCheck(MemStruct):

	"""
	PZ 40 bytes
	"""

	__name__ = 'ConditionCheck'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.conditions_2_count = name_type_map['Uint64'](self.context, 0, None)
		self.conditions_count = name_type_map['Uint64'](self.context, 0, None)
		self.condition_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.conditions_2 = name_type_map['ArrayPointer'](self.context, self.conditions_2_count, name_type_map['ConditionRef2Ptr'])
		self.conditions = name_type_map['ArrayPointer'](self.context, self.conditions_count, name_type_map['ConditionRefPtr'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'condition_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'conditions_2', name_type_map['ArrayPointer'], (None, name_type_map['ConditionRef2Ptr']), (False, None), (None, None)
		yield 'conditions_2_count', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'conditions', name_type_map['ArrayPointer'], (None, name_type_map['ConditionRefPtr']), (False, None), (None, None)
		yield 'conditions_count', name_type_map['Uint64'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'condition_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'conditions_2', name_type_map['ArrayPointer'], (instance.conditions_2_count, name_type_map['ConditionRef2Ptr']), (False, None)
		yield 'conditions_2_count', name_type_map['Uint64'], (0, None), (False, None)
		yield 'conditions', name_type_map['ArrayPointer'], (instance.conditions_count, name_type_map['ConditionRefPtr']), (False, None)
		yield 'conditions_count', name_type_map['Uint64'], (0, None), (False, None)