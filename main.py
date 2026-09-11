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

    # print("Rows: ", len(pixels))
    # print("Columns: ", len(pixels[0]))
    print("Successfully loaded pixel data!")
    return pixels

def buildBrightnessMatrix():
    brightness = []

    pixel_matrix = loadImgData(image)

    for pixel_row in pixel_matrix:
        brightness_row = []

        for pixel in pixel_row:
            calc = (pixel[0] + pixel[1] + pixel[2]) / 3
            calc = round(calc)
            brightness_row.append(calc)
        brightness.append(brightness_row)

    print("Successfully constructed brightness matrix!")
    return brightness

def brightnessToAscii():
    asciiStr = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

    # 0 to 255
    # brightness of 50 is 50 / 255 = b
    # b x len(asciiStr)-1 = i character

    asciiMatrix = []
    brightnessMatrix = buildBrightnessMatrix()

    for pixel_row in brightnessMatrix:
        ascii_row = []
        for pixel in pixel_row:
            b = (pixel / 255)
            char = (b * (len(asciiStr)-1))
            char = round(char)
            asciichar = asciiStr[char]
            ascii_row.append(asciichar)
        asciiMatrix.append(ascii_row)
    print("Successfully constructed ASCII matrix!")
    return asciiMatrix

readImg(image)
buildBrightnessMatrix()
brightnessToAscii()