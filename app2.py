from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def cortar(img, w, h):
    """Crop the image to the desired aspect ratio"""
    original_width, original_height = img.size
    newWidth = (original_height/(h/100))*(w/100)
    box = ((original_width-newWidth)/2, 0, (original_width+newWidth)/2, original_height)
    img = img.crop(box)
    img = img.resize((w,h))
    # img.save('teste.jpg')
    return img

def concatenar(img1, img2, width, height):
    """Concatenate two images horizontally, assuming they have the same height"""
    result = Image.new("RGB", (2*width, height), "white")
    result.paste(img1, (0, 0))
    result.paste(img2, (width, 0))
    return result

def texto(img, frase, fonte='arial.ttf', font_size=None):
    """Add text to the image"""
    if font_size is None:
        font_size = img.size[1]//12
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fonte, font_size)
    # draw in the center of the image
    width, height = img.size
    text_width, text_height = draw.textsize(frase, font=font)
    pos = ((width-text_width)/2, 0.05*height)
    stroke_width = font_size//25
    draw.text(pos, frase, font=font, stroke_width=stroke_width, stroke_fill='black')
    return img


def this_into_that(img1, img2, text1, text2, width, height, font='arial.ttf', font_size=None):
    """Merges two images horizontally, adding text to each
    img1: path to the first image
    img2: path to the second image
    text1: text to be added to the first image
    text2: text to be added to the second image
    width: width of the final image
    height: height of the final image
    font: path to the font to be used
    font_size: size of the font
    """
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    img1 = cortar(img1, width//2, height)
    img2 = cortar(img2, width//2, height)
    img1 = texto(img1, text1, font, font_size)
    img2 = texto(img2, text2, font, font_size)
    result = concatenar(img1, img2, width//2, height)
    return result

result = this_into_that('laptop.jpg', 'paisagem.jpg', 'Turn this...', '...into that!!!', 500*2, 700)
result.save('result.jpg')