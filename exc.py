from PIL import Image, ImageEnhance

my_image = Image.open("cow.jpg")

my_image.show("Original image")

img_enhancer = ImageEnhance.Brightness(my_image)

factor = 1.5
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.show(title=str(factor))

factor = 0.5
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.show(str(factor))