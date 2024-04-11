import mpu9250

mpu9250 = mpu9250.MPU9250()

try:
    while True:
        mpu9250.readAccel()
        mpu9250.readGyro()
        mpu9250.readMagnet()

        print('\r\nAcceleration:  X = %d , Y = %d , Z = %d\r\n'%(mpu9250.Accel[0], mpu9250.Accel[1], mpu9250.Accel[2]))  
        print('\r\nGyroscope:     X = %d , Y = %d , Z = %d\r\n'%(mpu9250.Gyro[0], mpu9250.Gyro[1], mpu9250.Gyro[2]))
        print('\r\nMagnetic:      X = %d , Y = %d , Z = %d'%(mpu9250.Mag[0], mpu9250.Mag[1], mpu9250.Mag[2]))
        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()