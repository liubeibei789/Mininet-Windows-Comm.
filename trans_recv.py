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

import config

import socket
import threading
import time

global FLAG
FLAG = 0

def receive(ip,port):  
	global FLAG
	i = 1
	while FLAG == 0:
		print "hello I am server on windows1..."
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((ip,port))
		sock.listen(5)
		connection,address = sock.accept()
		fileName = config.cfp['file_recv'] + '_' + str(i) + '.txt'
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
		
	
def transmit(ip,port):  
	global FLAG
	i = 1
	while FLAG == 0:
		while FLAG == 0:
			try:
				fileName2 = config.cfp['file_trans'] + '_' + str(i) + '.txt'
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
		
def exit():
	global FLAG
	while FLAG == 0:
		try:
			instruction = raw_input()
			if instruction == 'exit':
				print "server closed"
				FLAG = 1
			else:
				print "to close the server,type: exit"
		except:
			pass
		finally:
			pass
			

def do():
	threads = []
	t1 = threading.Thread( target = receive, args=(config.cfp['ip_windows'], config.cfp['port_windows']))
	threads.append(t1)
	t2 = threading.Thread( target = transmit, args=(config.cfp['ip_mininiet'], config.cfp['port_mininet']))
	threads.append(t2)
	t3 = threading.Thread( target = exit, args=())
	threads.append(t3)
	
	for t in threads:
		t.start()


if __name__ == '__main__':
	a = do()
