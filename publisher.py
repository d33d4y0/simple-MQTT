#! /usr/bin/env python3
from socket import *
import sys
import optparse
import json

def arguments():
	parser = optparse.OptionParser()
	parser.add_option("-b", "--broker", dest="broker_ip", help="ip of broker for publishing")
	parser.add_option("-t", "--topic", dest="topic", help="topic for publishing")
	parser.add_option("-d", "--data", dest="data", help="data for publishing")
	(options, argument) = parser.parse_args()
	if not options.broker_ip:
		parser.error("[-] Please specify an broker ip, use --help for more info.")
	elif not options.topic:
		parser.error("[-] Please specify an topic, use --help for more info.")
	elif not options.data:
		parser.error("[-] Please specify an data, use --help for more info.")
	return options

MAX_BUF = 2048
SERV_PORT = 50000

options = arguments()

serv_sock_addr = (options.broker_ip, SERV_PORT)     # Server socket address 
cli_sock = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket


publish_ip = gethostbyname(gethostname())
txtout = json.dumps({"host": publish_ip, "type":"publish", "broker_ip" : options.broker_ip, "topic" : options.topic, "data" : options.data})


cli_sock.sendto(txtout.encode('utf-8'), serv_sock_addr) # Convert to byte type and send

cli_sock.close()