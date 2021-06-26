import math
import numpy as np

def avg(y, x=None, n=5):
    if n%2 == 0:
        print("n must be an odd number")

    else:
        avg_y = []
        h = int((n-1)/2) #buffer width on either side of current point

        for i in range(h, len(y)-h):
            group = y[i-h:i+h+1]
            value = sum(group)/len(group)
            avg_y.append(value)

        if x == None:
            return avg_y
        else:
            new_x = x[h:-h]
            return new_x, avg_y


def med(y, x=None, n=5):
    med_y = []
    h = int((n-1)/2)

    if n%2 == 0:
        raise ValueError("Input 'n' for med function must be odd")

    for i in range(h, len(y)-h):
        group = y[i-h:i+h+1]
        ordered = sorted(group)
        value = ordered[int((n-1)/2)]
        med_y.append(value)
        
##        elif n%2 == 0:
##            value = (ordered[n/2-1]+ordered[n/2])/2
##            med_y.append(value)

    if x == None:
        return med_y
    else:
        new_x = x[h:-h]
        return new_x, med_y


def schmitt_trigger(voltages, threshold=0.5, buffer=0.1):
    new_vals = []
    first_val = voltages[0]
    new_vals.append(compare(first_val, threshold))
    
    for v in voltages[1:]:
        if new_vals[-1] == 0:
            new_vals.append(compare(v, threshold + buffer)) 
        elif new_vals[-1] == 1:
            new_vals.append(compare(v, threshold - buffer))
    return new_vals

def compare(val, threshold):
    if val >= threshold:
        return 1
    elif val < threshold:
        return 0


def normalize(y):
    high = max(y)
    low = min(y)
    height = high-low
    new_y = (np.array(y)-low)/height
    return new_y

def find_zero(x): #for an increasing data set with one zero
    x = np.array(x)
    i = int(len(x)/2) #start in middle of the set
    di = int(i/2)
    searching = True

    while searching:
        print(i)
        if x[i] > 0:
            i = i-di
        elif x[i] < 0:
            i = i+di
        di = int(di/2)
        if di == 0:
            searching = False
            print(i)

    if x[i] > 0:
        return (x[i-1], x[i])
    elif x[i] < 0:
        return (x[i], x[i+1])
    elif x[i] == 0:
        print("Exact value found in set")
        return x[i]
        

        
def find_min(x, y):
    x_bounds = find_zero(x_shifted) #finds the two points in the data set closest to x1


def find_troughs(x, y): #clean up this function
    high = max(y)
    threshold = 0.6*high
    start = 0
    end = 0
    troughs = []
    minima = []
    x_minima = []

    for i in range(len(x)):
        if start == 0:
            if y[i] < threshold:
                start = i

        elif start != 0: #i.e. marker is currently in a trough
            if y[i] > threshold:
                end = i
                x_trough = list(x)[start:end]

                if len(x_trough) > 1:
                    x_min = x_trough[0]+(x_trough[-1]-x_trough[0])/2
                else:
                    x_min = x_trough[0]

                middle_i = math.floor((start+end)/2) #index in the center

                x_minima.append(x_min)
                minima.append((x[middle_i], y[middle_i]))
                start, end = 0,0
    return minima
