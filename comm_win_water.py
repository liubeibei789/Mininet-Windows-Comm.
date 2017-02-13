############## comm_win_water.py ###################
# edited by Beibei LIU, Oct,2016

# --------------- introductions ------------

# windows2(water): ip='10.144.154.181',port=3333
# receive(): 
#		  listen to the port 3333, waiting for connection from mininet2(mininet2.py),
#         storing the received message into waterInFile.txt
# transmit(): 
#       send the output file of water system simulation 'waterOutFile.txt' to mininet2(mininet2.py)
# exit():
#		type 'exit' in the console input to terminate the program

# -------------- run -------------------
# command(typed in windows command window): 
# cd workspace (the folder containing this file)
# python comm_win_water.py 


# !/usr/bin/python

import config
import socket
import threading
import time

import ctrl_win_water


class CommWinWater():

    exitFLAG = 0

    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 2222

    def receive(self, ip, port):
        testObj = ctrl_win_water.CtrlWinWater()
        i = 0
        while self.exitFLAG == 0:
            print "hello I am server on windows2..."
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(5)
            connection, address = sock.accept()
            fileRecv = config.cfw['file_recv'] + '_' + str(i) + '.txt'
            fo = open(fileRecv, "w")
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                print "windows2 receives message:", buf
                connection.send('feedback: windows2 has received the message!')
                testObj.commander(i)
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
                    fileTransmit = 'waterOutFile' + '_' + str(i) + '.txt'
                    #fileTransmit = config.cfw['file_trans'] + '_' + str(i) + '.txt'
                    # 1= OS.PATH.ISFILE("BB")
                    fd = open(fileTransmit, "r")
                    print "file found!"
                    break
                except:
                    time.sleep(3)
                    print "wait..."
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock2.connect((self.ip, self.port))
            buf2 = fd.read()
            print "windows2 is going to send:", buf2
            sock2.send(buf2)
            print sock2.recv(1024)  # receive the message from the mininet2 server
            sock2.close()
            i += 1

    def exit(self):
        while self.exitFLAG == 0:
            try:
                instruction = raw_input()
                if instruction == 'exit':
                    print "server closed"
                    self.exitFLAG = 1
                else:
                    print "to close the server,type: exit"
            except:
                pass
            finally:
                pass


def do():
    inst = CommWinWater()
    threads = []
    t1 = threading.Thread(target=inst.receive, args=(config.cfw['ip_windows'], config.cfw['port_windows']))
    threads.append(t1)
    t2 = threading.Thread(target=inst.transmit, args=(config.cfw['ip_mininiet'], config.cfw['port_mininet']))
    threads.append(t2)
    t3 = threading.Thread(target=inst.exit, args=())
    threads.append(t3)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print 'windows2 finished'


if __name__ == '__main__':
    do()
