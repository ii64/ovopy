# -*- coding: utf-8 -*-
import os, sys
try: import ujson as json
except: import json

import livejson

class OVOAutosave(object):
	def __init__(self,
		*args, **kws):
		pass
		#	{ 
		#		phone_number : {
		#			token: string[JWT],
		#			tokenSeed: string[HEX]
		#			accessToken: string[*],
		#			securityCode: string[4]	
		#		},
		#		phone_number2 : {
		#			token: string[JWT],
		#			tokenSeed: string[HEX]
		#			accessToken: string[*]
		#			securityCode: string[4]
		#		}
		#	} 

	def resolveSavedAccount(self, number_phone):
		return livejson.File(number_phone + '.json')

	def resolveSettingsFromToken(self, token):
		all_json_file = [fjs for fjs in os.listdir('.') if fjs.endswith('.json')]
		for c_file in all_json_file:
			data = livejson.File(c_file)
			if data.data.get('token', None) == token:
				return data
		return {}

	def createNewOrUpdateExist(self, number_phone, params={}):
		data = livejson.File(number_phone + '.json')
		data.update(params)

	def checkOnSavedCredential(self, token):
		all_json_file = [fjs for fjs in os.listdir('.') if fjs.endswith('.json')]
		for c_file in all_json_file:
			data = livejson.File(c_file)
			if data.data.get('token', None):
				return True
		return False