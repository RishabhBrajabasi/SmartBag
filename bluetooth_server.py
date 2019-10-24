'''
Bluetooth socket support

Copyright 2018  Gunnar Bowman, Emily Boyes, Trip Calihan, Simon D. Levy, Shepherd Sims

MIT License
'''

import os
import time
import bluetooth as bt

pathON = '/home/pi/ObjectsNeeded.txt'
pathOP = '/home/pi/ObjectsPresent.txt'
pathBL = '/home/pi/BatteryLevel.txt'


class BluetoothServer(object):
    '''
    Provides an abstract class for serving sockets over Bluetooth.  You call the constructor and the start()
    method.  You must implement the method handleMessage(self, message) to handle messages from the client.
    '''

    def __init__(self):
        '''
        Constructor
        '''

        # Arbitrary service UUID to advertise
        self.uuid = "7be1fcb3-5776-42fb-91fd-2ee7b5bbb86d"

        self.client_sock = None

    def start(self):
        '''
        Serves a socket on the default port, listening for clients.  Upon client connection, runs a loop to 
        that receives period-delimited messages from the client and calls the sub-class's 
        handleMessage(self, message) method.   Sub-class can call send(self, message) to send a 
        message back to the client.   Begins listening again after client disconnects.
        '''

        # Make device visible
        os.system("hciconfig hci0 piscan")

        # Create a new server socket using RFCOMM protocol
        server_sock = bt.BluetoothSocket(bt.RFCOMM)

        # Bind to any port
        server_sock.bind(("", bt.PORT_ANY))#
        #server_sock.find(("", 1))#

        # Start listening
        server_sock.listen(1)

        # Get the port the server socket is listening
        port = server_sock.getsockname()[1]

        # Start advertising the service
        bt.advertise_service(server_sock, "RaspiBtSrv",
                           service_id=self.uuid,
                           service_classes=[self.uuid, bt.SERIAL_PORT_CLASS],
                           profiles=[bt.SERIAL_PORT_PROFILE])


        # Outer loop: listen for connections from client
        while True:
            print("Waiting for connection on RFCOMM channel %d" % port)
            try:
                # This will block until we get a new connection
                self.client_sock, client_info = server_sock.accept()
                print("Accepted connection from " +  str(client_info))

                # Track strings delimited by '.'
                s = ''
                try:
                    on = open(pathON, 'r')
                    neededContents = on.read()
                    nC = neededContents.split('|')[:-1]
	                
                    op = open(pathOP, 'r')
                    presentContents = op.read()
                    pC = presentContents.split('|')[:-1]
                        
                    bl = open(pathBL, 'r')
                    bp = bl.read()    # bp - battery percentage
                        
                    print("Sending List of Objects missing")
                    for need in nC:
                        if need not in pC:
                            print(need)
                            self.send("OM:"+need)
                    		    
                    print("Sending List of Objects present ")
                    for present in pC:
                        print(present)
                        self.send("OP:"+present)
                        
                    print("Sending battery level of Pi")
                    print(bp)
                    self.send("BL:"+bp)
               
                except IOError:
                    print("Trouble reading file. Trying again after 5 seconds")
                time.sleep(5)
        	#while True:
                    #self.send("Object Missing");
                    #self.send("U|0|1")
                    #c = self.client_sock.recv(1).decode('utf-8')
                    #if c == '.' and len(s) > 0:
                    #    self.handleMessage(s)
                        #self.send(s)
                        #print(s)
                        # self.handleMessage(s)
                    #    s = ''
                    #else:
                    #    s += c

            except IOError:
                pass

            except KeyboardInterrupt:

                if self.client_sock is not None:
                    self.client_sock.close()
                
                server_sock.close()

                print("Server going down")
                break

    def send(self, message):
        '''
        Appends a period to your message and sends the message back to the client.
        '''
        
        self.client_sock.send((message+'.').encode('utf-8'))
