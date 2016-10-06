############## mininet1.py ###################
# edited by Beibei LIU, Otc,2016
# introduction:
# mininet1(connected to windows1): ip='10.206.201.201'(external ip addr),port=4444
# receive: listen to the port 4444, waiting for connection from windows1(trans_recv.py),
#          storing the received message into mininetRcv1.txt
# transmit: do not send the received file 'mininetRcv1.txt',which will be picked up by host1(host1.py)
#           instead, check if there exists a file 'h1rcv.txt', send to windows1(trans_recv.py)

# command(typed in mininet terminal;from unbuntu terminal:ssh -Y mininet@'ip of mininet'): 
# cd (or the folder containing this file)
# python mininet1.py 

import socket
import select
import time
import threading

def receive(ip,port): # '10.206.201.201',4444
        i = 1
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock3.bind((ip,port))
        sock3.listen(5)
        while True:
            connection,address = sock3.accept()
            print "accept succeed"
            fileName = "mininetRcv1" + "_" + str(i) + ".txt"
            fo = open( fileName,"w" )
            try:
                        connection.settimeout(5)
                        buf = connection.recv(1024)
                        print "mininet1 receives:",buf
                        connection.send('feedback: Mininet1 has received the message!')
            except socket.timeout:
                        print 'time out'

            try:
                        fo.write(buf)
            finally:
                        fo.close()
            connection.close()
            i = i+1

def transmit(ip,port): # '10.144.154.181',2222
        i = 1
        while True:
                while True:
                        try:
                                fileName2 = "h1rcv" + "_" + str(i) + ".txt"
                                fd = open( fileName2,"r" )
                                break
                        except:
                                time.sleep(3)
                                print "checking file.."
                print "file found"
                all_the_text = fd.read()
                print "content of the file found is:",all_the_text

                sock2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock2.connect((ip,port))
                sock2.send(all_the_text)
                print "mininet1 sends to windows1:",all_the_text
                print sock2.recv(1024)
                sock2.close()
                i = i+1

threads = []
t1 = threading.Thread( target = receive, args=('10.206.201.201',4444))
threads.append(t1)
t2 = threading.Thread( target = transmit, args=('10.144.154.181',2222))
threads.append(t2)

if __name__ == '__main__':
        for t in threads:
            t.start()



