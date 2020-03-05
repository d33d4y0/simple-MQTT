#! /usr/bin/env python3

from socket import * 
import sys
import json

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

serv_sock_addr = ('127.0.0.1', SERV_PORT)          # Socket address
serv_sock = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
serv_sock.bind(serv_sock_addr)                    # Bind socket to address

print ('Broker server started ...')

topic = dict()
subscriber = [[] for i in range(100)]
index = 0

while(1):
	txtin,cli_sock_addr = serv_sock.recvfrom(MAX_BUF)  # txtin stores receive text
	data = json.loads(txtin.decode('utf-8'))
	if data["type"] == 'publish':
		print('Publisher> ', end = '')
		print('%s' %(data))
		if data["topic"] in topic:
			txtout = json.dumps(data)
			for addr in subscriber[topic[data["topic"]]]:
				serv_sock.sendto(txtout.encode('utf-8'), addr)
	elif data["type"] == 'subscribe':
		print('Subscriber> ', end = '')
		print('%s' %(data))
		if data["topic"] not in topic:
			topic[data["topic"]] = index
			subscriber[topic[data["topic"]]].append(cli_sock_addr)
			index+=1
		elif data["topic"] in topic:
			subscriber[topic[data["topic"]]].append(cli_sock_addr)
			
serv_sock.close()