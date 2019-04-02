# -*- coding: utf-8 -*-
#JSON-RPC #ref:
from base import *

class AmmountException(Exception):
	pass

class OVOException(Exception):
	pass

class OVONotLoggedIn(Exception):
	pass

class OVOUsageError(Exception):
	pass

class OVOHttpResponse(Response):
	def __init__(self, 
		code=None,
		status=None,
		message=None,
		content=None,
		data=None,
		):
		super().__init__()
		self.code    = code
		self.status  = status
		self.message = message
		self.content = content
		self.data    = data
	def read(self, MapObject):
		self.code    = MapObject.get('code', None)
		self.status  = MapObject.get('status', None)
		self.message = MapObject.get('message', None)
		self.content = MapObject.get('content', None)
		self.data    = MapObject.get('data', None)

class OVOUnexpectedError(Exception):
	pass