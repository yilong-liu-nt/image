import numpy as np 
from PIL import Image
import math

n= 900
k = 30
my_array = np.uint8(np.zeros([n, n])*255)


def add_x(my_array, n, k):
    for i in range(n):
        for j in range(i-k, i):
            if j >= 0 and j<n:
                my_array[i, j] =255
        for j in range(i, i+k):
            if j>=0 and j < n:
                my_array[i, j] =255

    for i in range(n):
        for j in range(n-i, n-i +k):
            if j >= 0 and j < n:
                my_array[i, j] =255
        for j in range(n-i -k, n-i):
            if j >= 0 and j < n:
                my_array[i, j] =255

    return my_array


def add_black_white(my_array, n, k):
    white_flag = True
    for i in range(0,n,k):
        for j in range(0,n,k):
            if white_flag:
                value = 255
            else:
                value = 0
            white_flag = not white_flag
            my_array[i:(i+k), j:(j+k)] = value
    return my_array


def add_circle(my_array, n, k):
    delta_angle = 1
    for radius in range(1, n//2, k):
        print("\n Radius", radius)
        for angle in range(0, 361, delta_angle):
            x = radius * math.cos(angle/180 *math.pi) + n//2
            x = int(x)
            y = radius * math.sin(angle/180 *math.pi) + n//2
            y = int(y)

            my_array[x, y] = 255

    return my_array



def add_fib_circle(my_array, n, k):
    delta_angle = 2
    radius_f0 = 0
    radius_f1 = 1

    while True:
        radius = radius_f0 + radius_f1
        radius_f0 = radius_f1
        radius_f1 = radius
        if radius >= n//2:
            break
        print("\n Radius", radius)
        for angle in range(0, 361, delta_angle):
            x = radius * math.cos(angle/180 *math.pi) + n//2
            x = int(x)
            y = radius * math.sin(angle/180 *math.pi) + n//2
            y = int(y)

            my_array[x, y] = 255


    return my_array


def add_fib_golden(my_array, n, k):

    radius_f0 = 0
    radius_f1 = 1

    golden_angle = 137.5
    angle = 0
    while True:
        radius = radius_f0 + radius_f1
        radius_f0 = radius_f1
        radius_f1 = radius
        if radius >= n//2 * k:
            break

        x = float(radius)/k * math.cos(angle/180 *math.pi) + n//2
        x = int(x)
        y = float(radius)/k * math.sin(angle/180 *math.pi) + n//2
        y = int(y)

        angle += golden_angle

        my_array[(x-1):(x+1), (y-1):(y+1)] = 255

        print(radius, np.mod(angle, 360), x, y)


    return my_array

# my_array = add_x(my_array, n, k)
# my_array = add_black_white(my_array, n, k)
# my_array = add_circle(my_array, n, k)
# my_array = add_fib_circle(my_array, n, k)
my_array = add_fib_golden(my_array, n, k)

my_image = Image.fromarray(my_array)
my_image.show()