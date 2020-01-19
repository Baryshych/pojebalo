def text_writer(img_path,fontsize,filename):
    from PIL import Image,ImageFont,ImageDraw
    from pandas import read_csv as rc
    from random import randrange
    from textwrap3 import wrap

    a = read_csv('./kotomatrix.txt',sep = '\r',header = None)
    text_index = randrange(0,a.size)
    text = a.loc[text_index][0]
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    img_fraction = 0.50
    font = ImageFont.truetype("Arial.ttf", fontsize)
  
    margin = int(img.size[0]*0.05)
    offset = int(img.size[0]*0.7)
    for line in wrap(text, width=40):
        draw.text((margin, offset), line, (255,255,0), font=font)
        offset += font.getsize(line)[1]
        
    img.save("/DL/Hackathon_2020/koto_{}.jpeg".format(filename))
