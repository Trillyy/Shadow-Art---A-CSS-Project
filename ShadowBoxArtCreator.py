from PIL import Image
import os
import numpy as np

def generate(image = 'img.jpg', pixelsize = 1):
    imagename = os.path.splitext(image)[0]
    classname = os.path.split(imagename)[1]

    try:
        image = np.asarray(Image.open(image))
    except:
        print("ShadowBoxArtCreator: File not found!")
        exit()

    try:
        pixelsize = int(pixelsize)
        if pixelsize < 1:
            print("ShadowBoxArtCreator: Invalid Pixel Size!")
            exit()
    except ValueError:
        print("ShadowBoxArtCreator: Invalid Pixel Size!")
        exit()

    num_rows = image.shape[0]
    num_cols = image.shape[1]
    try:
        startinghex = '#%02x%02x%02x' % (image[0][0][0], image[0][0][1], image[0][0][2])
    except:
        print("ShadowBoxArtCreator: Invalid Image! Transparency Found!")
        exit()

    f = open(imagename + ".css", "w")

    f.write(""".{name} {bracket} 
        background: {hex}; 
        height: {px}px; 
        width: {px}px;
        box-shadow: """.format(px = pixelsize, 
                            bracket = "{", 
                            hex = startinghex,
                            name = classname))

    for i in range(num_rows):
        for j in range(num_cols):
            if(i == 0 and j == 0):
                break
            try:
                hexvalue = '#%02x%02x%02x' % (image[i][j][0], image[i][j][1], image[i][j][2])
            except:
                print("ShadowBoxArtCreator: Invalid Image! Transparency Found!")
                os.remove(image)
                exit()
            boxshadowrow = str(j*pixelsize) + "px " + str(i*pixelsize) + "px 0 " + hexvalue
            if(i == num_rows - 1 and j == num_cols - 1):
                boxshadowrow += ";\n"
            else:
                boxshadowrow += ",\n\t\t"
            f.write(boxshadowrow)
    f.write("}")