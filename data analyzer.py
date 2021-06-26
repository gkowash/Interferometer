import numpy as np

file = open('data3 (excerpt).txt', 'r')
lines = file.readlines()
file.close()

data = []
for pair in lines:
    values = pair.split(", ")
    t = float(values[0])
    v = float(values[1])
    data.append((t, v))

dark_to_bright = 0
bright_to_dark = 0
for i in range(1, len(data)):
    if data[i][1] - data[i-1][1] >= 3:
        dark_to_bright += 1
    elif data[i-1][1] - data[i][1] >= 3:
        bright_to_dark += 1
        print(data[i])

print("Dark to bright: ", dark_to_bright)
print("Bright to dark: ", bright_to_dark)
