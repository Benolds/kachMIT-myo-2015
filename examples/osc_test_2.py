import OSC
import time, random
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
a = [98, 104, 110, 117, 123, 131, 139, 147, 156, 165, 176, 196]
while 1:
	for i in a:
	    msg = OSC.OSCMessage()
	    msg.setAddress("/print")
	    msg.append([i,i,i])
	    client.send(msg)
	    time.sleep(0.1)