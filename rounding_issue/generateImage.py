#!/usr/bin/env python3

# from https://stackoverflow.com/questions/69117672/how-to-make-a-color-grid-in-python-using-pil

import numpy as np
from PIL import Image
import math

# Generate 10x10 grid of random colours
#grid = np.random.randint(0,256, (10,10,3), dtype=np.uint8)
#print (grid)
#grid = [
#    [89, 102, 145], [89, 102, 145], [207, 229,  22],
#    [89, 102, 145], [89, 102, 145], [207, 229,  22],
#    [207, 229,  22], [207, 229,  22], [207, 229,  22]
#]

# Make into PIL Image and scale up using Nearest Neighbour
#im = Image.fromarray(np.asarray(grid)).resize((1536,1536), resample=Image.NEAREST)
#im = Image.fromarray(grid).resize((1600,1600), resample=Image.NEAREST)

#im.save('result.png')

image_blank = np.zeros((3, 3, 3), np.uint8)
image_blank[0][0] = (89, 102, 145) # Bluey
image_blank[0][1] = (89, 102, 145) # Bluey
image_blank[1][0] = (89, 102, 145) # Bluey
image_blank[1][1] = (89, 102, 145) # Bluey

image_blank[0][2] = (207, 229, 22) # Yellow
image_blank[1][2] = (207, 229, 22) # Yellow
image_blank[2][2] = (79,  235, 52) # Green 52, 235, 79
image_blank[2][0] = (190,  98,  89) # Redy
image_blank[2][1] = (190,  98,  89) # Redy

#image_blank.save(image_filename)
im = Image.fromarray(image_blank).resize((1536,1536), resample=Image.NEAREST)

im.save('regular.jpg')

width = 3073
height = width
tileWidth = 2048
tileHeight = 2048
odd_image = np.zeros((width,height, 3), np.uint8)
tileNoX = math.ceil(width/tileWidth)
tileNoY = math.ceil(height/tileHeight) 
print (f"TileNoX: {tileNoX} {width / tileWidth}, TileNoY: {tileNoY}")
colourGrid = np.random.randint(0,256, (tileNoX,tileNoY,3), dtype=np.uint8)

for x in range(0, width):
    for y in range(0,height):
        tilePositionX = math.ceil(x / tileWidth) - 1 
        tilePositionY = math.ceil(y / tileHeight) - 1 
        odd_image[x][y] = colourGrid[tilePositionX][tilePositionY]

im = Image.fromarray(odd_image)

im.save('odd.jpg')