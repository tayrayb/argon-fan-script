import os
from time import sleep
from smbus2 import SMBus

bus = SMBus(1)
addr = 0x1a

while True:
    temp = int(open("/sys/class/thermal/thermal_zone0/temp", "r").readline())/1000
    if temp <= 40:
        bus.write_byte(addr, 0)
    if temp > 40:
        bus.write_byte(addr, 1)
    if temp > 45:
        bus.write_byte(addr, 50)
    if temp > 50:
        bus.write_byte(addr, 100)
    sleep(10)
