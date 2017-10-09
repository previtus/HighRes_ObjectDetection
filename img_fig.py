# show figures of images

import os
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np



# paths:
images_folder = "/home/ekmek/saliency_tools/_sample_inputs/images/"
saliency_folder = "/home/ekmek/saliency_tools/_sample_inputs/heatmaps/"
save_mixes_folder = "/home/ekmek/saliency_tools/_sample_inputs/mixes/"

image_files = os.listdir(images_folder)
saliency_files = os.listdir(saliency_folder)

#for i in range(0,2):
for i in range(0,len(image_files)):
    img_path = images_folder+image_files[i]
    sal_path = saliency_folder+saliency_files[i]

    img = Image.open(img_path)
    sal = Image.open(sal_path).convert("RGB").resize(img.size, Image.ANTIALIAS)

    print img.mode, img.size, sal.mode, sal.size

    #img.show()
    #sal.show()

    mix = Image.blend(img, sal, alpha=0.9)

    mix.save(save_mixes_folder+image_files[i])
    #mix.show()

    #print img, sal