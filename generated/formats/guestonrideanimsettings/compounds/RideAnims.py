from generated.array import Array
from generated.formats.guestonrideanimsettings.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class RideAnims(MemStruct):

	"""
	PZ 128 bytes
	PC 136 bytes
	"""

	__name__ = 'RideAnims'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.bools = Array(self.context, 0, None, (0,), name_type_map['Ubyte'])
		self.floats = Array(self.context, 0, None, (0,), name_type_map['Float'])
		self.count = name_type_map['Uint64'](self.context, 0, None)
		self.bools = Array(self.context, 0, None, (0,), name_type_map['Ubyte'])
		self.floats = Array(self.context, 0, None, (0,), name_type_map['Float'])
		self.anim_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.am = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.af = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.tm = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.tf = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.cf = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.cm = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.anims = name_type_map['ArrayPointer'](self.context, self.count, name_type_map['AnimPair'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'anim_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'am', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'af', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'tm', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'tf', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'cf', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'cm', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'bools', Array, (0, None, (44,), name_type_map['Ubyte']), (False, None), (lambda context: context.version == 18, None)
		yield 'floats', Array, (0, None, (5,), name_type_map['Float']), (False, None), (lambda context: context.version == 18, None)
		yield 'anims', name_type_map['ArrayPointer'], (None, name_type_map['AnimPair']), (False, None), (lambda context: context.version == 18, None)
		yield 'count', name_type_map['Uint64'], (0, None), (False, None), (lambda context: context.version == 18, None)
		yield 'bools', Array, (0, None, (56,), name_type_map['Ubyte']), (False, None), (lambda context: not (context.version == 18), None)
		yield 'floats', Array, (0, None, (4,), name_type_map['Float']), (False, None), (lambda context: not (context.version == 18), None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'anim_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'am', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'af', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'tm', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'tf', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'cf', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'cm', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		if instance.context.version == 18:
			yield 'bools', Array, (0, None, (44,), name_type_map['Ubyte']), (False, None)
			yield 'floats', Array, (0, None, (5,), name_type_map['Float']), (False, None)
			yield 'anims', name_type_map['ArrayPointer'], (instance.count, name_type_map['AnimPair']), (False, None)
			yield 'count', name_type_map['Uint64'], (0, None), (False, None)
		if not (instance.context.version == 18):
			yield 'bools', Array, (0, None, (56,), name_type_map['Ubyte']), (False, None)
			yield 'floats', Array, (0, None, (4,), name_type_map['Float']), (False, None)