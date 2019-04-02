# -*- coding: utf-8 -*-
#JSON-RPC #ref:

class Response(object):
	def __init__(self):
		super().__init__()
	def read(self):
		pass
	def write(self):
		pass
	def __getitem__(self, key):
		return getattr(self, key, None)
	def __setitem__(self, key, val):
		return setattr(self, key, val)
	def keys(self):
		return self.__dict__.keys()
	def values(self):
		return self.__dict__.values()
	def items(self):
		return self.__dict__.items()
	def __eq__(self, obj):
		return self.__class__.__name__ == obj.__class__.__name__
	def __repr__(self):
		L=['%s=%r'%(key, value) for key, value in self.__dict__.items()]
		return '%s(%s)'%(self.__class__.__name__, ', '.join(L))
	__str__ = __repr__

Request = Response