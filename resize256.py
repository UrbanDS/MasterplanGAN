from PIL import Image, ImageFilter
import numpy as np
import os
from os.path import join

for root, dirs, files in os.walk('/scratch/user/jiaxin.du/DeepPS/data/dataset/trainBack'):
    for name in files:
        first_image = Image.open(join(root, name)).convert("RGBA")  # results after GAN
        h1, w1 = first_image.size
        image_pil = first_image.resize((512, 256), Image.BICUBIC)
        image_pil.save('/scratch/user/jiaxin.du/DeepPS/data/dataset/train/' + name)


im = Image.open('test.png')
im = im.convert('RGBA')
se = im.crop((100, 100, 1124, 1124))
data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
white_areas = (red > 200) & (blue > 200) & (green >200)
data[..., :-1][white_areas.T] = (0, 0, 0) # Transpose back needed

im2 = Image.fromarray(data)

im2 = Image.open('cz.png')
background = Image.new('RGBA', im2.size, (255,255,255))
alpha_composite = Image.alpha_composite(background, im2)
alpha_composite.save('cz.png', 'PNG', quality=80)

