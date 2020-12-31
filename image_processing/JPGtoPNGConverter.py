import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

images = os.listdir(image_folder)

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for i in range(len(images)):
    jpg = Image.open(image_folder + '/' + images[i])
    jpg.save(output_folder + '/' + images[i][:-4] + '.png', 'png')
