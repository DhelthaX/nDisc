import os
import sys
import platform
import ipaddress

networkRange = ipaddress.IPv4Network('192.168.1.0/24')#sys.argv[1])

if not networkRange:
	print("Usage: 'IP'/'CIDR Sub-Maskn'\n e.g.: \"nDisc.py 192.168.0.0/16\"")
	sys.exit()

def ping():
	param = '-n' if platform.system().lower()=='windows' else '-c'
	param2 = '-w' if platform.system().lower()=='windows' else '-t'

	for ip in networkRange:
		resp = os.popen(f"ping {ip} {param} 1 {param2} 1").read()
		if not "0 packets received" in resp:
			print(f"[+] The {ip} is UP - Ping Successful")
	return None

if __name__ == '__main__':
	ping()


