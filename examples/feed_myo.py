# Copyright (c) 2015  Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function
import myo as libmyo; libmyo.init()
import time
import uuid
from myo_data_queue import MyoDataQueue
from myo_data_reading import MyoData
# from OSC import OSCClient, OSCMessage

import OSC
import time, random


def main():
    #print('starting')
    #unique_filename = uuid.uuid4()
    #print(unique_filename)
    unique_filename = raw_input("Give a unique name for the file: ") + "_myo.txt"
    # if len(unique_filename) == 0:
    #     unique_filename = str(uuid.uuid4())
    target = open(unique_filename, 'a')

    feed = libmyo.device_listener.Feed()
    hub = libmyo.Hub()
    hub.run(1000, feed)

    ip_address = '127.0.0.1' #'10.101.3.134' #'10.101.5.216' #'10.102.0.1'
    client = OSC.OSCClient()
    client.connect( ( ip_address, 57120 ) )

    # for m in myos:
    #     print(m)

    # return

    try:
        print("Waiting for a Myo to connect ...")
        # myo = feed.wait_for_single_device(2)
        # if not myo:
        time.sleep(1)
        myos_unsorted = feed.get_connected_devices()
        myos = []
        if len(myos) == 0:
            print("No Myo connected after 1 second.")
            return

        print("Hello, Myo!")
        print("Found " + str(len(myos)) + " myos")
        for myo in myos_unsorted:
            print("Found myo for " + str(myo.arm) + " arm")
            if myo.arm == 'right': # right
                print("Right arm")
                myos.append(myo)
        for myo in myos_unsorted:
            print("Found myo for " + str(myo.arm) + " arm")
            if myo.arm == 'left': # right
                print("Right arm")
                myos.append(myo)
        
            # elif myo.arm == 'left': #left
            #     print("Left arm")

        q = MyoDataQueue()

        # client = OSCClient()
        # client.connect( ("localhost", 7110) )

        while hub.running and any(myo.connected for myo in myos): #myo.connected:
            #print(myo.orientation)
            # dataline = ""
            # for o in [myo.orientation.x, myo.orientation.y, myo.orientation.z, myo.orientation.w]:
            #     dataline += str(o) + " "
            # print(myo.acceleration)
            # # dataline = str(myo.orientation.x) + " " + str(myo.orientation.y) 
            # # target.write(str(myo.orientation.x))
            # dataline += "\n"
            # target.write(dataline)

            msg = OSC.OSCMessage()
            msg.setAddress("/print")

            msg_data = []

            for myo in myos:
                arm_string = 'right' if myo.arm == 'right' else 'left'
                d = MyoData(arm_string, myo.acceleration.x, myo.acceleration.y, myo.acceleration.z, myo.orientation.roll, myo.orientation.pitch, myo.orientation.yaw) #myo.orientation.x, myo.orientation.y, myo.orientation.z, myo.orientation.w)
                q.push(d)

                new_d = q.get()
                # print(new_d.toString())

                if arm_string == 'right':
                    right_roll = max(2, min(10, abs(int(10 * myo.orientation.pitch / 3.14))))
                    print("right: " + str(right_roll))
                    #msg.append(right_roll) #new_d.toString())
                    msg_data.append(right_roll)
                    # msg_data.append(right_roll)
                    # if myo.pose == 'fist':
                    #     msg.append(0.0)
                    # else:
                    #     msg.append(1.0)
                else:
                    left_roll = max(200, min(10000, 60 + abs(int(15000 * myo.orientation.pitch / 3.14))))
                    print("left: " + str(left_roll))
                    #msg.append(left_roll) #new_d.toString())
                    msg_data.append(left_roll)
                    # msg_data.append(left_roll)

                # time.sleep(0.03)

                #sendData()

                target.write(new_d.toString() + "\n")


            msg.append(msg_data)
            client.send(msg)

            # client.send( OSCMessage("/user/1", [1.0, 2.0, 3.0 ] ) )

            time.sleep(0.03)
        print("Goodbye, Myo!")
    except KeyboardInterrupt:
        print("Keyboard Interrupt.")
    else:
        print("Myo disconnected.")
    finally:
        print("Shutting down Myo Hub ...")
        hub.shutdown()

if __name__ == "__main__":
    main()
