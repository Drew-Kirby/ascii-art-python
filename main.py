from PIL import Image

image = ("ascii-pineapple.jpg")

def readImg(im):
    img = Image.open(im)

    if img._open:
        print("Successfully loaded image!")
        print("Image size: ", img.width, "x", img.height)
    else:
        print("error")

def loadImgData(im):
    img = Image.open(im)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = []

    for y in range(img.height):
        row = []

        for x in range(img.width):
            pixel = img.getpixel((x,y))
            row.append(pixel)

        pixels.append(row)

    print("Rows: ", len(pixels))
    print("Columns: ", len(pixels[0]))

loadImgData(image)
readImg(image)
