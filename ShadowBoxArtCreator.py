from PIL import Image
import numpy as np

image = np.asarray(Image.open('random.jpg'))
num_rows, num_cols, depth = image.shape
pixelsize = 1
hexvalue = '#%02x%02x%02x' % (image[0][0][0], image[0][0][1], image[0][0][2])

f = open("teststyle.css", "a")

f.write(""".box-shadow-trick {bracket} 
    background: {hex}; 
    height: {px}px; 
    width: {px}px;
    box-shadow: """.format(px=pixelsize, bracket = "{", hex=hexvalue))

for i in range(num_rows):
    for j in range(num_cols):
        if(i == 0 and j == 0):
            break
        hexvalue = '#%02x%02x%02x' % (image[i][j][0], image[i][j][1], image[i][j][2])
        strtoappend = str(j*pixelsize) + "px " + str(i*pixelsize) + "px 0 " + hexvalue
        if(i == num_rows - 1 and j == num_cols - 1):
            strtoappend += ";\n"
        else:
            strtoappend += ",\n\t\t"
        f.write(strtoappend)

f.write("}")