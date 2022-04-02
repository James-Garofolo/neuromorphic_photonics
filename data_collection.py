import serial
import numpy as np
import os

com = None

while com == None:
    try:
        com = serial.Serial(port = "COM3")
    except serial.serialutil.SerialException:
        pass


sampled = []
latched = []
out = []
in_data = None

print("started")
while in_data != "end":
    in_data = str(com.readline().decode()).removesuffix("\r\n")

    if in_data == "s":
        in_data = str(com.readline().decode()).removesuffix("\r\n")
        sampled.append(int(in_data))
    elif in_data == "l":
        in_data = str(com.readline().decode()).removesuffix("\r\n")
        latched.append(int(in_data))
    elif in_data == "o":
        in_data = str(com.readline().decode()).removesuffix("\r\n")
        out.append(int(in_data))
    elif in_data != "end":
        print(in_data)
    
a = np.array([sampled, latched, out]).transpose() * 5 / 1024

print(a)

np.savetxt(os.getcwd() + "/data/arduino_test.csv", a, delimiter=",")
