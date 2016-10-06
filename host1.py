############## host1.py ###################
# edited by Beibei LIU, Otc,2016
# introduction:
# host1(connected to mininet1): ip='10.0.0.1'(internal ip addr),port=6666
# receive: listen to the port 6666, waiting for connection from host2(host2.py),
#          storing the received message into 'h1rcv.txt'
# transmit: do not send the received message('h1rcv.txt'),which is supposed to be picked up by mininet1(mininet1.py)
#           instead, check if there exists a file 'mininetRcv1.txt', send to host2(mmm.py)

# command(typed in host1 terminal;from mininet:sudo mn --topo...xterm h1): 
# cd (or the folder containing this file)
# sudo python host1.py 

import socket
import select
import time
import threading
import string

def receive(ip,port): # '10.0.0.1',6666
        i = 1
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock3.bind((ip,port))
        sock3.listen(5)
        while True:
                connection,address = sock3.accept()
                print "accept succeed"
                fileName2 = "h1rcv" + "_" + str(i) + ".txt"
                fo = open( fileName2,"w" )
                try:
                        connection.settimeout(5)
                        buf = connection.recv(1024)
                        print "h1 receives:", buf
                        connection.send('feedback: h1 has received the message!')
                except socket.timeout:
                        print 'time out'
                try:
                        fo.write(buf)
                finally:
                        fo.close()
                connection.close()
                i = i+1

def transmit(ip,port): # '10.0.0.2',6666
        i = 1
        while True:
                while True:
                        try:
                                fileName = "mininetRcv1" + "_" + str(i) + ".txt"
                                fd = open( fileName,"r" )
                                break
                        except:
                                time.sleep(3)
                                print "checking file.."
                print "file found!"
                all_the_text = fd.read()
                print "content of the file found is:",all_the_text

                sock2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock2.connect((ip,port))
                sock2.send(all_the_text)
                print "The message h1 sends to h2 is:",all_the_text
                print sock2.recv(1024)
                sock2.close()
                i = i+1

threads = []
t1 = threading.Thread( target = receive, args=('10.0.0.1',6666))
threads.append(t1)
t2 = threading.Thread( target = transmit, args=('10.0.0.2',6666))
threads.append(t2)

if __name__ == '__main__':
        for t in threads:
                t.start()



