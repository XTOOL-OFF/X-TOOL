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
print("Setup will install this tools!:")
print('[*]Aircrack-ng')
print('[*]postgresql')
print("Another Tools (below) you must install yourself")
print("[*]Ngrok")
print("[*]Metasploit Framework")
print("[*]Wifite")
print("Responsibility for using this tool rests ONLY with you.")
query = input("[*] Enter ACCEPT if you are want use this for not ILLEGAL purposes!:")                                       
if query.startswith('ACCEPT'):
	print('[*]Aircrack-ng')
	print('[*]postgresql')
	print('[*]Wifite')
	Install1 = input('OK! Do you wanna install folowing repositories and X-TOOL (Y/n):').lower()
	if Install1.startswith("y"):
		os.system("apt install aircrack-ng")
		os.system("apt-get install postgresql")
		os.system("echo 'alias xtool=\"cd ~ && cd X-TOOL && python3 X-TOOL.py\"' >> ~/.bashrc")
		print("You can start X-TOOL if you execute command xtool")

	
