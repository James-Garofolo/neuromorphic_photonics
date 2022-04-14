import serial
import numpy as np
import os
import time as t

com = None

while com == None:
    try:
        com = serial.Serial(port = "COM3")
        t_start = t.time_ns()
    except serial.serialutil.SerialException:
        pass


sampled = []
latched = []
out = []
time = []
in_level = 0
data = []
in_data = None
max = 0
max_idx = 0

print("started")
while in_data != "end":

    # read the data in as a string, remove newlines and split on commas
    in_data = str(com.readline().decode()).removesuffix("\r\n").split(",") 

    if in_data[0] == "s": # sampled voltage
        sampled.append(int(in_data[1]))
    elif in_data[0] == "l": # latched voltage
        latched.append(int(in_data[1]))
    elif in_data[0] == "o": # output laser current
        out.append(int(in_data[1]))
        time.append(t.time_ns() - t_start)
    elif in_data[0] == "in": # input laser current
        if len(sampled) > max: # record maximum number of loops and 
            max = len(sampled)
        data.append([sampled, latched, out, time, np.ones_like(sampled)*in_level]) # save the current page of data
        in_level = in_data[1] # save new input level
        sampled = [] # reinitialize data arrays
        latched = []
        out = []
        time = []
        t_start = t.time_ns() # get new starting time
        print(in_level)
    elif in_data[0] != "end":
        print(in_data)
    

for d in data: # make all of the arrays the same size by appending zeros to tests that ended earlier
    while len(d[0]) < max:
        for arr in d:
            arr.append(0)


a = np.array(data) * 5 / 1024 # create a numpy array for data and scale it to transform it from counts to volts/amps

print(a)

np.savetxt(os.getcwd() + "/data/arduino_test.csv", a, delimiter=",")
