class MyoData:
    def __init__(self, arm, acc_x, acc_y, acc_z, roll, pitch, yaw): #ori_x, ori_y, ori_z, ori_w):
    	
    	self.arm = arm # 'left' or 'right'

        # acceleration values
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z

        # orientation values
        # self.ori_x = ori_x
        # self.ori_y = ori_y
        # self.ori_z = ori_z
        # self.ori_w = ori_w

        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def toString(self):
    	return self.arm + " %f %f %f %f %f %f" % (self.acc_x, self.acc_y, self.acc_z, self.roll, self.pitch, self.yaw) #self.ori_x, self.ori_y, self.ori_z, self.ori_w)
    	#return self.acc_x + " " + self.acc_y + " " + self.acc_z + " " + self.ori_x + " " + self.ori_y + " " + self.ori_z + " " + self.ori_w

    def process_reading(self):

        # Freq: 60 - 1000 Hz;
        # LPF Cutoff: 40 - 20000 Hz;
        # Envelope Freq: 2.33333 - 18.666666 Hz

    	print("processing " + self.arm + " arm data")
    	if self.arm == 'right':
    		# rotation -> envelope frequency

    		pass
    	else:
    		# rotation -> low pass filter cutoff frequency
    		pass