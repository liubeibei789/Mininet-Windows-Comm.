############## host2.py ###################
# edited by Beibei LIU, Otc,2016
# introduction:
# host2(connected to mininet2): ip='10.0.0.2'(internal ip addr),port=6666
# receive: listen to the port 6666, waiting for connection from host1(host1.py),
#          storing the received message into h2rcv.txt
# transmit: do not send the received message('h2rcv.txt'),which is supposed to be picked up by mininet2(mininet2.py)
#           instead, check if there exists a file 'mininetRcv2.txt', send to host1(host1.py)

# command(typed in host2 terminal;from mininet:sudo mn --topo...xterm h2): 
# cd (or the folder containing this file)
# sudo python host2.py 


import socket
import select
import time
import threading

def receive(ip,port):  # '10.0.0.2',6666
        i = 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip,port))
        sock.listen(5)
        while True:
                connection,address = sock.accept()
                print "accept succeed"
                fileName = "h2rcv"+ "_" + str(i) + ".txt"
                fo = open( fileName,"w" )
                try:
                        connection.settimeout(5)
                        buf = connection.recv(1024)
                        print "h2 receives:", buf
                        connection.send('feedback: h2 has received the message!')
                except socket.timeout:
                        print 'time out'
                try:
                        fo.write(buf)
                finally:
                        fo.close()
                connection.close()
                i = i+1

def transmit(ip,port): # '10.0.0.1',6666
        i = 1
        while True:
                while True:
                        try:
                                fileName2 = "mininetRcv2" + "_" + str(i) + ".txt"
                                fd = open( fileName2,"r" )
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
                print "The message h2 sends to h1 is:",all_the_text
                print sock2.recv(1024)
                sock2.close()
                i = i+1


threads = []
t1 = threading.Thread( target = receive, args=('10.0.0.2',6666))
threads.append(t1)
t2 = threading.Thread( target = transmit, args=('10.0.0.1',6666))
threads.append(t2)

if __name__ == '__main__':
        for t in threads:
            t.start()



