import requests
import json
import socket
import time

while(True):
	Cond = int(input('\nDo You Want To Continue\nPress 1 For Yes\nPress 2 For No: '))
	
	if (Cond == 1):
		host = input('\nPlease Enter The Host Name: ')
		Mainip = socket.gethostbyname(host)
		print('Locating Server.....')
		time.sleep(5)
		res = requests.get("https://api.iplegit.com/full?", params={
    'ip': Mainip
}).json()

		print(json.dumps(res,sort_keys=True,indent=4))
		
	else:
		break



