#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray

import time
import smbus

import paho.mqtt.client as paho

class mpu6050:

    address = None
    bus = None
    
    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C

    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F

    TEMP_OUT0 = 0x41

    GYRO_XOUT0 = 0x43
    GYRO_YOUT0 = 0x45
    GYRO_ZOUT0 = 0x47

    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        # Wake up the MPU-6050 since it starts in sleep mode
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)

    # I2C communication methods

    def read_i2c_word(self, register):
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    def get_accel_data(self, g = False):
        x = self.read_i2c_word(self.ACCEL_XOUT0)
        y = self.read_i2c_word(self.ACCEL_YOUT0)
        z = self.read_i2c_word(self.ACCEL_ZOUT0)

        return [x, y, z]

    def get_gyro_data(self):
        x = self.read_i2c_word(self.GYRO_XOUT0)
        y = self.read_i2c_word(self.GYRO_YOUT0)
        z = self.read_i2c_word(self.GYRO_ZOUT0)

        return [x, y, z]

    def get_all_data(self):
        temp = self.get_temp()
        accel = self.get_accel_data()
        gyro = self.get_gyro_data()

        return [accel, gyro, temp]

mpu = mpu6050(0x68)

accel = [0]*3
gyro = [0]*3

broker = "localhost"
client = paho.Client("accelerometre-publisher")

def accelerometre():
    
    pub = rospy.Publisher('/accelerometre', Float32MultiArray, queue_size=10)
    rospy.init_node('accel_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        accel = mpu.get_accel_data()
        gyro = mpu.get_gyro_data()
        
        #1=GaucheDroite 2=HautBas 3=  4= 5=VitesseHaut 6=VitesseAvant
        accel_data = Float32MultiArray()
        speed = gyro[1] / 131.0
        angleY = accel[1]/16384.0 + 0.06
        angleX = accel[0]/(-16384.0) + 0.16
        accel_data.data = [angleX, angleY, speed]
        
        strAccel = str(speed) + "@" + str(angleX) + "@" + str(angleY)
        client.publish("accel", strAccel)
        
        pub.publish(accel_data)
        rate.sleep()

if __name__ == '__main__':
    try:
        print("Connecting to broker...")
        client.connect(broker)

        accelerometre()
    except rospy.ROSInterruptException:
        pass
