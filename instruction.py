# PIL stands for Python Imaging Library, is a powerful library in Python
# that allows users to open, manipulate, and save various image file formats. It provides
# a wide range of features for image processing tasks such as resizing, cropping, applying filters, and more.
from PIL import Image

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
import matplotlib.pyplot as plt

# Read the image
img = Image.open("./images/Bird.jpeg")

# The .show() method saves the image as a temporary file and displays
# it using your operating system’s native software for dealing with images.
img.show()


# -------------------------------------------------------------------------------------------------
# Explore image size, format, and mode using the Image class attributes .format, .size, and .mode
# -------------------------------------------------------------------------------------------------
# size (width and height) of the image
print(img.size)
print(img.width)
print(img.height)

# format of the image (e.g., JPEG, PNG, GIF, BMP, TIFF and etc)
print(img.format)

# mode of image (e.g., L/grayscale, RGB, RGBA)
print(img.mode)

# resolution of printed image
dpi = img.info["dpi"]
print(dpi)

# change image resolution
img.save("./images/Bird_lowRes.jpeg", quality=10)
lowRes_img = Image.open("./images/Bird_lowRes.jpeg")



# Exif to extract image metadata, (details about the image and its production such height, width, date and time)
# These metadata, often created by cameras and other capture devices, include technical information
# about an image and its capture method, such as exposure settings, capture time, GPS location information
# and camera model
exifdata = img.getexif()
print(exifdata)

# looping through all the tags present in exifdata to convert the exif tag id into human readable form
from PIL.ExifTags import TAGS
for tagid in exifdata:
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")


# --------------------------------------------------------------------------------
# Get a pixel value from an image:
# --------------------------------------------------------------------------------
# Get all pixel values of the image
# You can get pixel (x, y) by pixel_values[width*y+x]
pixel_values = list(img.getdata())
npixels = len(pixel_values)
print(npixels)

x = 1
y = 2
width, height = img.size
print(pixel_values[width*y+x])

# .getpixel(xy) method returns the pixel value at a given position, where
#  xy – The coordinate, given as (x, y)
mypixel = (x,y)
print(img.getpixel(mypixel))


# When translating a color image to greyscale (mode “L”), the library uses the ITU-R 601-2 luma transform:
# L = R * 299/1000 + G * 587/1000 + B * 114/1000
grey_img = img.convert(mode='L')
grey_img.save("./images/grey_Bird.jpg")
print(grey_img.mode)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))

# Plot the original image
axs[0].imshow(img)
axs[0].set_title('Original Image')

# Plot the greyscale image
axs[1].imshow(grey_img)
axs[1].set_title('Grayscale Image')

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------------------------------
# Resized image using .resize method
# Syntax: Image.resize(size, resample=0)
# Parameters:
# size – The requested size in pixels, as a 2-tuple: (width, height).
# resample – An optional resampling filter. This can be one of PIL.Image.NEAREST (use nearest neighbour),
#            PIL.Image.BILINEAR (linear interpolation), PIL.Image.BICUBIC (cubic spline interpolation),
#            or PIL.Image.LANCZOS (a high-quality downsampling filter). If omitted, or if the image
#            has mode “1” or “P”, it is set PIL.Image.NEAREST. Otherwise, the default filter is
#            Resampling.BICUBIC.
# ------------------------------------------------------------------------------------------------------
newsize = (300, 300)
resize_img = img.resize(newsize)
resize_img.show()



# ---------------------------------------------------------------------------------------------------------
# Basic image transformation use the .transpose() method
# There are seven options that you can pass as arguments to .transpose():
#     Image.FLIP_LEFT_RIGHT: Flips the image left to right, resulting in a mirror image
#     Image.FLIP_TOP_BOTTOM: Flips the image top to bottom
#     Image.ROTATE_90: Rotates the image by 90 degrees counterclockwise
#     Image.ROTATE_180: Rotates the image by 180 degrees
#     Image.ROTATE_270: Rotates the image by 270 degrees counterclockwise, which is the
#                       same as 90 degrees clockwise
#     Image.TRANSPOSE: Transposes the rows and columns using the top-left pixel as the origin, with
#                      the top-left pixel being the same in the transposed image as in the original image
#     Image.TRANSVERSE: Transposes the rows and columns using the bottom-left pixel as the origin, with
#                       the bottom-left pixel being the one that remains fixed between the original and
#                       modified versions
# ---------------------------------------------------------------------------------------------------------

# Flip the original image vertically
vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.show()
vertical_img.save("./images/vertical.jpeg")

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))

# Plot the original image
axs[0].imshow(img)
axs[0].set_title('Original Image')

# Plot the greyscale image
axs[1].imshow(vertical_img)
axs[1].set_title('Flipped Image')

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()



# -------------------------------------------------------------------------------------
#  Crop and resize images. The Image class has two methods that you can use to
#  perform these operations, .crop() and .resize():
# -------------------------------------------------------------------------------------

# Crop the image
width, height = img.size

# Setting the points for cropped image
left = 2 * width / 4
top = height / 5
right = 3 * width / 4
bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change original image)
# Image.crop(box=None) returns a rectangular region from this image.
# The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate
crop_img = img.crop((left, top, right, bottom))
crop_img.show()

newsize = (600, 800)
resize_img = crop_img.resize(newsize)

# Shows the image in image viewer
resize_img.show()

# -------------------------------------------------------------------------------------
# Image filtering and blurring
# .filter() method to apply filtering to the image
# The ImageFilter module contains definitions for a pre-defined set of filters, which
# can be used with the .filter() method.
# -------------------------------------------------------------------------------------
from PIL import ImageFilter
blur_img = img.filter(ImageFilter.BoxBlur(20))

blur_img.save("./images/blur_Bird.jpeg")

fig, axs = plt.subplots(1, 2, figsize=(7, 4))

# Plot the original image
axs[0].imshow(img)
axs[0].set_title('Original Image')

# Plot the greyscale image
axs[1].imshow(blur_img)
axs[1].set_title('Blurred Image')

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# Adding text on image
# --------------------------------------------------------------------
from PIL import ImageDraw, ImageFont

# Call draw Method to add 2D graphics in an image
text_img = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('FreeMono.ttf', 145)

# Add Text to an image at the starting position (in pixels) (x, y)
text = 'THIS PHOTO WAS TAKEN \n IN ALASKA (2023)'

text_img.text((100, 200), text, font=myFont, fill="red", align="left")

# Display edited image
img.show()

# Save the edited image
text_img.save("Bird_text.jpg")


# --------------------------------------------------------------------
# Superposition of images using .paste method
# --------------------------------------------------------------------
tiger = Image.open("./images/tiger.jpeg")
tiger.show()

grey_tiger = tiger.convert(mode='L')
grey_tiger.show()
grey_tiger.save("./images/grey_tiger.jpeg")

binary_tiger = tiger.convert(mode='1')
binary_tiger.show()
binary_tiger.save("./images/binary_tiger.jpeg")

# Pasting tiger image on top of img starting at coordinates (x, y)
img.paste(tiger,(3 * img.width // 4, 4 * img.height // 5))
img.show()

img.save('./images/BirdandTiger.jpeg')
