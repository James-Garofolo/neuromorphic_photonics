Python files used for optical neuromorphics research

File descriptions:

* circuit_funciton.py: mathematical model of current repeater circuit, with modifyable input current timeseries. uses matplotlib to generate time series for each signal of interest in the design. currently configured to repeat random currents between 0 and 1 amps

* data_collection.py: python script to poll serial data from an arduino and store it as a series of .csv files in ../data for later analysis

* doppler_shift.py: small wavelength calculation of the magnitude of change in wavelength in response to objects moving at speeds that would be reasonable to measure with a lidar sensor. results show the change is likely not significant enough to be measurable

* instrument_control.py: WIP attempt to control optical attenuator via USB-GPIB port in python

* snn_signal.py: simulation of the mathematical model for LIF neurons described in Dr. Paul Prucnal's Neuromorphic Photonics textbook

* test.py: catch-all python file for testing syntaxes, algorithms, methods, calculations, etc.