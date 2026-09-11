from PIL import Image

img = Image.open("ascii-pineapple.jpg")

if img._open:
    print("Successfully loaded image!")
    print("Image size: ", img.width, "x", img.height)
else:
    print("error")
