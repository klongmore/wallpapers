from PIL import Image
import os
from os import listdir
from os.path import isfile, join, dirname, realpath

ppath = dirname(realpath(__file__))
os.system('mkdir -p ' + ppath + '/mobile/')
os.system('mkdir -p ' + ppath + '/square/')
os.system('mkdir -p ' + ppath + '/desktop/')
for file in [f for f in listdir(ppath) if isfile(join(ppath, f))]:
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img = Image.open(ppath + '/' + file)
        ratio = round(img.size[0] / img.size[1], 1)
        if ratio <= 0.8:
            os.system('mv ' + ppath + '/' + file + ' ' + ppath + '/mobile/' + file)
        elif ratio > 0.8 and ratio <= 1.4:
            os.system('mv ' + ppath + '/' + file + ' ' + ppath + '/square/' + file)
        else:
            os.system('mv ' + ppath + '/' + file + ' ' + ppath + '/desktop/' + file)
