import numpy as np
import matplotlib.pyplot as plt
import math
import time

start_time = time.perf_counter()



# DON'T FORGET ARRAYS WORK AS [Y,X] INSTEAD OF (X,Y)
# THIS WILL FUCK YOU UP


width  = 100  +1
height = 100  +1

input = "7/(np.cos(x/5))"


input = input.replace(" ","")
input = input.replace("^","**")


img = np.zeros((height,width,3))

for x in range(len(img[0])):
    img[x, math.floor(width/2)] = [255,255,255]

for y in range(len(img)):
    img[math.floor(height/2), y] = [255,255,255]


step = 0.01

for x in np.arange(0, len(img[0]), step):

    x = x - math.floor(width/2)

    if eval(input) == math.inf or eval(input) == -math.inf:
        continue

    y_value = -math.floor(eval(input))

    if y_value <= height - math.floor(height/2) - 1 and y_value >= -height + math.floor(height/2) + 1:
        img[y_value + math.floor(height/2), int(x) - math.floor(width/2) - 1] = [255,0,0]



plt.imshow(img)
print(time.perf_counter() - start_time)
plt.show()
