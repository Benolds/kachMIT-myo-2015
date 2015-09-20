from myo_data_reading import MyoData

def test_myo_data():
	#reading_left = MyoData('left', -0.031738, 0.423828, -0.031738, -0.180725, -0.188599, -0.754822, -0.601746)
	#reading_right = MyoData('right', -0.269043, -0.907715, -0.269043, 0.169739, 0.585815, -0.792480, 0.004700)

	l1 = MyoData('left', 0.983398, -0.009766, 0.983398, -1.549808, -1.473438, -0.130706)
	l2 = MyoData('left', 0.982910, -0.042969, 0.982910, -1.521798, -1.461458, -0.124401)
	l3 = MyoData('left', 0.987793, -0.006348, 0.987793, -1.486177, -1.376552, -0.115690)

	r1 = MyoData('right', 0.911621, -0.106934, 0.911621, -1.573113, 1.303148, 0.053537)
	r2 = MyoData('right', 0.956055, -0.080566, 0.956055, -1.642836, 1.317662, 0.069826)
	r3 = MyoData('right', 0.964844, -0.061035, 0.964844, -1.662665, 1.335806, 0.080696)

	print(l1.toString())
	print(l1.process_reading())

	print(r1.toString())
	print(r1.process_reading())

test_myo_data()