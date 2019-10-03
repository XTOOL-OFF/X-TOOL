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
		os.system("apt-get install apache2")
		os.system("pip install SimpleQIWI")
		os.system("pkg install apache2")
		os.system("git clone https://github.com/TheSpeedX/TBomb.git")
		os.system("cd && cd X-TOOL && cd TBomb/ && chmod +x *")
#		os.system("git clone https://github.com/byt3bl33d3r/MITMf.git")
#		os.system("cd && cd X-TOOL && cd MITMf && git submodule init && git submodule update --recursive")
#		os.system("cd && cd X-TOOL && cd MITMf && pip install -r requirements.txt")
		os.system("git clone https://github.com/sophron/wifiphisher")
		os.system("cd && cd X-TOOL && cd wifiphisher && python setup.py install")
		os.system("apt-get install libssl-dev && apt-get install libnl-3-dev libnl-genl-3-dev && cd && git clone https://github.com/wifiphisher/roguehostapd && cd roguehostapd && python3 setup.py install")
		os.system("git clone https://github.com/thewhiteh4t/seeker.git")
		os.system("cd && cd X-TOOL && cd seeker && chmod 777 termux_install.sh && ./termux_install.sh")
		os.system("cd && cd X-TOOL && chmod +x *")
		os.system("cd && cd X-TOOL && pip3 install -r requirements.txt")
		os.system("cd seeker && chmod 777 install.sh && ./install.sh")
		os.system("echo 'alias xtoolru=\"cd ~ && cd X-TOOL && python3 X-TOOL_ru.py\"' >> ~/.bashrc")

		os.system("echo 'alias xtool=\"cd ~ && cd X-TOOL && python3 X-TOOL.py\"' >> ~/.bashrc")
		os.system("cd && cd X-TOOL && git clone https://github.com/DarkSecDevelopers/HiddenEye.git")
		os.system("cd && cd X-TOOL && chmod 777 * && cd HiddenEye && pip3 install -r requirements.txt")
		print("RESTART YOUR TERMINAL!")
		print("You can start X-TOOL if you execute command xtool or xtoolru, if you want to use X-Tool on Russian Langauge")

	
