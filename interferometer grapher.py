import numpy as np
import math
import matplotlib.pyplot as plt
from helper import *


na = 81  #width of moving average
nm = 81   #width of moving median
threshold = 0.5 #for schmitt trigger
buffer = 0.1 #also for schmitt trigger
averaging = True
median = True
normalizing = True
schmitt = True

folder_name = '4-26-19'



class Sensor(object):
    def __init__(self):
        self.voltages = []
        self.times = []
        self.minima = []
        sensors.append(self)

    def apply_median(self, n=5):
        self.times, self.voltages = med(self.voltages, self.times, n=n)

    def apply_average(self, n=5):
        self.times, self.voltages = avg(self.voltages, self.times, n=n)

    def apply_normalization(self):
        self.voltages = normalize(self.voltages)

    def apply_schmitt(self):
        self.voltages = schmitt_trigger(self.voltages, threshold, buffer)


def load_data():
    times = []
    leftVoltages = []
    midVoltages = []
    rightVoltages = []

    filename = input("Filename: ")
    file = open(folder_name+"\\"+filename+".txt", "r")
    lines = file.readlines()
    file.close()


    for line in lines:
        pair = line[:-2].split(": ")  #-2 to remove newline character

        time = float(pair[0])
        voltages = np.array(pair[1].split(", ")).astype(float)
        vleft = voltages[0]
        vmid = voltages[1]
        vright = voltages[2]
        
        times.append(time)
        leftVoltages.append(vleft)
        midVoltages.append(vmid)
        rightVoltages.append(vright)

    return times, leftVoltages, midVoltages, rightVoltages


def plot_setup():
    fig, ax = plt.subplots(2, 2)
    fig.subplots_adjust(hspace=0.5)
    
    ax[0,0].set_title("Raw data")
    ax[0,1].set_title("Average (na={})".format(na))
    ax[1,0].set_title("Average and median, normalized (nm={})".format(nm))
    ax[1,1].set_title("Average, median, and Schmitt trigger\n(threshold={}, buffer={})".format(threshold,buffer))
    return fig, ax

        

sensors = []
sL = Sensor()
sM = Sensor()
##sR = Sensor()
    
while True:    
    data = load_data()
    fig, ax = plot_setup()
    
    for i,sensor in enumerate(sensors):
        sensor.times = data[0]
        sensor.voltages = data[i+1]
    
    for sensor in sensors:
        ax[0,0].plot(sensor.times, sensor.voltages)
        if averaging:
            sensor.apply_average(na)
            ax[0,1].plot(sensor.times, sensor.voltages)
        if normalizing:
            sensor.apply_normalization()
        if median:
            sensor.apply_median(nm)
            ax[1,0].plot(sensor.times, sensor.voltages)
        if schmitt:
            sensor.apply_schmitt()
            ax[1,1].plot(sensor.times, sensor.voltages)

##    left_minima = find_troughs(times, leftVoltages)
##    mid_minima = find_troughs(times, midVoltages)
##    right_minima = find_troughs(times, rightVoltages)
##
##    left_x = []
##    left_y = []
##    right_x = []
##    right_y = []
##
##    for point in left_minima:
##        left_x.append(point[0])
##        left_y.append(point[1])
##    for point in right_minima:
##        right_x.append(point[0])
##        right_y.append(point[1])
##    
##
##    print("Dark fringes: ", len(right_minima))

    #plt.plot(times, leftVoltages)
    #plt.plot(times, midVoltages)
    #plt.plot(times, rightVoltages)
##    plt.scatter(left_x, left_y)
    #plt.scatter(right_x, right_y)
    
##    for minimum in left_minima:
##        plt.plot((minimum[0], minimum[0]), (1.001, 1.01), 'black', lw=0.6)
##    for minimum in mid_minima:
##        plt.plot((minimum[0], minimum[0]), (1.001, 1.01), 'black', lw=0.6)
##    for minimum in right_minima:
##        plt.plot((minimum[0], minimum[0]), (1.001, 1.01), 'black', lw=0.6)
##        
    plt.show()
