import OSC
import time, random
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
for i in range(600):
    msg = OSC.OSCMessage()
    msg.setAddress("/print")
    msg.append(i)
    client.send(msg)
    time.sleep(0.03)