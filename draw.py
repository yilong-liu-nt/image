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


def cows(my_array, n):
    for x in range(n):
        radius =  (n-2)//3
        offset = n //2 
        k = 100
        y = math.sin( x*math.pi/2 /30) * radius + offset
        y = int(y)
        print(x, y)
        my_array[y, x] = 255
    return my_array


def add_golden_spiral(my_array, n, angle_0 = 0):

    golden_angle = 137.5
    angle = angle_0
    radius = 1
    while radius < n//2:

        x = radius * math.cos(angle/180 *math.pi) + n//2
        x = int(x)
        y = radius * math.sin(angle/180 *math.pi) + n//2
        y = int(y)

        angle += golden_angle

        my_array[(x-1):(x+1), (y-1):(y+1)] = 255

        print(radius, np.mod(angle, 360), x, y)
        radius += 0.2

    return my_array



def add_triangle(my_array, n, p1, p2, p3):

    def draw_line(my_array, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        if x1 != x2:
            slope = (y2-y1)/(x2-x1)

            if x2 >= x1:
                for x in np.arange(x1, x2, 0.1):
                    y = (x-x1) * slope + y1

                    my_array[int(x), int(y)] = 255
            else:
                for x in np.arange(x2, x1, 0.1):
                    y = (x-x1) * slope + y1

                    my_array[int(x), int(y)] = 255


        else:
            if y2 >= y1:
                for y in range(y1, y2+1):
                    my_array[x1, y] = 255
            else:
                for y in range(y2, y1+1):
                    my_array[x1, y] = 255


    
    # draw a line between p1 and p2
    draw_line(my_array, p1, p2)


    # draw a line between p2 and p3
    draw_line(my_array, p2, p3)


    # draw a line between p1 and p3
    draw_line(my_array, p1, p3)

    return my_array

# my_array = add_x(my_array, n, k)
# my_array = add_black_white(my_array, n, k)
# my_array = add_circle(my_array, n, k)
# my_array = add_fib_circle(my_array, n, k)
# my_array = add_fib_golden(my_array, n, k)
# my_array = cows(my_array, n)
# my_array = add_golden_spiral(my_array, n, k)

my_array = add_triangle(my_array, n, (69, 69), (42, 800), (420, 900))
my_image = Image.fromarray(my_array)
my_image.show()