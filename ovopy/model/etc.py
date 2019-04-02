# -*- coding: utf-8 -*-
#JSON-RPC #ref:
from base import Response

class History(Response):
	def __init__(self,
		amount=None,
		categoryId=None,
		spending=None,
		):
		super().__init__()
		self.amount     = amount
		self.categoryId = categoryId
		self.spending   = spending
	def read(self, MapObject):
		self.amount     = MapObject.get('amount', None)
		self.categoryId = MapObject.get('categoryId', None)
		self.spending   = MapObject.get('spending', None)

class Telephone(Response):
	def __init__(self,
		id=None,
		number=None,
		ext=None,
		telephoneType=None,
		status=None,
		dateCreated=None,
		dateUpdated=None,
		):
		super().__init__()
		self.id     = id
		self.number = number
		self.ext    = ext
		self.telephoneType = telephoneType
		self.status        = status
		self.dateCreated   = dateCreated
		self.dateUpdated   = dateUpdated
	def read(self, MapObject):
		self.id     = MapObject.get('id', None)
		self.number = MapObject.get('number', None)
		self.ext    = MapObject.get('ext', None)
		self.telephoneType = MapObject.get('telephoneType', None)
		self.status        = MapObject.get('status', None)
		self.dateCreated   = MapObject.get('dateCreated', None)
		self.dateUpdated   = MapObject.get('dateUpdated', None)

class Email(Response):
	def __init__(self,
		id=None,
		address=None,
		status=None,
		dateCreated=None,
		dateUpdated=None,
		):
		super().__init__()
		self.id          = id
		self.address     = address
		self.status      = status
		self.dateCreated = dateCreated
		self.dateUpdated = dateUpdated
	def read(self, MapObject):
		self.id          = MapObject.get('id', None)
		self.address     = MapObject.get('address', None)
		self.status      = MapObject.get('status', None)
		self.dateCreated = MapObject.get('dateCreated', None)
		self.dateUpdated = MapObject.get('dateUpdated', None)

class Organization(Response):
	def __init__(self,
		dateCreated=None,
		dateUpdated=None,
		status=None,
		createdBy=None,
		updatedBy=None,
		name=None,
		organizationId=None,
		email=None,
		phoneNumber=None,
		):
		super().__init__()
		self.dateCreated = dateCreated
		self.dateUpdated = dateUpdated
		self.status      = status
		self.createdBy   = createdBy
		self.updatedBy   = updatedBy
		self.name        = name
		self.organizationId = organizationId
		self.email       = email
		self.phoneNumber = phoneNumber
	def read(self, MapObject):
		self.dateCreated = MapObject.get('dateCreated', None)
		self.dateUpdated = MapObject.get('dateUpdated', None)
		self.status      = MapObject.get('status', None)
		self.createdBy   = MapObject.get('createdBy', None)
		self.updatedBy   = MapObject.get('updatedBy', None)
		self.name        = MapObject.get('name', None)
		self.organizationId = MapObject.get('organizationId', None)
		self.email       = MapObject.get('email', None)
		self.phoneNumber = MapObject.get('phoneNumber', None)

class Profile(Response):
	#emt:type -> type_
	def __init__(self,
		dateCreated=None,
		dateUpdated=None,
		status=None,
		createdBy=None,
		updatedBy=None,
		fullName=None,
		nickName=None,
		deviceId=None,
		lockStatus=None,
		type_=None,
		level=None,
		state=None,
		ktpCard=None,
		lmpCard=None,
		passport=None,
		document=None,
		refNo=None,
		userLevel=None,
		ovoId=None,
		dateOfBirth=None,
		address=None,

		telephones=None,
		emails=None,
		cards=None,
		macAddress=None,
		drivers=None,
		ovoCard=None,
		organization=None,
		bonus=None,
		mobilePhoneNumber=None,
		email=None,
		registrationOrigin=None,
		dateOnUpgrade=None,
		birthPlace=None,
		religion=None,
		nationality=None,
		npwpCard=None,
		company=None,
		family=None,
		occupation=None,
		motherMaidenName=None,
		correspondenceType=None,
		cif=None,
		firstSignIn=None,
		lastSignIn=None,
		camId=None,
		):
		super().__init__()
		self.dateCreated = dateCreated
		self.dateUpdated = dateUpdated
		self.status      = status
		self.createdBy   = createdBy
		self.updatedBy   = updatedBy
		self.fullName    = fullName
		self.nickName    = nickName
		self.deviceId    = deviceId
		self.lockStatus  = lockStatus
		self.type_       = type_
		self.level       = level
		self.state       = state
		self.ktpCard     = ktpCard
		self.lmpCard     = lmpCard
		self.passport    = passport
		self.document    = document
		self.refNo       = refNo
		self.userLevel   = userLevel
		self.ovoId       = ovoId
		self.dateOfBirth = dateOfBirth
		self.address     = address

		self.telephones   = telephones
		self.emails       = emails
		self.cards        = cards
		self.macAddress   = macAddress
		self.drivers      = drivers
		self.ovoCard      = ovoCard
		self.organization = organization
		self.bonus        = bonus
		self.mobilePhoneNumber  = mobilePhoneNumber
		self.email              = email
		self.registrationOrigin = registrationOrigin
		self.dateOnUpgrade      = dateOnUpgrade
		self.birthPlace         = birthPlace
		self.religion           = religion
		self.nationality        = nationality
		self.npwpCard   = npwpCard
		self.company    = company
		self.family     = family
		self.occupation = occupation
		self.motherMaidenName   = motherMaidenName
		self.correspondenceType = correspondenceType
		self.cif         = cif
		self.firstSignIn = firstSignIn
		self.lastSignIn  = lastSignIn
		self.camId       = camId
	def read(self, MapObject):
		self.dateCreated = MapObject.get('dateCreated', None)
		self.dateUpdated = MapObject.get('dateUpdated', None)
		self.status      = MapObject.get('status', None)
		self.createdBy   = MapObject.get('createdBy', None)
		self.updatedBy   = MapObject.get('updatedBy', None)
		self.fullName    = MapObject.get('fullName', None)
		self.nickName    = MapObject.get('nickName', None)
		self.deviceId    = MapObject.get('deviceId', None)
		self.lockStatus  = MapObject.get('lockStatus', None)
		self.type_       = MapObject.get('type', None)
		self.level       = MapObject.get('level', None)
		self.state       = MapObject.get('state', None)
		self.ktpCard     = MapObject.get('ktpCard', None)
		self.lmpCard     = MapObject.get('lmpCard', None)
		self.passport    = MapObject.get('passport', None)
		self.document    = MapObject.get('document', None)
		self.refNo       = MapObject.get('refNo', None)
		self.userLevel   = MapObject.get('userLevel', None)
		self.ovoId       = MapObject.get('ovoId', None)
		self.dateOfBirth = MapObject.get('dateOfBirth ', None)
		self.address     = MapObject.get('address', None)

		for item1 in MapObject.get('telephones', []):
			if self.telephones == None:
				self.telephones = []
			ctx = Telephone()
			ctx.read(item1)
			self.telephones.append(ctx)

		for item2 in MapObject.get('emails', []):
			if self.emails == None:
				self.emails = []
			ctx = Email()
			ctx.read(item2)
			self.emails.append(ctx)

		self.cards        = MapObject.get('cards', None)
		self.macAddress   = MapObject.get('macAddress', None)
		self.drivers      = MapObject.get('drivers', None)
		self.ovoCard      = MapObject.get('ovoCard', None)
		ctx = Organization()
		ctx.read( MapObject.get('organization', {}) )
		self.organization = ctx
		self.bonus        = MapObject.get('bonus', None)
		self.mobilePhoneNumber  = MapObject.get('mobilePhoneNumber', None)
		self.email              = MapObject.get('email', None)
		self.registrationOrigin = MapObject.get('registrationOrigin', None)
		self.dateOnUpgrade      = MapObject.get('dateOnUpgrade', None)
		self.birthPlace         = MapObject.get('birthPlace', None)
		self.religion           = MapObject.get('religion', None)
		self.nationality        = MapObject.get('nationality', None)
		self.npwpCard   = MapObject.get('npwpCard', None)
		self.company    = MapObject.get('company', None)
		self.family     = MapObject.get('family', None)
		self.occupation = MapObject.get('occupation', None)
		self.motherMaidenName   = MapObject.get('motherMaidenName', None)
		self.correspondenceType = MapObject.get('correspondenceType', None)
		self.cif         = MapObject.get('cif', None)
		self.firstSignIn = MapObject.get('firstSignIn', None)
		self.lastSignIn  = MapObject.get('lastSignIn', None)
		self.camId       = MapObject.get('camId', None)

class BudgetResponse(Response):
	def __init__(self,
		budget=None,
		totalSpending=None,
		cycleDate=None,
		summary=None,
		):
		super().__init__()
		self.budget = budget
		self.totalSpending = totalSpending
		self.cycleDate     = cycleDate
		self.summary       = summary
	def read(self, MapObject):
		self.budget = History()
		self.budget.read( MapObject.get('budget', {}) )
		self.totalSpending = MapObject.get('totalSpending', None)
		self.cycleDate     = MapObject.get('cycleDate', None)
		self.summary = []
		for summary in MapObject.get('summary', []):
			ctx = History()
			ctx.read(summary)
			self.summary.append(ctx)

class CustomerTransferResponse(Response):
	#emk:dynamic_reading
	def __init__(self,
		code=None,
		message=None,
		isOvo=None,
		):
		super().__init__()
		self.code = code
		self.message = message
		self.isOvo   = isOvo
	def read(self, MapObject):
		for k,v in MapObject.items():
			if k in ['type']:
				k = k + '_'
			setattr(self, k, v)

class Balance(Response):
	def __init__(self,
		card_balance=None,
		card_no=None,
		payment_method=None,
		):
		super().__init__()
		self.card_balance   = card_balance
		self.card_no        = card_no
		self.payment_method = payment_method
	def read(self, MapObject):
		self.card_balance   = MapObject.get('card_balance', None)
		self.card_no        = MapObject.get('card_no', None)
		self.payment_method = MapObject.get('payment_method', None)

class Permission(Response):
	def __init__(self,
		id=None,
		menuName=None,
		isEnabled=None,
		state=None,
		childMenu=None,
		):
		super().__init__()
		self.id        = id
		self.menuName  = menuName
		self.isEnabled = isEnabled
		self.state     = state
		self.childMenu = childMenu
	def read(self, MapObject):
		self.id        = MapObject.get('id', None)
		self.menuName  = MapObject.get('menuName', None)
		self.isEnabled = MapObject.get('isEnabled', None)
		self.state     = MapObject.get('state', None)
		self.childMenu = None
		for item in MapObject.get('childMenu', []):
			ctx = Permission()
			ctx.read(item)
			if self.childMenu == None:
				self.childMenu = []
			self.childMenu.append(ctx)


class FrontResponse(Response):
	def __init__(self,
		balance=None,
		permissions=None,
		profile=None,
		):
		super().__init__()
		self.balance     = balance
		self.permissions = permissions
		self.profile     = profile
	def read(self, MapObject):
		self.balance     = {}
		for k,v in MapObject.get('balance', {}).items():
			ctx = Balance()
			ctx.read(v)
			self.balance[k] = ctx
		self.permissions = []
		for permission in MapObject.get('permissions', []):
			ctx = Permission()
			ctx.read(permission)
			self.permissions.append(ctx)
		ctx = Profile()
		ctx.read( MapObject.get('profile', {}) )
		self.profile     = ctx

class GenTrxIdResponse(Response):
	def __init__(self,
		trxId=None,
		):
		super().__init__()
		self.trxId = trxId
	def read(self, MapObject):
		self.trxId = MapObject.get('trxId', None)

class Notification(Response):
	def __init__(self,
		id=None,
		channelType=None,
		messageType=None,
		subject=None,
		message=None,
		dateCreated=None,
		status=None,
		receiver=None,
		):
		super().__init__()
		self.id = id
		self.channelType = channelType
		self.messageType = messageType
		self.subject     = subject
		self.message     = message
		self.dateCreated = dateCreated
		self.status      = status
		self.receiver    = receiver
	def read(self, MapObject):
		self.id = MapObject.get('id', None)
		self.channelType = MapObject.get('channelType', None)
		self.messageType = MapObject.get('messageType', None)
		self.subject     = MapObject.get('subject', None)
		self.message     = MapObject.get('message', None)
		self.dateCreated = MapObject.get('dateCreated', None)
		self.status      = MapObject.get('status', None)
		self.receiver    = MapObject.get('receiver', None)

class NotificationAllRespone(Response):
	def __init__(self,
		notifications=None,
		):
		super().__init__()
		self.notifications = notifications
	def read(self, MapObject):
		for item1 in MapObject.get('notifications', []):
			if self.notifications == None:
				self.notifications = []
			ctx = Notification()
			ctx.read(item1)
			self.notifications.append(ctx)

class NotificationUnreadResponse(Response):
	def __init__(self,
		Total=None,
		):
		super().__init__()
		self.Total = Total
	def read(self, MapObject):
		self.Total = MapObject.get('Total', None)

class Transaction(Response):
	def __init__(self,
		icon_url=None,
		category_id=None,
		category_name=None,
		merchant_id=None,
		merchant_name=None,
		merchant_invoice=None,
		transaction_type=None,
		transaction_type_id=None,
		transaction_date=None,
		transaction_time=None,
		transaction_amount=None,
		transaction_fee=None,
		transaction_amount_text=None,
		name=None,
		card_no=None,
		ovo_earn=None,
		ovo_used=None,
		emoney_used=None,
		emoney_topup=None,
		emoney_bonus=None,
		emoney_used_text=None,
		emoney_topup_text=None,
		emoney_bonus_text=None,
		desc1=None,
		desc2=None,
		desc3=None,
		status=None,
		pending_message=None,
		ui_type=None,
		):
		super().__init__()
		self.icon_url            = icon_url
		self.category_id         = category_id
		self.category_name       = category_name
		self.merchant_id         = merchant_id
		self.merchant_name       = merchant_name
		self.merchant_invoice    = merchant_invoice
		self.transaction_type    = transaction_type
		self.transaction_type_id = transaction_type_id
		self.transaction_date    = transaction_date
		self.transaction_time    = transaction_time
		self.transaction_amount  = transaction_amount
		self.transaction_fee     = transaction_fee
		self.transaction_amount_text = transaction_amount_text
		self.name                = name
		self.card_no             = card_no
		self.ovo_earn            = ovo_earn
		self.ovo_used            = ovo_used
		self.emoney_used         = emoney_used
		self.emoney_topup        = emoney_topup
		self.emoney_bonus        = emoney_bonus
		self.emoney_used_text    = emoney_used_text
		self.emoney_topup_text   = emoney_topup_text
		self.emoney_bonus_text   = emoney_bonus_text
		self.desc1               = desc1
		self.desc2               = desc2
		self.desc3               = desc3
		self.status              = status
		self.pending_message     = pending_message
		self.ui_type             = ui_type
	def read(self, MapObject):
		self.icon_url            = MapObject.get('icon_url', None)
		self.category_id         = MapObject.get('category_id', None)
		self.category_name       = MapObject.get('category_name', None)
		self.merchant_id         = MapObject.get('merchant_id', None)
		self.merchant_name       = MapObject.get('merchant_name', None)
		self.merchant_invoice    = MapObject.get('merchant_invoice', None)
		self.transaction_type    = MapObject.get('transaction_type', None)
		self.transaction_type_id = MapObject.get('transaction_type_id', None)
		self.transaction_date    = MapObject.get('transaction_date', None)
		self.transaction_time    = MapObject.get('transaction_time', None)
		self.transaction_amount  = MapObject.get('transaction_amount', None)
		self.transaction_fee     = MapObject.get('transaction_fee', None)
		self.transaction_amount_text = MapObject.get('transaction_amount_text', None)
		self.name                = MapObject.get('name', None)
		self.card_no             = MapObject.get('card_no', None)
		self.ovo_earn            = MapObject.get('ovo_earn', None)
		self.ovo_used            = MapObject.get('ovo_used', None)
		self.emoney_used         = MapObject.get('emoney_used', None)
		self.emoney_topup        = MapObject.get('emoney_topup', None)
		self.emoney_bonus        = MapObject.get('emoney_bonus', None)
		self.emoney_used_text    = MapObject.get('emoney_used_text', None)
		self.emoney_topup_text   = MapObject.get('emoney_topup_text', None)
		self.emoney_bonus_text   = MapObject.get('emoney_bonus_text', None)
		self.desc1               = MapObject.get('desc1', None)
		self.desc2               = MapObject.get('desc2', None)
		self.desc3               = MapObject.get('desc3', None)
		self.status              = MapObject.get('status', None)
		self.pending_message     = MapObject.get('pending_message', None)
		self.ui_type             = MapObject.get('ui_type', None)
class Wallet(Response):
	def __init__(self,
		pending=None,
		complete=None,
		):
		super().__init__()
		self.pending  = None
		self.complete = None
	def read(self, MapObject):
		for item1 in MapObject.get('pending', []):
			if self.pending == None:
				self.pending = []
			ctx = Transaction()
			ctx.read(item1)
			self.pending.append(ctx)
		for item2 in MapObject.get('complete', []):
			if self.complete == None:
				self.complete = []
			ctx = Transaction()
			ctx.read(item2)
			self.complete.append(ctx)

class WalletTransactionResponse(Response):
	def __init__(self,
		status=None,
		data=None,
		message=None,
		):
		super().__init__()
		self.status  = status
		self.data    = data
		self.message = message
	def read(self, MapObject):
		self.status  = MapObject.get('status', None)
		for item1 in MapObject.get('data', []):
			if self.data == None:
				self.data = []
			ctx = Wallet()
			ctx.read(item1)
			self.data.append(ctx)
		self.message = MapObject.get('message', None)