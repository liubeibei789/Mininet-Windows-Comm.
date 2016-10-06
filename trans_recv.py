############## trans_recv.py ###################
# edited by Beibei LIU, Otc,2016
# introduction:
# windows1(power): ip='10.144.154.181',port=2222
# receive: listen to the port 2222, waiting for connection from mininet1(mininet1.py),
#          storing the received message into bbb.txt
# transmit: send the received message to mininet1(mininet1.py)

# command(typed in windows command window): 
# cd workspace (the folder containing this file)
# python trans_recv.py 

#!/usr/bin/python

import socket
import threading
import time

def receive(ip,port):  # '10.144.154.181', 2222
	i = 1
	while True:
		print "hello I am server on windows1..."
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((ip,port))
		sock.listen(5)
		connection,address = sock.accept()
		fileName = "bbb" + "_" + str(i) + ".txt"
		fo = open( fileName,"w" )
		try:
			connection.settimeout(5)
			buf = connection.recv(1024)
			print "windows1 receives message:",buf
			connection.send('feedback: windows1 has received the message!')
		except socket.timeout:
			print 'time out'
		try:
			fo.write(buf)
		finally:
			fo.close()
		connection.close()
		i = i+1
	
def transmit(ip,port):  # '10.206.201.201', 4444
	i = 1
	while True:
		while True:
			try:
				fileName2 = "bbb" + "_" + str(i) + ".txt"
				fd = open( fileName2,"r" )
				print "file found!"
				break
			except:
				time.sleep(3)
				print "wait..."
		sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock2.connect((ip,port))
		buf2 = fd.read()
		print "windows1 is going to send:",buf2
		sock2.send(buf2)
		print sock2.recv(1024) # receive the message from the server
		sock2.close()
		i = i+1
			
threads = []
t1 = threading.Thread( target = receive, args=('10.144.154.181', 2222))
threads.append(t1)
t2 = threading.Thread( target = transmit, args=('10.206.201.201', 4444))
threads.append(t2)

if __name__ == '__main__':
	for t in threads:
		t.start()