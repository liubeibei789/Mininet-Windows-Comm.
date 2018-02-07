# This is a testing program running on Power side

import config
import threading
import time
import comm_win_power

class CtrlWinPower(threading.Thread):

    stateFLAG = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.N_iter = 3         
        # self.Name = 'somebody'

    def soldier(self, N_iter):
        event = threading.Event()
		list = ['1', '1', '3']
        for i in range(N_iter):
            print "# %d: start..." %i
            self.stateFLAG = 0
            # ---- this is the entrance of your main function ----
            fileName = 'powerInFile' + '_' + str(i) + '.txt'
            fo = open(fileName, "r")
            print fo.read()
            time.sleep(3)
            fileName2 = 'powerOutFile' + '_' + str(i) + '.txt'
            fd = open(fileName2, "w")
            fd.write('power simulation results')
            # -----------------------------------------------------
            # print "* %d %s: done!" %i %self.Name
            print 'done!'
            self.stateFLAG = 1
		    print i, '\n', list
            event.wait()


    def commander(self):
        print 'file arrived'
        event = threading.Event()
        event.set()

    def communicator(self):
        comObj = comm_win_power.CommWinPower()
        j = 0
        while j < self.N_iter:
            if self.stateFLAG == 0:
                print 'stateFLAG= %d' %self.stateFLAG
                time.sleep(1)
            else:
                print 'stateFLAG= %d' %self.stateFLAG
                #comObj.transmit(config.cfp['ip_mininet1'], config.cfp['port_mininet1'])
                comObj.transmit('10.206.201.201', 4444)
                j += 1


def do():
    N_iter = 3
    testObj = CtrlWinPower()

    t1 = threading.Thread(target=testObj.soldier, args=(N_iter,))
    t2 = threading.Thread(target=testObj.communicator, args=())

    t1.start()
    t2.start()

if __name__ == '__main__':
    do()