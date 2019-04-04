# ovopy
[![BuildStatus](https://travis-ci.org/anysz/ovopy.svg?branch=master)](https://travis-ci.org/anysz/ovopy)
[![Version 1.0.0](https://img.shields.io/badge/stable-1.0.0-brightgreen.svg "Version 1.0.0")](https://github.com/anysz/ovopy)
[![Supported python versions: 3.6](https://img.shields.io/badge/python-3.6-green.svg "Supported python versions: 3.6")](https://www.python.org/download/releases/3.6/)
[![License](https://img.shields.io/github/license/anysz/ovopy.svg)](https://github.com/anysz/ovopy/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e8dfd96812194ac393d40ec5ef478a54)](https://www.codacy.com/app/anysz/ovopy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=anysz/ovopy&amp;utm_campaign=Badge_Grade)
[![Donate](https://img.shields.io/badge/donate-patreon-orange.svg)](https://www.patreon.com/anysz)

*Un-official OVOid Python3 Client*

Bahasa: [English](README.md) [Indonesia](README.id.md)

---
## Instal
`python3 setup.py install`

## Status Fungsi
| Fungsi                  	| Status               	|
|-------------------------	|----------------------	|
| `login2FA`              	| OK                   	|
| `verifyLogin2FA`        	| OK                   	|
| `loginSecurityCode`     	| OK                   	|
| `getBudget`             	| OK                   	|
| `getFrontModel`         	| OK                   	|
| `generateTrxId`         	| OK                   	|
| `transferOvoBalance`    	| Error: Invalid Model 	|
| `logout`                	| OK                   	|
| `getUnreadNotification` 	| OK                   	|
| `getWalletTransaction`  	| OK                   	|

Telah dites pada OVO v2.8.0 | 27/03/2019 | Python 3.6

## Contoh Penggunaan

![](fig1.jpg)

### Login
Untuk contoh penggunaan bisa cek di file `test.py`.  

PERHATIAN: Setelah masuk pertama kali, pastikan token yang didapat tersimpan, karena OVO membatasi akun tiap deviceId
```python
import ovopy
# By default, settings saved to local .json file, so when you attempted to login with phone number (again) it'll use token that saved on local .json file resolved by phone number. You can disable this feature by adding `save_auth=False` at OVO class argument.
# ovo = ovopy.OVO(save_auth=False)

ovo = ovopy.OVO()
# with phone_number
l2fa  = ovo.login('<phone_number>')
vl2fa = ovo.verifyLogin2FA(l2fa.refId, '<SMS Pincode>', '<phone_number>')
lsc   = ovo.loginSecurityCode('<6digit of security code>', vl2fa.updateAccessToken)

# with token
lwt  = ovo.login(token='<token here JWT>')

# Test now! :D
print(ovo.getFrontModel())
```

### Informasi Akun
Mendapatkan informasi tentang akun
```python
r = ovo.getFrontModel()
print(r) # resp: FrontResponse(...)
```

### Detail Budget
Mendapatkan informasi seputar budget
```python
r = ovo.getBudget()
print(r) # resp: BudgetResponse(budget=History(amount=0, categoryId=None, spending=0), totalSpending=0, cycleDate=1, summary=[...])
```

### Histori Transaksi
Mendapatkan daftar histori transaksi
```python
r = ovo.getWalletTransaction(page=1, limit=1)
print(r) # resp: WalletTransactionResponse(...)
```

### Transfer Saldo
Untuk sementara, hanya bisa melakukan transfer dua kali, untuk yang ketiga membutuhkan header signature. Bila anda menemukan implementasi signature bisa membuat request pull, Terima kasih.
```python
rtrx = ovo.transferOvoBalance('<to_phone_number>', 10000, None)
print(rtrx) # resp: CustomerTransferResponse(...)
```

### Notifikasi
```python
# Get all notifications
rx = ovo.getAllNotification()
print(rx) # resp: NotificationAllRespone(notifications=[...])

# Get total unread notification
r = ovo.getUnreadNotification()
print(r)  # resp: NotificationUnreadResponse(Total=0)
```

### Logout
Logout dari client
```python
r = ovo.logout()
print(r) # resp: LogoutResponse(httpStatus=200)
```

## Error
### OVOUnexpectedError
Sebuah error terjadi karena respon kode http bukan 200, Kebanyakkan terjadi karena invalid client payload

## Bahasa Program Lainnya
Cek juga Un-official OVO\[id] client yang lainnya!

| Repositori                                                   	| Bahasa   	|
|--------------------------------------------------------------	|----------	|
| [@lintangtimur/ovoid](https://github.com/lintangtimur/ovoid) 	| PHP      	|
| [@anysz/ovopy](https://github.com/anysz/ovopy)               	| Python   	|

## Author
Anysz / [@Anysz](https://github.com/anysz)
