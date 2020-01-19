import glob
import os
from PIL import Image

# gif_name = 'outputName'
# file_list = glob.glob('*.png') # Get all the pngs in the current directory
# list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case

# with open('image_list.txt', 'w') as file:
#     for item in file_list:
#         file.write("%s\n" % item)

# os.system('convert @image_list.txt {}.gif'.format(gif_name)) # On windows


# 1. Gif2pngs
# 2. Pngs2gif
# 3. Apply distort to all pngs

def gif2pngs(filePath, folder):
    im = Image.open("example.gif")
    print(dir(im))
    