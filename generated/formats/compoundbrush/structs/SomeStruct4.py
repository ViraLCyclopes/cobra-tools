from generated.formats.compoundbrush.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class SomeStruct4(MemStruct):

	__name__ = 'SomeStruct4'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.brush_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.some_struct_4_sub_1 = name_type_map['Pointer'](self.context, 0, name_type_map['SomeStruct4Sub1'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'brush_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'some_struct_4_sub_1', name_type_map['Pointer'], (0, name_type_map['SomeStruct4Sub1']), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'brush_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'some_struct_4_sub_1', name_type_map['Pointer'], (0, name_type_map['SomeStruct4Sub1']), (False, None)
