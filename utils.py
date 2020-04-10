from PIL import ImageDraw, Image, ImageFont


def generate_image(text):
    image = Image.new('RGB', (500, 500), color='black')
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='5015.ttf', size=212)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2), text, font=font, fill='#157381')

    image.save("time.jpg")

