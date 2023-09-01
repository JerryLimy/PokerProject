'''
Created on Apr 12, 2023

@author: limuyang
'''
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Card
import Deck
import Hand

def get_image(card):
    return Image.open(f"cards/{card.image_file_name()}")

def text_image(w,h,hand_type,is_winner):
    image = Image.new(mode="RGB", size=(w, h), color="black")
    draw = ImageDraw.Draw(image)
    font1 = ImageFont.truetype('Arial', 15)
    font2 = ImageFont.truetype('Arial', 25)

    winner = "Winner!"
    (w1,h1) = font1.getsize(hand_type)
    (left1,top1) = ((w-w1)/2, (h-h1)/2)
    (w2,h2) = font2.getsize(winner)
    (left2,top2)=((w-w2)/2, top1+h1+10)

    draw.text(xy=(left1,top1), text=hand_type, fill=(255,255,255),font = font1)

    if is_winner: draw.text(xy=(left2,top2), text = winner, fill=(255, 0, 0),font=font2)
    return image

def make_row(images):
        image = Image.new('RGB',(sum([img.width for img in images]), images[0].height))
        left = 0
        for img in images:
            image.paste(img,(left,0))
            left += img.width
        return image
    
def make_collum(images):  
    image = Image.new('RGB',(images[0].width,sum([img.height for img in images])))
    top = 0
    for img in images:
        image.paste(img,(0,top))
        top += img.height
    return image