import mpu9250
import serialcom
import select
import sys
import time

# Create an instance of a polling object 
poll_obj = select.poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin,1)

mpu9250 = mpu9250.MPU9250()

try:
    rec = 0
    while(1):
        rec = sys.stdin.read(1)
        if(rec == 'r'):
            while(rec != 's'):
                mpu9250.readAccel()
                mpu9250.readGyro()
                mpu9250.readMagnet()

                serialcom.sendData(mpu9250.Mag, mpu9250.Accel, mpu9250.Gyro)
                if(poll_obj.poll(0)):
                    rec = sys.stdin.read(1)
                # time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()
