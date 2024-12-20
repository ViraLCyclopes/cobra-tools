from generated.array import Array
from generated.formats.bnk.compounds.HircObject import HircObject
from generated.formats.bnk.imports import name_type_map


class EventAction(HircObject):

	__name__ = 'EventAction'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.scope = name_type_map['ActionScope'](self.context, 0, None)
		self.action_type = name_type_map['Ubyte'](self.context, 0, None)
		self.game_obj = name_type_map['Uint'](self.context, 0, None)
		self.zero_1 = name_type_map['Ubyte'](self.context, 0, None)
		self.num_params = name_type_map['Ubyte'](self.context, 0, None)
		self.params = Array(self.context, 0, None, (0,), name_type_map['Ubyte'])
		self.values = Array(self.context, 0, None, (0,), name_type_map['Uint'])
		self.zero_2 = name_type_map['Ubyte'](self.context, 0, None)
		self.four = name_type_map['Ubyte'](self.context, 0, None)
		self.flag = name_type_map['Ubyte'](self.context, 0, None)
		self.extra_id = name_type_map['Ushort'](self.context, 0, None)
		self.state_group_id = name_type_map['Uint'](self.context, 0, None)
		self.state_id = name_type_map['Uint'](self.context, 0, None)
		self.switch_group_id = name_type_map['Uint'](self.context, 0, None)
		self.switch_id = name_type_map['Uint'](self.context, 0, None)
		self.end_flag = name_type_map['Ubyte'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'scope', name_type_map['ActionScope'], (0, None), (False, None), (None, None)
		yield 'action_type', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'game_obj', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'zero_1', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'num_params', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'params', Array, (0, None, (None,), name_type_map['Ubyte']), (False, None), (None, None)
		yield 'values', Array, (0, None, (None,), name_type_map['Uint']), (False, None), (None, None)
		yield 'zero_2', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'four', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'flag', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'extra_id', name_type_map['Ushort'], (0, None), (False, None), (None, True)
		yield 'state_group_id', name_type_map['Uint'], (0, None), (False, None), (None, True)
		yield 'state_id', name_type_map['Uint'], (0, None), (False, None), (None, True)
		yield 'switch_group_id', name_type_map['Uint'], (0, None), (False, None), (None, True)
		yield 'switch_id', name_type_map['Uint'], (0, None), (False, None), (None, True)
		yield 'end_flag', name_type_map['Ubyte'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'scope', name_type_map['ActionScope'], (0, None), (False, None)
		yield 'action_type', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'game_obj', name_type_map['Uint'], (0, None), (False, None)
		yield 'zero_1', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_params', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'params', Array, (0, None, (instance.num_params,), name_type_map['Ubyte']), (False, None)
		yield 'values', Array, (0, None, (instance.num_params,), name_type_map['Uint']), (False, None)
		yield 'zero_2', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'four', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'flag', name_type_map['Ubyte'], (0, None), (False, None)
		if instance.action_type == 4:
			yield 'extra_id', name_type_map['Ushort'], (0, None), (False, None)
		if instance.action_type == 18:
			yield 'state_group_id', name_type_map['Uint'], (0, None), (False, None)
			yield 'state_id', name_type_map['Uint'], (0, None), (False, None)
		if instance.action_type == 25:
			yield 'switch_group_id', name_type_map['Uint'], (0, None), (False, None)
			yield 'switch_id', name_type_map['Uint'], (0, None), (False, None)
		yield 'end_flag', name_type_map['Ubyte'], (0, None), (False, None)
