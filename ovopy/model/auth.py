# -*- coding: utf-8 -*-
#JSON-RPC #ref:
from base import Response

class LoginWithToken(Response):
	def __init__(self,
		success=None,
		saved=None,
		):
		super().__init__()
		self.success = success
		self.saved   = saved
	def read(self, MapObject):
		self.success = MapObject.get('success', None)
		self.saved   = MapObject.get('saved', None)

class Login2FAResponse(Response):
	def __init__(self, 
		refId=None,
		):
		super().__init__()
		self.refId = refId
	def read(self, MapObject):
		self.refId = MapObject.get('refId', None)

class Login2FAVerifyResponse(Response):
	def __init__(self,
		mobile=None,
		email=None,
		fullName=None,
		isEmailVerified=None,
		isSecurityCodeSet=None,
		updateAccessToken=None,
		):
		super().__init__()
		self.mobile   = mobile
		self.email    = email
		self.fullName = fullName
		self.isEmailVerified   = isEmailVerified
		self.isSecurityCodeSet = isSecurityCodeSet
		self.updateAccessToken = updateAccessToken
	def read(self, MapObject):
		self.mobile = MapObject.get('mobile', None)
		self.email  = MapObject.get('email', None)
		self.fullName = MapObject.get('fullName', None)
		self.isEmailVerified   = MapObject.get('isEmailVerified', None)
		self.isSecurityCodeSet = MapObject.get('isSecurityCodeSet', None)
		self.updateAccessToken = MapObject.get('updateAccessToken', None)

class LoginSecurityCodeResponse(Response):
	#emt:timeStamp -> timestamp
	def __init__(self,
		token=None,
		tokenSeed=None,
		timestamp=None,
		tokenSeedExpiredAt=None,
		displayMessage=None,
		email=None,
		fullName=None,
		isEmailVerified=None,
		isSecurityCodeSet=None,
		updateAccessToken=None,
		):
		super().__init__()
		self.token     = token
		self.tokenSeed = tokenSeed
		self.timestamp = timestamp
		self.tokenSeedExpiredAt = tokenSeedExpiredAt
		self.displayMessage     = displayMessage
		self.email              = email
		self.fullName           = fullName
		self.isEmailVerified    = isEmailVerified
		self.isSecurityCodeSet  = isSecurityCodeSet
		self.updateAccessToken  = updateAccessToken
	def read(self, MapObject):
		self.token     = MapObject.get('token', None)
		self.tokenSeed = MapObject.get('tokenSeed', None)
		self.timestamp = MapObject.get('timeStamp', None) # rewrited
		self.tokenSeedExpiredAt = MapObject.get('tokenSeedExpiredAt', None)
		self.displayMessage     = MapObject.get('displayMessage', None)
		self.email              = MapObject.get('email', None)
		self.fullName           = MapObject.get('fullName', None)
		self.isEmailVerified    = MapObject.get('isEmailVerified', None)
		self.isSecurityCodeSet  = MapObject.get('isSecurityCodeSet', None)
		self.updateAccessToken  = MapObject.get('updateAccessToken', None)


class LogoutResponse(Response):
	def __init__(self,
		):
		super().__init__()
		#NULL
	def read(self, MapObject):
		pass