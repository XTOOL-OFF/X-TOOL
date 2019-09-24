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
		os.system("pip install SimpleQIWI")
		os.system("git clone https://github.com/TheSpeedX/TBomb.git")
		os.system("cd TBomb/ && chmod +x *")
		os.system("git clone https://github.com/byt3bl33d3r/MITMf.git")
		os.system("apt-get install python-dev python-setuptools libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone3 libcapstone-dev libffi-dev file")
		os.system("cd MITMf && git submodule init && git submodule update --recursive")
		os.system("cd MITMf && pip install -r requirements.txt")
		os.system("echo 'alias xtool=\"cd ~ && cd X-TOOL && python3 X-TOOL.py\"' >> ~/.bashrc")
		print("You can start X-TOOL if you execute command xtool")

	
