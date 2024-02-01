from PIL import Image
import numpy as np

my_image = Image.open("cow.jpg")

my_image.show("Original image")


my_array = np.asarray(my_image)

# make it brighter
factor = 1.5
my_array = my_array * factor

my_array[my_array>255] = 255
my_array = my_array.astype(np.uint8)
print(my_array)

enhanced_image = Image.fromarray(my_array)
enhanced_image.show(str(factor))


# make it darker
factor = 0.1
my_array = my_array * factor

my_array = my_array.astype(np.uint8)
print(my_array)

enhanced_image = Image.fromarray(my_array)
enhanced_image.show(str(factor))