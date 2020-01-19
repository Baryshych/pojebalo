from io import BytesIO
from glob import glob
import os
from PIL import Image
import random

def distort(fname, scale=0.6):
    scale = int(100 * scale)
    image = Image.open(fname)
    imgdimens = image.width, image.height
    distortcmd = f"magick {fname} -liquid-rescale {scale}x{scale}%! -resize {imgdimens[0]}x{imgdimens[1]}\! result/{fname}"
#     print(distortcmd)
    os.system(distortcmd)  
#     buf = BytesIO()
#     buf.name = 'image.jpeg'

#     image = Image.open(f"result/{fname}")
#     filetype = "JPEG" if fname.endswith(".jpg") else "PNG"
#     image.save(buf, filetype)
#     buf.seek(0)

# distort("images/0.jpg")
# distort("images/AgADAgADu6wxGz-6EUleQCgkoOYay8doXA8ABAEAAwIAA3kAA_9FBAABFgQ.jpg", 0.3)