from smbus import SMBus
from time import sleep
import os

bus = SMBus(1)
i2c_address = 0x1a

def read_temp():
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    cpu_temp = f.read()
    f.close()
    return int(cpu_temp)
    # print(temp)

def fan_percentage():
    temp = read_temp() / 1000
    temp_min_max = (40, 70)
    temp_range = temp_min_max[1] - temp_min_max[0]
    temp_percentage = int((temp - temp_min_max[0]) / (temp_range) * 100)
    if temp_percentage < 0:
        temp_percentage = 0
    return temp_percentage

def update_fan():
    amt_hex = int(hex(fan_percentage()), 16)
    bus.write_byte(i2c_address, amt_hex)

while True:
    print('CPU Temp:', int((read_temp() / 1000)),'c')
    print('Fan Speed:',fan_percentage(),'%')
    update_fan()
    sleep(10)
    os.system('clear')
