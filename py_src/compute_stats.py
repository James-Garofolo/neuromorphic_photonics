import matplotlib.pyplot as plt
import numpy as np
import os
import math

arr = np.loadtxt(os.getcwd() + "/data/2.2uF latch.csv", delimiter=",").T

time = []
v_sample = []
i_in = []
i_out = []
heartbeat = []
sample_error = []
output_error = []
state = True

for t in range(len(arr[0])):
    time.append(arr[0,t] - arr[0,0])
    v_sample.append(arr[1,t])
    i_in.append(arr[2,t])
    i_out.append(arr[3,t])
    heartbeat.append(arr[4,t])

    if state:
        if heartbeat[t] < 1:
            state = False
            sample_error.append((i_in[t]-v_sample[t])/i_in[t])
    else:
        if heartbeat[t] > 4:
            state = True
            output_error.append((i_in[t]-i_out[t])/i_in[t])

sample_mean = np.average(sample_error)
sample_stdev = np.std(sample_error)
sample_range = sample_mean + (1.645*sample_stdev/math.sqrt(sample_stdev))
print("sample guy: ", sample_range)

output_mean = np.average(output_error)
output_stdev = np.std(output_error)
output_range = output_mean + (1.645*output_stdev/math.sqrt(output_stdev))
print("output guy: ", output_range)

plt.hist(sample_mean)
plt.hist(output_mean)
plt.ylabel("Probability density")
plt.xlabel("Percentage error")
plt.legend()
plt.show

