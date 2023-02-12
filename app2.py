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

def texto(img, frase, pos, fonte='arial.ttf', tamanho=60):
    """Add text to the image"""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fonte, tamanho)
    draw.text(pos, frase, font=font)
    return img

imagem1 = Image.open('laptop.jpg')
imagem2 = Image.open('paisagem.jpg')

IMAGE_WIDTH = 500
IMAGE_HEIGHT = 700

text_1 = 'Turn this...'
text_2 = '...Into that!!!'

FONT_SIZE = 50
FONT_PATH = "arial.ttf"

fonte = ImageFont.truetype(FONT_PATH, FONT_SIZE)

img1 = cortar(imagem1, IMAGE_WIDTH, IMAGE_HEIGHT)
img2 = cortar(imagem2, IMAGE_WIDTH, IMAGE_HEIGHT)
img1 = texto(img1, text_1, (150,28), FONT_PATH, FONT_SIZE)
img2 = texto(img2, text_2, (150,28), FONT_PATH, FONT_SIZE)
result = concatenar(img1, img2, IMAGE_WIDTH, IMAGE_HEIGHT)

result.save('result.jpg')