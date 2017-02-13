############## comm_win_power.py ###################
# edited by Beibei LIU, Oct,2016

# --------------- introductions ------------
# windows1(power): ip='10.144.154.181',port=2222
# receive(): 
#		 listen to the port 2222, waiting for connection from mininet1(mininet1.py),
#        storing the received message into 'powerInFile.txt',
#        which is the input file of power system simulation
# transmit(): 
#        send the output file of power system simulation 'powerOutFile.txt' to mininet1(mininet1.py)
# exit():
#        type 'exit' in the console input to terminate the program

# -------------- run -------------------
# command(typed in windows command window): 
# cd workspace (the folder containing this file)
# python comm_win_power.py

# !/usr/bin/python

import config
import socket
import threading
import time

import ctrl_win_power


class CommWinPower():

    exitFLAG = 0

    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 2222

    def receive(self, ip, port):
        testObj = ctrl_win_power.CtrlWinPower()
        i = 0
        while self.exitFLAG == 0:
            print "hello I am server on windows1..."
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(5)
            connection, address = sock.accept()
            fileName = config.cfp['file_recv'] + '_' + str(i) + '.txt'
            fo = open(fileName, "w")
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                print "windows1 receives message:", buf
                connection.send('feedback: windows1 has received the message!')
                testObj.commander()
            except socket.timeout:
                print 'time out'
            try:
                fo.write(buf)
            finally:
                fo.close()
            connection.close()
            i += 1

    def transmit(self, ip, port):
        i = 0
        while self.exitFLAG == 0:
            while self.exitFLAG == 0:
                try:
                    fileName2 = config.cfp['file_trans'] + '_' + str(i) + '.txt'
                    #1= OS.PATH.ISFILE("BB")
                    fd = open(fileName2, "r")
                    print "file found!"
                    break
                except:
                    print "wait..."
                    time.sleep(3)

            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sock2.connect((self.ip, self.port))
            sock2.connect(('10.206.201.201', 4444))
            buf2 = fd.read()
            print "windows1 is going to send:", buf2
            sock2.send(buf2)
            print sock2.recv(1024)  # receive the message from the server
            sock2.close()
            i += 1

    def exit(self):
        while self.exitFLAG == 0:
            try:
                instruction = raw_input()
                if instruction == 'exit':
                    print "server closed"
                    exitFLAG = 1
                else:
                    print "to close the server,type: exit"
            except:
                pass
            finally:
                pass

def do():
    inst = CommWinPower()
    threads = []
    t1 = threading.Thread(target=inst.receive, args=(config.cfp['ip_windows1'], config.cfp['port_windows1']))
    threads.append(t1)
    t2 = threading.Thread(target=inst.transmit, args=(config.cfp['ip_mininiet1'], config.cfp['port_mininet1']))
    threads.append(t2)
    t3 = threading.Thread(target=inst.exit, args=())
    threads.append(t3)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print 'windows1 finished'

if __name__ == '__main__':
    do()
