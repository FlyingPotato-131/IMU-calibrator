import mpu9250
import numpy as np

Npoints = 10000
Navg = 100

def calibrateMag(mpu9250, axis, refdata):
	with open(f"mag-curve-{axis}.csv", w) as data:
		for point in range(Npoints):
			S = 0
			for msr in range(Navg):
                mpu9250.readMagnet()
                S += mpu9250.Mag[axis]
            data.write(refdata[point] + ',' + S / Navg + '\n')

def calibrateAcc(mpu9250, axis, refdata):
	with open(f"acc-curve-{axis}.csv", w) as data:
		for point in range(Npoints):
			S = 0
			for msr in range(Navg):
                mpu9250.readAccel()
                S += mpu9250.Accel[axis]
            data.write(refdata[point] + ',' + S / Navg + '\n')

def calibrateAng(mpu9250, axis, refdata):
	with open(f"ang-curve-{axis}.csv", w) as data:
		for point in range(Npoints):
			S = 0
			for msr in range(Navg):
                mpu9250.readGyro()
                S += mpu9250.Gyro[axis]
            data.write(refdata[point] + ',' + S / Navg + '\n')

def binsearch(value, array):
	if(value < array[0]):
		return 0
	if(value > array[-1]):
		return len(array)

	step = len(array) // 2
	it = step
	while(array[it] >= value || array[it+1] <= value):
		if(array[it] > value):
			it -= step
		else:
			it += step
		step = step // 2
	return it

def lerp(start, end, t):
	return start + t / (end - start)

def inverselerp(start, end, s):
	return (s - start) / (end - start)

refData = np.empty(Npoints, 12)

def loadRefData():
	for axis in range(3):
		magData = open(f"mag-curve-{axis}.csv")
		refData[:, 0] = magData[:, 0]
		refData[:, 1 + axis] = magData[:, 1]

		accData = open(f"acc-curve-{axis}.csv")
		refData[:, 4] = accData[:, 0]
		refData[:, 5 + axis] = accData[:, 1]

		angData = open(f"ang-curve-{axis}.csv")
		refData[:, 8] = accData[:, 0]
		refData[:, 9 + axis] = accData[:, 1]

def decodeMag(mpu9250, axis):
	it = binsearch(refData[:, 1+axis], mpu9250.Mag[axis])
	return lerp(refData[it, 0], refData[it+1, 0], inverselerp(refData[it, 1+axis], refData[it+1, 1+axis], mpu9250.Mag[axis]))

def decodeAcc(mpu9250, axis):
	it = binsearch(refData[:, 5+axis], mpu9250.Accel[axis])
	return lerp(refData[it, 4], refData[it+1, 4], inverselerp(refData[it, 5+axis], refData[it+1, 5+axis], mpu9250.Accel[axis]))

def decodeAng(mpu9250, axis):
	it = binsearch(refData[:, 9+axis], mpu9250.Gyro[axis])
	return lerp(refData[it, 8], refData[it+1, 8], inverselerp(refData[it, 9+axis], refData[it+1, 9+axis], mpu9250.Gyro[axis]))
