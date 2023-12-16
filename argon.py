from smbus import SMBus
from time import sleep

bus = SMBus(1)
i2c_address = 0x1a

def read_temp():
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    cpu_temp = f.read()
    f.close()
    return int(cpu_temp)
    # print(temp)

def update_fan():
    temp = read_temp() / 1000
    temp1 = 40
    temp2 = 70
    temp_range = temp2 - temp1
    temp_percentage = int((temp - temp1) / (temp_range) * 100)
    if temp_percentage < 0:
        temp_percentage = 0    
    amt_hex = int(hex(temp_percentage), 16)
    bus.write_byte(i2c_address, amt_hex)
    return temp_percentage

while True:
    print('CPU Temp:', int((read_temp() / 1000)),'c')
    print('Fan Speed:',update_fan(),'%')
    sleep(10)