# -*- coding: utf-8 -*-
import os, sys
import uuid, time
import requests

path = os.path.join(os.path.dirname(__file__),'../model')
sys.path.insert(0, path)

from auth import *
from etc import *
from error import *

def needLoggedin(f):
	def wrap_kargs(*args, **kws):
		this = args[0]
		if this.logged_in:
			return f(*args, **kws)
		else:
			raise OVONotLoggedIn('You need to login befoire using %r' % (f.__name__))
	return wrap_kargs

class OVOClient(object):
	BASE_ENDPOINT = 'https://api.ovo.id/'
	def __init__(self,
		app_id=None,
		app_version=None,
		os_name=None,
		os_version=None,
		mac_address=None,
		device_id=None,
		notification_id=None,

		token=None,

		base_url=None,
		debug=None, *args, **kws):
		super().__init__()
		self.session = requests.session()
		self.session.headers = {
			'app-id'      : app_id,
			'App-Version' : app_version,
			'OS'          : os_name
		}
		self.app_id      = app_id
		self.app_version = app_version
		self.mac_address = mac_address
		self.token   = token
		self.device_id   = device_id
		self.os_name     = os_name
		self.os_version  = os_version
		self.debug       = debug

		self.notification_id = notification_id

		self.logged_in = False
		self.BASE_ENDPOINT = base_url if base_url else self.BASE_ENDPOINT

	def onValidLogin(self, res):
		#Function binding for token, authToken auto save
		pass

	def onValidSecurityCode(self, res, securityCode):
		pass

	def checkOnSavedCredential(self, token):
		#Function binding to check if the authToken is saved or not
		return False

	def req(self, method, url, *args, **kws):
		r = getattr(self.session, method)(self.BASE_ENDPOINT + url, *args, **kws)
		if(self.debug): print(r.text)
		return r

	def cookie(self):
		return self.session.cookies

	def unixTime(self):
		return int(time.time())

	"""
	-*- Client -*-
	"""

	def loginWithToken(self, token):
		self.session.headers.update({
			'Authorization': token
		})
		self.logged_in = True
		res = LoginWithToken()
		res_o = {
			'success': True,
			'saved'  : self.checkOnSavedCredential(token)
		}
		res.read(res_o)
		return res

	def login2FA(self, phone_number):
		assert isinstance(phone_number, (str)), 'phone_number must be a string'
		r = self.req('post', 
			'v2.0/api/auth/customer/login2FA',
			json={
				'deviceId': self.device_id,
				'mobile'  : phone_number,
			}, headers=self.session.headers)
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus  = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = Login2FAResponse()
				res.read(r.json())
				res.saved = False
				return res

	def verifyLogin2FA(self, refId, verificationCode, phone_number):
		assert isinstance(refId, str), 'refId must be a string'
		assert isinstance(verificationCode, str), 'verificationCode must be a string'
		assert isinstance(phone_number, (str)), 'phone_number must be a string'
		r = self.req('post', 
			'v2.0/api/auth/customer/login2FA/verify',
			json={
				'appVersion': self.app_version,
				'deviceId': self.device_id,
				'macAddress': self.mac_address,
				'mobile': phone_number,
				'osName': self.os_name,
				'osVersion': self.os_version,
				'pushNotificationId': self.notification_id,
				'refId': refId,
				'verificationCode': verificationCode,
			})
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus  = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = Login2FAVerifyResponse()
				res.read(r.json())
				self.onValidLogin(res)
				return res

	def loginSecurityCode(self, securityCode, updateAccessToken, message=''):
		assert isinstance(securityCode, str), 'securityCode must be a string'
		assert isinstance(updateAccessToken, str), 'updateAccessToken must be a string'
		r = self.req('post',
			'v2.0/api/auth/customer/loginSecurityCode/verify',
			json={
				'deviceUnixtime': self.unixTime(),
				'securityCode': securityCode,
				'updateAccessToken': updateAccessToken,
				'message': message,
			})
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus  = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = LoginSecurityCodeResponse()
				res.read(r.json())
				self.onValidSecurityCode(res, securityCode)
				return res

	"""
	-*- Need logged in -*-
	"""
	@needLoggedin
	def getBudget(self):
		r = self.req('get',
			'v1.0/budget/detail'
		)
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = BudgetResponse()
				res.read(r.json())
				return res

	@needLoggedin
	def getFrontModel(self):
		r = self.req('get',
			'v1.0/api/front/')
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = FrontResponse()
				res.read(r.json())
				return res

	@needLoggedin
	def generateTrxId(self, phone_number, amount):
		"""phone_number is not used??"""
		assert isinstance(phone_number, str), 'phone_number must be a string'
		assert isinstance(amount, (int)), 'amount must be a integer or float'
		data = {
			'actionMark': 'trf_ovo',
			'amount': amount,
		}
		r = self.req('post',
			'v1.0/api/auth/customer/genTrxId',
			json=data)
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = GenTrxIdResponse()
				res.read(r.json())
				return res

	@needLoggedin
	def transferOvoBalance(self, phone_number, amount, message=None):
		"""amount is in rupias"""
		assert isinstance(phone_number, str), 'phone_number must be a string'
		assert isinstance(amount, (int)), 'amount must be a integer or float'
		assert amount <= 10000, 'Amount must be greater than Rp. 10000'
		data = {
			'to': phone_number,
			'amount': amount,
			'trxId': self.generateTrxId(phone_number, amount).trxId
		}
		r = self.req('post',
			'v1.0/api/customers/transfer', json=data)
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				#checking
				res = CustomerTransferResponse()
				res.read(r.json())
				return res

	@needLoggedin
	def logout(self):
		r = self.req('get',
			'v1.0/api/auth/customer/logout')
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				err.read(r.json())
				err.httpStatus  = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = LogoutResponse()
				res.httpStatus = r.status_code
				res.read(r.json())
				return res

	""" 
	-*- UserActivity Record -*-
	"""
	@needLoggedin
	def getAllNotification(self):
		r = self.req('get',
			'v1.0/notification/status/all')
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = NotificationAllRespone()
				res.read(r.json())
				return res

	@needLoggedin
	def getUnreadNotification(self):
		r = self.req('get',
			'v1.0/notification/status/count/UNREAD')
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = NotificationUnreadResponse()
				res.read(r.json())
				return res

	@needLoggedin
	def getWalletTransaction(self, page=1, limit=10,*_, **kws):
		r = self.req('get',
			'wallet/v2/transaction', params={'page':page, 'limit': limit, **kws})
		if(self.debug):
			return r.status_code, r.headers, r.text
		else:
			if(r.status_code != 200):
				err = OVOHttpResponse()
				try: err.read(r.json())
				except: err.read({})
				err.httpStatus = r.status_code
				raise OVOUnexpectedError(err)
			else:
				res = WalletTransactionResponse()
				res.read(r.json())
				return res