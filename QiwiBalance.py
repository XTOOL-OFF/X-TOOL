from SimpleQIWI import *
print('Q I W I Software by XERSIX');
token=input('Enter token: ');
phone=input('Enter phone: ');
api = QApi(token=token, phone=phone)
print('Balance Founded')
print(api.balance)
input()
