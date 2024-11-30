from PIL import Image, ImageDraw, ImageFont
import requests
import random

# Function to create a meme
def create_meme(template_path, top_text, bottom_text):
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 40)

    # Add top text
    draw.text((10, 10), top_text, font=font, fill='white')
    # Add bottom text
    width, height = draw.textsize(bottom_text, font=font)
    draw.text((image.width - width - 10, image.height - height - 10), bottom_text, font=font, fill='white')

    meme_path = 'meme.png'
    image.save(meme_path)
    print(f'Meme saved at {meme_path}')

# Example usage
create_meme('image.png', 'Top Text', 'Bottom Text')