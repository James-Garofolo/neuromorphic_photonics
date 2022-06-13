import serial
import numpy as np
import os
import time as t
import matplotlib.pyplot as plt

com = None

while com == None:
    try:
        com = serial.Serial(port = "COM3", baudrate=115200)
        t_start = t.time_ns()
    except serial.serialutil.SerialException:
        pass


sampled = []
sample_t = []
latched = []
latch_t = []
out = []
out_t = []
in_lvl = []
in_t = []

in_data = None

print("started")

while in_data != "end":
    in_data = str(com.readline().decode('ascii')).removesuffix("\r\n")
    parts = in_data.split(",")
    try:
        if parts[0] == "s": # sampled voltage
            sample_t.append(int(parts[1]))
            sampled.append(int(parts[2]))
        elif parts[0] == "l": # latched voltage
            latch_t.append(int(parts[1]))
            latched.append(int(parts[2]))
        elif parts[0] == "o": # output current
            out_t.append(int(parts[1]))
            out.append(int(parts[2]))
        elif parts[0] == "c": # sampled voltage
            in_t.append(int(parts[1]))
            in_lvl.append(int(parts[2]))
        else:
            print(in_data)
    except:
        print(in_data)
        raise ValueError


plt.plot(sample_t, sampled, label="Vsampled")
plt.plot(latch_t, latched, label="Vlatched")
plt.plot(in_t, in_lvl, label="Iin")
plt.plot(out_t, out, label="Iout")
plt.legend()
plt.title("Latching of Random Currents")
plt.xlabel("Time (s)")
plt.ylabel("Voltage/Current")
plt.show()

while len(sampled) < len(latched):
    sampled.append(0)
    sample_t.append(sample_t[-1] + 1)

while len(latched) < len(sampled):
    latched.append(0)
    latch_t.append(latch_t[-1] + 1)

while len(sampled) < len(out):
    sampled.append(0)
    sample_t.append(sample_t[-1] + 1)
    latched.append(0)
    latch_t.append(latch_t[-1] + 1)

while len(out) < len(sampled):
    out.append(0)
    out_t.append(out_t[-1] + 1)

while len(sampled) < len(in_lvl):
    sampled.append(0)
    sample_t.append(sample_t[-1] + 1)
    latched.append(0)
    latch_t.append(latch_t[-1] + 1)
    out.append(0)
    out_t.append(out_t[-1] + 1)

while len(in_lvl) < len(sampled):
    in_lvl.append(0)
    in_t.append(in_t[-1] + 1)


#sampled.insert(0, "sample v")
#sample_t.insert(0, "sample t")
#latched.insert(0, "latch v")
#latch_t.insert(0, "latch t")
#out.insert(0, "out c")
#out_t.insert(0, "out t")
#in_lvl.insert(0, "in c")
#in_t.insert(0, "in t")
a = np.array([sampled, sample_t, latched, latch_t, out, out_t, in_lvl, in_t]).T
#print(a)
np.savetxt(os.getcwd() + "/data/tseries.csv", a, delimiter=",")

