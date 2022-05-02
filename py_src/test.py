import serial
import numpy as np
import os
import time as t

com = None

while com == None:
    try:
        com = serial.Serial(port = "COM3")
    except serial.serialutil.SerialException:
        pass

print("started")

while True:
    indata = str(com.readline().decode('ascii')).removesuffix("\r\n")
    print(indata)

