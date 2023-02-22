
import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x58      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_ID = 0x00
DEVICE_REG_EN = 0x01
DEVICE_REG_LEDOUT0 = 0x02
DEVICE_REG_LEDOUT1 = 0x03

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_EN, 0x01)

deviceid = bus.read_byte(DEVICE_ADDRESS, DEVICE_REG_ID)
print(deviceid)

#Write an array of registers
while True:
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, 0x00)
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT1, 0x00)
    print("Leds on")
    time.sleep(1)
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, 0x00)
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT1, 0x00)
    time.sleep(1)
    print("Leds off")

