# -*- coding: utf-8 -*-
import os, sys
try:
	import ovopy
except ImportError:
	print('Module `ovopy` is not installed yet.')
	print('Please run `python3 setup.py install` within this folder.')
	os._exit(1)

ovo = ovopy.OVO(debug=False) 

phone_number = input('Phone number >> ')
l2fa = ovo.login(phone_number)
print(ovo.settings)
print(l2fa)

if l2fa == ovopy.model.auth.LoginWithToken():
	print('You don\'t need to login, you still have token')
	print('Let\'s see if it still valid')

	#print(ovo.getBudget())
	print(ovo.getFrontModel())
	#print(ovo.generateTrxId('xx', 10000))
	#print(ovo.transferOvoBalance('xx', 10000))
	#print(ovo.getUnreadNotification())
	#print(ovo.getWalletTransaction(page=1, limit=1))
	#print(ovo.getAllNotification())
	#print(ovo.getUnreadNotification())
	os._exit(1)

smsVerificationCode = input('SMS Verification Code >> ')
vl2fa = ovo.verifyLogin2FA(l2fa.refId, smsVerificationCode,phone_number)
print(vl2fa)

securityPincode = input('Security Pincode >> ')
lsc = ovo.loginSecurityCode(securityPincode, vl2fa.updateAccessToken)
print(lsc)