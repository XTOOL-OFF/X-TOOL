from SimpleQIWI import *
print('Q I W I Software by XERSIX');
token=input('Enter token: ')
money=input("Enter, how many money to transfer:");
inputphone=input('Enter target  phone: ');
outputphone=input("Enter your phone:");
comment=input("Enter comment to transfer!:");
api = QApi(token=token, phone=inputphone)
print('Balance Founded')
print(api.balance)
api.pay(account=(outputphone), amount=(money), comment=comment)
print(api.balance)
input()

